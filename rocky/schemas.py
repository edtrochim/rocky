"""Schema files and validators for the two FAO formats.

``schemas/lccs3.xsd``  LCCS v3 (byte-identical to the per-legend .xsd the
                       registry ships with every LCCS3 legend).
``schemas/lchs.xsd``   Land Characterization System, FAO's serialisation of
                       ISO 19144-2:2023, taken verbatim from registry legend
                       L49.

The LChS schema as published cannot be used for validation as-is:

* two declarations have invalid names (an empty ``name=""`` twice, a type
  name with a leading space);
* the record types ``LC_PropertiesType`` and ``LC_CharacteristicsType`` list
  dozens of optional elements followed by ``xs:any``, which violates XML
  Schema's Unique Particle Attribution rule, so no processor compiles them;
* FAO's own files carry fields the record types do not declare (``name``,
  ``elementID``, ``onTopID``, ``instanceIndex`` ...).

So the schema is loaded with patches applied in memory (never written back):
the invalid names are fixed and every flat record type becomes "its required
id fields, then anything". What the XSD then checks is the container shape and
the enumerations declared on the typed element and characteristic definitions.
Property names, enum values and ranges per element type are checked by
``rocky.validate`` against the vocabulary parsed from the same schema.
That split is deliberate: the schema stays FAO's, the strictness is ours.

Reading is tolerant everywhere; validation is the acceptance test for what we
write.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path

from lxml import etree

from . import REPO_ROOT

SCHEMA_DIR = REPO_ROOT / "schemas"
LCCS3_XSD = SCHEMA_DIR / "lccs3.xsd"
LCHS_XSD = SCHEMA_DIR / "lchs.xsd"
XS = "{http://www.w3.org/2001/XMLSchema}"

# Text patches: (pattern, replacement, why)
LCHS_TEXT_PATCHES = [
    (r'\s*<xs:element name="" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>', "",
     "LC_PropertiesType declares an element with an empty name"),
    (r'<xs:element name="" type="xs:string" minOccurs="0" maxOccurs="1">\s*<xs:annotation>\s*'
     r'<xs:documentation></xs:documentation>\s*</xs:annotation>\s*</xs:element>', "",
     "LC_ElementsType declares an element with an empty name"),
    (r'<xs:complexType name=" LC_IceCategoryCharacteristicType">',
     '<xs:complexType name="LC_IceCategoryCharacteristicType">',
     "type name has a leading space"),
]

# Record types relaxed to "required leading ids, then xs:any (lax)".
# value = the leading elements to keep, in order.
LCHS_RELAXED_RECORDS = {
    "LC_ClassType": ["class_id", "class_name"],
    "LC_HorizontalPatternsType": ["class_id", "horizontal_pattern_id"],
    "LC_StrataType": ["HPID", "stratumID"],
    "LC_PropertiesType": ["StratumID", "BlockID"],
    "LC_CharacteristicsType": ["StratumID", "BlockID"],
}

_cache: dict[str, etree.XMLSchema] = {}


def lchs_schema_text() -> str:
    """The LChS schema with the text-level patches applied (parseable XML)."""
    text = LCHS_XSD.read_text(encoding="utf-8")
    for pat, rep, why in LCHS_TEXT_PATCHES:
        text, n = re.subn(pat, rep, text)
        if n == 0:
            raise RuntimeError(f"LChS schema patch did not apply: {why}")
    return text


def lchs_schema_doc() -> etree._Element:
    """The LChS schema as a DOM with record types relaxed so it compiles.

    The flat record types become ``xs:any`` (lax) because FAO's files order
    and extend their fields freely; the required ids are enforced by
    ``rocky.validate`` instead. The root gains ``xs:anyAttribute`` for the
    same reason (``elementID``, ``objectReference`` ... appear on it).
    """
    root = etree.fromstring(lchs_schema_text().encode("utf-8"))
    for ct in root.findall(f"{XS}complexType"):
        name = (ct.get("name") or "").strip()
        if name in LCHS_RELAXED_RECORDS:
            seq = ct.find(f"{XS}sequence")
            for e in list(seq):
                seq.remove(e)
            etree.SubElement(seq, f"{XS}any", minOccurs="0", maxOccurs="unbounded", processContents="lax")
        elif name == "LC_LegendType":
            etree.SubElement(ct, f"{XS}anyAttribute", processContents="lax")
    return root


def lccs3_schema() -> etree.XMLSchema:
    if "lccs3" not in _cache:
        _cache["lccs3"] = etree.XMLSchema(etree.parse(str(LCCS3_XSD)))
    return _cache["lccs3"]


def lchs_schema() -> etree.XMLSchema:
    if "lchs" not in _cache:
        _cache["lchs"] = etree.XMLSchema(lchs_schema_doc())
    return _cache["lchs"]


def _errors(schema: etree.XMLSchema, tree) -> list[str]:
    if schema.validate(tree):
        return []
    return [f"{e.line}: {e.message}" for e in schema.error_log]


def _tree(x):
    return etree.parse(str(x)) if isinstance(x, (str, Path)) else x


def validate_lccs3(tree_or_path) -> list[str]:
    return _errors(lccs3_schema(), _tree(tree_or_path))


def validate_lchs(tree_or_path) -> list[str]:
    return _errors(lchs_schema(), _tree(tree_or_path))
