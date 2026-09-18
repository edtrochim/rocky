"""Parse the FAO LCCS3 XML schema into a vocabulary of LCML types.

The XSD (``g4g2026_ideathon.xsd``) is the authoritative list of what a class
may be made of. This module reads it into plain dictionaries so that
``okf/vocab/lccs3`` can be generated, writers can be validated against it,
and agents can look up what attributes an element type allows.

No hand-typed vocabulary anywhere else: if the XSD changes, rerun the tool.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree

XS = "http://www.w3.org/2001/XMLSchema"
NS = {"xs": XS}

# The abstract roots that partition the schema into the groups agents care about.
ROOT_ELEMENT = "LC_LandCoverElement"          # concrete descendants = atomic elements
ROOT_ELEMENT_CHAR = "LC_ElementCharacteristic"  # element-level characteristics
ROOT_CLASS_CHAR = "LC_ClassCharacteristic"      # class-level characteristics
ROOT_VALUE = "LC_Element"                       # code-list style values (Evergreen, Needleleaved ...)


@dataclass
class Attr:
    """An XML attribute or simple child element that carries a value."""

    name: str
    kind: str                     # "attribute" | "element"
    type: str | None = None       # xs type or named simpleType
    enum: list[str] = field(default_factory=list)
    min_occurs: int = 0
    max_occurs: str = "1"
    range: dict | None = None     # {"min": ..., "max": ...} for min/max attribute pairs


@dataclass
class TypeDef:
    name: str
    base: str | None
    abstract: bool
    instantiable: bool            # has a top-level xs:element of the same name
    attrs: list[Attr] = field(default_factory=list)
    children: list[Attr] = field(default_factory=list)   # complex child elements (containers)
    doc: str | None = None

    @property
    def group(self) -> str:
        return ""


def _local(tag: str) -> str:
    return tag.split("}", 1)[-1]


def _enum_from_simple(st: etree._Element) -> list[str]:
    """Enumerations come as xs:enumeration or as a '.*|A|B|C' pattern."""
    out: list[str] = []
    for e in st.iter(f"{{{XS}}}enumeration"):
        out.append(e.get("value"))
    if not out:
        for p in st.iter(f"{{{XS}}}pattern"):
            val = p.get("value") or ""
            parts = [x for x in val.split("|") if x and x != ".*"]
            out.extend(parts)
    return out


def _range_of(ct: etree._Element) -> dict | None:
    """A complexType with only min/max attributes is a numeric range."""
    names = [a.get("name") for a in ct.findall("xs:attribute", NS)]
    if set(names) == {"min", "max"} and ct.find("xs:sequence", NS) is None \
            and ct.find("xs:complexContent", NS) is None:
        base = None
        for r in ct.iter(f"{{{XS}}}restriction"):
            base = r.get("base")
            break
        return {"min": None, "max": None, "base": base}
    return None


class XsdVocab:
    def __init__(self, xsd_path: Path):
        self.path = Path(xsd_path)
        self.tree = etree.parse(str(self.path))
        self.root = self.tree.getroot()
        self.simple: dict[str, list[str]] = {}
        self.types: dict[str, TypeDef] = {}
        self.instantiable: set[str] = set()
        self._parse()

    # ------------------------------------------------------------------ parse
    def _parse(self) -> None:
        for st in self.root.findall("xs:simpleType", NS):
            self.simple[st.get("name")] = _enum_from_simple(st)
        for el in self.root.findall("xs:element", NS):
            if el.get("type"):
                self.instantiable.add(el.get("name"))
        for ct in self.root.findall("xs:complexType", NS):
            name = ct.get("name")
            if _range_of(ct) is not None:
                # treat plain ranges as simple types with a range marker
                self.simple[name] = ["<range>"]
                continue
            self.types[name] = self._type_def(ct)

    def _type_def(self, ct: etree._Element) -> TypeDef:
        name = ct.get("name")
        base = None
        body = ct
        cc = ct.find("xs:complexContent", NS)
        if cc is not None:
            ext = cc.find("xs:extension", NS)
            if ext is not None:
                base = ext.get("base")
                body = ext
        td = TypeDef(name=name, base=base, abstract=ct.get("abstract") == "true",
                     instantiable=name in self.instantiable)
        for a in body.findall("xs:attribute", NS):
            td.attrs.append(self._attr(a))
        seq = body.find("xs:sequence", NS)
        if seq is not None:
            for e in seq.findall("xs:element", NS):
                td.children.append(self._child(e))
        return td

    def _attr(self, a: etree._Element) -> Attr:
        at = Attr(name=a.get("name"), kind="attribute", type=a.get("type"))
        st = a.find("xs:simpleType", NS)
        if st is not None:
            at.enum = _enum_from_simple(st)
            r = st.find("xs:restriction", NS)
            if r is not None:
                at.type = r.get("base")
        elif at.type in self.simple:
            at.enum = list(self.simple[at.type])
        return at

    def _child(self, e: etree._Element) -> Attr:
        at = Attr(name=e.get("name"), kind="element", type=e.get("type"),
                  min_occurs=int(e.get("minOccurs", "1")), max_occurs=e.get("maxOccurs", "1"))
        inline = e.find("xs:complexType", NS)
        if inline is not None:
            rng = _range_of(inline)
            if rng is not None:
                at.range = rng
                at.type = "<range>"
            else:
                # inline container, e.g. <elements> wrapping a list of typed children
                inner = [c.get("name") + ":" + (c.get("type") or "?")
                         for c in inline.iter(f"{{{XS}}}element")]
                at.type = "{" + ",".join(inner) + "}"
                # simpleContent extension with enum base (OR mixed class items)
                sc = inline.find("xs:simpleContent/xs:extension", NS)
                if sc is not None and sc.get("base") in self.simple:
                    at.enum = list(self.simple[sc.get("base")])
        st = e.find("xs:simpleType", NS)
        if st is not None:
            at.enum = _enum_from_simple(st)
        if at.type in self.simple:
            vals = self.simple[at.type]
            if vals == ["<range>"]:
                at.range = {"min": None, "max": None}
            else:
                at.enum = list(vals)
        return at

    # -------------------------------------------------------------- queries
    def chain(self, name: str) -> list[str]:
        """Inheritance chain from the type up to the root, inclusive."""
        out = []
        cur = name
        seen = set()
        while cur and cur in self.types and cur not in seen:
            out.append(cur)
            seen.add(cur)
            cur = self.types[cur].base
        return out

    def descends_from(self, name: str, root: str) -> bool:
        return root in self.chain(name)

    def concrete_descendants(self, root: str) -> list[str]:
        return sorted(n for n, t in self.types.items()
                      if not t.abstract and n != root and self.descends_from(n, root))

    def inherited_attrs(self, name: str) -> list[tuple[str, Attr]]:
        """All attributes and simple children along the chain, nearest first."""
        out: list[tuple[str, Attr]] = []
        for t in self.chain(name):
            td = self.types[t]
            for a in td.attrs:
                out.append((t, a))
            for c in td.children:
                out.append((t, c))
        return out

    def allowed_characteristics(self, element_type: str) -> list[str]:
        """Characteristics an element may carry, by the schema's own base grouping.

        The XSD only says LC_LandCoverElement.elements holds LC_ElementCharacteristic;
        the practical restriction is by family (vegetation vs water vs artificial).
        We return every concrete LC_ElementCharacteristic whose chain shares a
        family marker with the element, falling back to all of them.
        """
        fam = self.family(element_type)
        out = []
        for c in self.concrete_descendants(ROOT_ELEMENT_CHAR):
            cf = self.family(c)
            if cf is None or fam is None or cf == fam:
                out.append(c)
        return out

    FAMILY_MARKERS = {
        "vegetation": ("LC_Vegetation", "LC_GrowthForm", "LC_CultivatedAndManagedVegetation",
                       "LC_NaturalOrSeminaturalVegetation", "LC_VegetationArtificiality"),
        "water": ("LC_WaterBodyAndAssociatedSurface", "LC_WaterAndAssociatedSurfacesCharacteristic"),
        "artificial": ("LC_ArtificialSurface", "LC_ArtificialSurfaceCharacteristic"),
        "natural_surface": ("LC_NaturalSurface", "LC_NaturalSurfaceCharacteristic"),
    }

    def family(self, name: str) -> str | None:
        ch = set(self.chain(name))
        for fam, markers in self.FAMILY_MARKERS.items():
            if ch & set(markers):
                return fam
        return None

    # ------------------------------------------------------------- export
    def to_dict(self) -> dict:
        elements = {}
        for n in self.concrete_descendants(ROOT_ELEMENT):
            elements[n] = self._export_type(n)
        el_chars = {n: self._export_type(n) for n in self.concrete_descendants(ROOT_ELEMENT_CHAR)}
        cl_chars = {n: self._export_type(n) for n in self.concrete_descendants(ROOT_CLASS_CHAR)}
        values = {n: self._export_type(n) for n in self.concrete_descendants(ROOT_VALUE)}
        other = {n: self._export_type(n) for n in sorted(self.types)
                 if n not in elements and n not in el_chars and n not in cl_chars and n not in values}
        return {
            "source": self.path.name,
            "counts": {"types": len(self.types), "elements": len(elements),
                       "element_characteristics": len(el_chars),
                       "class_characteristics": len(cl_chars), "values": len(values)},
            "elements": elements,
            "element_characteristics": el_chars,
            "class_characteristics": cl_chars,
            "values": values,
            "other_types": other,
            "simple_types": {k: v for k, v in self.simple.items()},
        }

    def _export_type(self, n: str) -> dict:
        td = self.types[n]
        attrs = []
        for owner, a in self.inherited_attrs(n):
            d = {"name": a.name, "kind": a.kind, "type": a.type, "declared_on": owner}
            if a.enum:
                d["enum"] = a.enum
            if a.range is not None:
                d["range"] = True
            if a.kind == "element":
                d["min_occurs"] = a.min_occurs
                d["max_occurs"] = a.max_occurs
            attrs.append(d)
        return {
            "name": n,
            "base": td.base,
            "chain": self.chain(n),
            "abstract": td.abstract,
            "instantiable": td.instantiable,
            "family": self.family(n),
            "attributes": attrs,
        }


def load(xsd_path: str | Path) -> XsdVocab:
    return XsdVocab(Path(xsd_path))


if __name__ == "__main__":  # quick look
    import json, sys
    v = load(sys.argv[1])
    d = v.to_dict()
    print(json.dumps(d["counts"], indent=1))
    print("elements:", ", ".join(d["elements"]))
