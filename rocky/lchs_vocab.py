"""Parse the LChS schema into the primary LCML vocabulary.

The LChS XSD (ISO 19144-2:2023 as FAO serialises it) is annotated: every
type, property and enumeration value carries an ``xs:documentation``. That
makes it the best single source for what an agent may put in a class:

* element types      ``LC_TreeType`` ... referenced in files as ``BlockReference = LC_Tree``
* characteristic types ``LC_WaterSalinityCharacteristicType`` ... referenced as
  ``CharacteristicReference = LC_WaterSalinityCharacteristic``
* record types       ``LC_ClassType``, ``LC_StrataType`` ... the flat records of a file
* enumerations       with per-value documentation

Property values in files come as repeated elements for ranges (``<cover>30</cover>
<cover>70</cover>``) which the schema expresses as ``maxOccurs="2"``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree

from .schemas import LCHS_XSD, lchs_schema_text

XS = "{http://www.w3.org/2001/XMLSchema}"

RECORD_TYPES = {
    "LC_LegendType", "ObjectsContainerType", "LC_ClassType", "LC_ClassCharacteristicsType",
    "LC_HorizontalPatternsType", "LC_StrataType", "LC_PropertiesType", "LC_CharacteristicsType",
    "LC_ElementsType",
}


def _doc(node) -> str:
    d = node.find(f"{XS}annotation/{XS}documentation")
    return (d.text or "").strip() if d is not None else ""


@dataclass
class Prop:
    name: str
    type: str
    doc: str
    min_occurs: int
    max_occurs: str

    @property
    def is_range(self) -> bool:
        return self.max_occurs == "2"

    @property
    def is_enum(self) -> bool:
        return self.type.endswith("Enum")


@dataclass
class LchsType:
    name: str            # schema type name, e.g. LC_TreeType
    ref: str             # reference name used in files, e.g. LC_Tree
    kind: str            # element | characteristic | record
    doc: str
    props: list[Prop] = field(default_factory=list)


@dataclass
class Enum:
    name: str
    doc: str
    values: dict[str, str]   # value -> documentation


class LchsVocab:
    def __init__(self, xsd_path: Path = LCHS_XSD):
        self.path = Path(xsd_path)
        root = etree.fromstring(lchs_schema_text().encode("utf-8"))
        self.enums: dict[str, Enum] = {}
        self.types: dict[str, LchsType] = {}
        for st in root.findall(f"{XS}simpleType"):
            vals = {}
            for e in st.iter(f"{XS}enumeration"):
                vals[e.get("value")] = _doc(e)
            self.enums[st.get("name")] = Enum(st.get("name"), _doc(st), vals)
        for ct in root.findall(f"{XS}complexType"):
            name = ct.get("name").strip()
            kind = ("record" if name in RECORD_TYPES
                    else "characteristic" if "Characteristic" in name or name in
                    ("LC_ArtificialSurfaceTypesType", "LC_ConstructionUseType")
                    else "element")
            t = LchsType(name=name, ref=name[:-4] if name.endswith("Type") else name,
                         kind=kind, doc=_doc(ct))
            seq = ct.find(f"{XS}sequence")
            if seq is not None:
                for e in seq.findall(f"{XS}element"):
                    if not e.get("name"):
                        continue
                    t.props.append(Prop(e.get("name"), e.get("type") or "", _doc(e),
                                        int(e.get("minOccurs", "1")), e.get("maxOccurs", "1")))
            self.types[name] = t

    # ------------------------------------------------------------ queries
    def by_ref(self, ref: str) -> LchsType | None:
        return self.types.get(ref + "Type") or self.types.get(ref)

    def elements(self) -> dict[str, LchsType]:
        return {t.ref: t for t in self.types.values() if t.kind == "element"}

    def characteristics(self) -> dict[str, LchsType]:
        return {t.ref: t for t in self.types.values() if t.kind == "characteristic"}

    def records(self) -> dict[str, LchsType]:
        return {t.name: t for t in self.types.values() if t.kind == "record"}

    def enum_values(self, enum_name: str) -> list[str]:
        e = self.enums.get(enum_name)
        return list(e.values) if e else []

    def enum_match(self, enum_name: str, value: str) -> str | None:
        """Return the canonical enum code for a value given as code or as its
        documentation label, case-insensitively. FAO's tools write labels
        ('Hectare', 'Natural or Seminatural') where the schema declares codes
        ('ha', 'naturalOrSeminatural'); both are accepted."""
        e = self.enums.get(enum_name)
        if not e:
            return None
        v = value.strip().lower()
        for code, doc in e.values.items():
            if v == code.lower() or (doc and v == doc.strip().lower()):
                return code
        return None

    def allowed_props(self, ref: str) -> list[Prop]:
        t = self.by_ref(ref)
        return list(t.props) if t else []

    def to_dict(self) -> dict:
        def td(t: LchsType) -> dict:
            return {"name": t.name, "ref": t.ref, "kind": t.kind, "doc": t.doc,
                    "props": [{"name": p.name, "type": p.type, "doc": p.doc,
                               "range": p.is_range, "required": p.min_occurs > 0,
                               "enum": self.enum_values(p.type) if p.is_enum else None}
                              for p in t.props]}
        return {
            "source": self.path.name,
            "counts": {"elements": len(self.elements()), "characteristics": len(self.characteristics()),
                       "records": len(self.records()), "enums": len(self.enums)},
            "elements": {k: td(v) for k, v in self.elements().items()},
            "characteristics": {k: td(v) for k, v in self.characteristics().items()},
            "records": {k: td(v) for k, v in self.records().items()},
            "enums": {k: {"doc": v.doc, "values": v.values} for k, v in self.enums.items()},
        }


def load() -> LchsVocab:
    return LchsVocab()


if __name__ == "__main__":
    import json
    v = load()
    d = v.to_dict()
    print(json.dumps(d["counts"]))
    print("elements:", ", ".join(d["elements"]))
    print("characteristics:", ", ".join(d["characteristics"]))
