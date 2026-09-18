"""Read and write FAO LCCS v3 ``.lccs`` legend files.

The LCCS3 file is nested and typed with ``xsi:type``; the table is flat.
Nested typed sub-structures inside an element or characteristic are kept
losslessly as *paths* in the ``attribute`` column::

    LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Evergreen]/percentage   min=.. max=..
    LC_Property[LC_PropertyDouble@Crop]/value                                     value=..

Segment grammar: ``tag[xsi:type@name]`` where both parts are optional. Ranges
are ``min``/``max`` attributes in LCCS3 (never repeated elements), so a row
with min/max is written back as attributes and a row with a value as text.

Element and characteristic ``ref`` values in the table are LChS names (via
``crosswalk``); the original LCCS3 type is kept in an ``lccs3_type`` row so a
round trip restores it exactly. Ids of classes, patterns and strata are kept
as the table's ids. ``LC_MixedClasses`` and ``views`` are carried verbatim in
``table.meta['lccs3_extra']``.

Writing follows the schema's element order strictly (LC_Base name and
description first, then the ``elements`` container, then the base fields,
then subtype fields), because that is what makes the output XSD-valid even
though FAO's own tool is looser.
"""

from __future__ import annotations

import re
import uuid as _uuid
from pathlib import Path

from lxml import etree

from .table import Row, Table
from . import crosswalk

XSI = "http://www.w3.org/2001/XMLSchema-instance"
XSI_TYPE = f"{{{XSI}}}type"
NSMAP = {"xsi": XSI}
CLASS_KEYS = {"name": "class_name", "description": "class_description", "map_code": "class_map_code"}
LEGEND_ORDER = ("name", "description", "author")
ELEMENT_BASE_TAIL = ("sequential_temporal_relationship", "presence_type", "cover", "portioning")
HP_TAIL = ("type", "cover", "occurance")
TABLE_ONLY = {"lccs3_type", "uuid"}

# segment grammar: tag[type@name]#ordinal, every part after tag optional
_seg = re.compile(r"^([^\[#]+)(?:\[([^@\]]*)(?:@([^\]]*))?\])?(?:#(\d+))?$")


def _type(el) -> str:
    return el.get(XSI_TYPE) or ""


def _segment(el) -> str:
    t = _type(el)
    n = el.get("name") or ""
    if t or n:
        return f"{el.tag}[{t}@{n}]" if n else f"{el.tag}[{t}]"
    return el.tag


def _flatten(el, prefix: str, base: Row, record: str, rows: list[Row], skip: set[str] = frozenset()) -> None:
    """Recursively turn children of ``el`` into rows with path attributes.

    Siblings with the same tag, type and name get ``#2``, ``#3`` ... so two
    periodic variations or two species under one parent stay distinct."""
    seen: dict[str, int] = {}
    for c in el:
        if not isinstance(c.tag, str) or c.tag in skip:
            continue
        seg = _segment(c)
        kids = [k for k in c if isinstance(k.tag, str)]
        if kids:  # only containers can collide meaningfully
            n = seen.get(seg, 0) + 1
            seen[seg] = n
            if n > 1:
                seg = f"{seg}#{n}"
        path = prefix + seg
        has_range = c.get("min") is not None or c.get("max") is not None
        text = (c.text or "").strip()
        if has_range:
            rows.append(Row(**{**base.__dict__, "record": record, "attribute": path,
                               "min": c.get("min") or "", "max": c.get("max") or ""}))
        elif not kids:
            rows.append(Row(**{**base.__dict__, "record": record, "attribute": path, "value": text}))
        else:
            if text:
                rows.append(Row(**{**base.__dict__, "record": record, "attribute": path, "value": text}))
            _flatten(c, path + "/", base, record, rows)


# --------------------------------------------------------------------- read
def read(path: str | Path, system: str = "") -> Table:
    tree = etree.parse(str(path))
    root = tree.getroot()
    t = Table()
    t.meta = {"format": "lccs3", "source": str(path)}
    for k in LEGEND_ORDER:
        v = root.findtext(k)
        if v is not None:
            t.meta["legend_" + k] = v.strip()
            t.add(system=system, record="legend", attribute="legend_" + k, value=v.strip())
    extra = {}
    for tag in ("LC_MixedClasses", "views"):
        node = root.find(tag)
        if node is not None:
            extra[tag] = etree.tostring(node, encoding="unicode")
    if extra:
        t.meta["lccs3_extra"] = extra

    for cls in root.find("elements").findall("LC_LandCoverClass"):
        cid = cls.get("id") or ""
        name = (cls.findtext("name") or "").strip()
        code = (cls.findtext("map_code") or "").strip()
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name)
        for k, attr in CLASS_KEYS.items():
            v = cls.findtext(k)
            if v is not None:
                t.add(**{**base.__dict__, "record": "class", "attribute": attr, "value": v.strip()})
        if cls.get("uuid"):
            t.add(**{**base.__dict__, "record": "class", "attribute": "uuid", "value": cls.get("uuid")})
        els = cls.find("elements")
        if els is None:
            continue
        for ci, ch in enumerate(els.findall("LC_Characteristic"), start=1):
            cb = Row(**{**base.__dict__, "ref": _type(ch), "char_id": str(ci)})
            rows: list[Row] = []
            _flatten(ch, "", cb, "class_char", rows)
            if not rows:
                rows.append(Row(**{**cb.__dict__, "record": "class_char", "attribute": "", "value": ""}))
            t.extend(rows)
        for hp in els.findall("LC_HorizontalPattern"):
            hid = hp.get("id") or ""
            hb = Row(**{**base.__dict__, "hp_id": hid})
            rows = []
            _flatten(hp, "", hb, "hp", rows, skip={"elements"})
            t.extend(rows)
            hels = hp.find("elements")
            for st in (hels.findall("LC_Stratum") if hels is not None else []):
                sid = st.get("id") or ""
                sb = Row(**{**hb.__dict__, "stratum_id": sid})
                rows = []
                _flatten(st, "", sb, "stratum", rows, skip={"elements"})
                if st.get("ontop") is not None:
                    rows.append(Row(**{**sb.__dict__, "record": "stratum", "attribute": "@ontop", "value": st.get("ontop")}))
                t.extend(rows)
                sels = st.find("elements")
                for bi, el in enumerate(sels.findall("LC_LandCoverElement") if sels is not None else [], start=1):
                    ltype = _type(el)
                    ref, note = crosswalk.element_to_lchs(ltype)
                    eb = Row(**{**sb.__dict__, "block_id": str(bi), "ref": ref})
                    rows = [Row(**{**eb.__dict__, "record": "element", "attribute": "lccs3_type", "value": ltype, "note": note})]
                    _flatten(el, "", eb, "element", rows, skip={"elements"})
                    t.extend(rows)
                    cels = el.find("elements")
                    for ci, ch in enumerate(cels.findall("LC_Characteristic") if cels is not None else [], start=1):
                        ctype = _type(ch)
                        cref, cnote = crosswalk.char_to_lchs(ctype)
                        cb = Row(**{**eb.__dict__, "char_id": str(ci), "ref": cref})
                        rows = [Row(**{**cb.__dict__, "record": "characteristic", "attribute": "lccs3_type", "value": ctype, "note": cnote})]
                        _flatten(ch, "", cb, "characteristic", rows)
                        t.extend(rows)
    return t


# -------------------------------------------------------------------- write
class _Ids:
    """Fresh ids for things the table does not identify; never collides with table ids."""

    def __init__(self, taken: set[str]):
        self.taken = set(taken)
        self.n = 0x1000

    def next(self) -> str:
        while True:
            self.n += 1
            s = format(self.n, "X")
            if s not in self.taken:
                self.taken.add(s)
                return s


def _new_uuid() -> str:
    return str(_uuid.uuid4())


def _is_base(tag: str) -> bool:
    return tag.startswith("LC_")


_containers: dict[tuple[int, str], etree._Element] = {}


def _ensure_path(parent, path: str, ids: _Ids):
    """Create (or reuse) the nested element chain for a path, return the leaf.

    Intermediate containers are reused per (parent, segment) so sibling
    ordinals (``#2``) map to distinct nodes; typed and LC_* nodes get id and
    uuid because every LC_Base descendant requires them.
    """
    node = parent
    parts = path.split("/")
    for i, part in enumerate(parts):
        m = _seg.match(part)
        tag, typ, name = m.group(1), m.group(2) or "", m.group(3) or ""
        key = (id(node), part)
        hit = _containers.get(key) if i < len(parts) - 1 else None
        found = hit[1] if hit is not None and hit[0] is node else None
        if found is None:
            found = etree.SubElement(node, tag)
            if typ:
                found.set(XSI_TYPE, typ)
            if name:
                found.set("name", name)
            if (typ or _is_base(tag)) and tag != "LC_Property":
                found.set("id", ids.next())
                found.set("uuid", _new_uuid())
            if i < len(parts) - 1:
                _containers[key] = (node, found)   # holding `node` keeps its id() unique for this write
        node = found
    return node


_xsd_cache = {}


def _schema_order(xsi_type: str) -> dict[str, int]:
    """tag -> position, root type first, in the XSD's declared sequence order."""
    if "vocab" not in _xsd_cache:
        from . import xsd_vocab
        from .schemas import LCCS3_XSD
        _xsd_cache["vocab"] = xsd_vocab.load(LCCS3_XSD)
    v = _xsd_cache["vocab"]
    if xsi_type in _xsd_cache:
        return _xsd_cache[xsi_type]
    order: dict[str, int] = {}
    for t in reversed(v.chain(xsi_type)):
        for c in v.types[t].children:
            order.setdefault(c.name, len(order))
    _xsd_cache[xsi_type] = order
    return order


def _load_vocab():
    _schema_order("LC_Legend")
    return _xsd_cache["vocab"]


def _declared_child_type(enclosing: str, tag: str) -> str | None:
    v = _load_vocab()
    for t in v.chain(enclosing):
        for c in v.types[t].children:
            if c.name == tag:
                return c.type if c.type in v.types else None
    return None


def _path_key(attribute: str, top_type: str) -> tuple:
    """Sort key placing every path segment at its schema position within its enclosing type."""
    key = []
    enclosing = top_type
    for part in attribute.split("/"):
        m = _seg.match(part)
        tag, typ = (m.group(1), m.group(2) or "") if m else (part, "")
        order = _schema_order(enclosing) if enclosing else {}
        key.append(order.get(tag, len(order) + 1))
        enclosing = typ or _declared_child_type(enclosing, tag) if enclosing else typ
    return tuple(key)


def _only_schema_fields(rows: list[Row], xsi_type: str) -> tuple[list[Row], list[str]]:
    """Keep rows whose top-level tag the LCCS3 type declares; report the rest as dropped."""
    if xsi_type not in _load_vocab().types:
        return rows, []
    order = _schema_order(xsi_type)
    keep, dropped = [], []
    for r in rows:
        tag = re.split(r"[/\[]", r.attribute)[0]
        (keep if tag in order else dropped).append(r if tag in order else r.attribute)
    return keep, dropped


def _sort_by_schema(rows: list[Row], xsi_type: str) -> list[Row]:
    return sorted(rows, key=lambda r: _path_key(r.attribute, xsi_type))


def _put(parent, rows: list[Row], ids: _Ids):
    for r in rows:
        if r.attribute in TABLE_ONLY or r.attribute == "" or r.attribute.startswith("@"):
            continue
        leaf = _ensure_path(parent, r.attribute, ids)
        if r.min != "" or r.max != "":
            if r.min != "":
                leaf.set("min", r.min)
            if r.max != "":
                leaf.set("max", r.max)
        else:
            leaf.text = r.value


def _partition(rows: list[Row], tail: tuple[str, ...]):
    """(head name/description, nested 'elements/...' rows, tail base fields, subtype rest) in schema order."""
    by: dict[str, Row] = {}
    for r in rows:
        by.setdefault(r.attribute, r)
    head = [by[a] for a in ("name", "description") if a in by]
    nested = [r for r in rows if r.attribute.startswith("elements/")]
    tails = [r for r in rows if r.attribute in tail or any(r.attribute.startswith(t + "/") for t in tail)]
    tails.sort(key=lambda r: tail.index(r.attribute.split("/")[0]))
    rest = [r for r in rows if r not in head and r not in nested and r not in tails
            and r.attribute not in ("name", "description")]
    return head, nested, tails, rest


def _base_node(parent, tag: str, typ: str, node_id: str, ids: _Ids, name: str, description: str, extra_attrs=None):
    el = etree.SubElement(parent, tag)
    el.set("id", node_id or ids.next())
    for k, v in (extra_attrs or {}).items():
        el.set(k, v)
    el.set("uuid", _new_uuid())
    el.set(XSI_TYPE, typ)
    etree.SubElement(el, "name").text = name
    etree.SubElement(el, "description").text = description
    return el


def _name_desc(rows: list[Row], default_name: str) -> tuple[str, str]:
    d = {r.attribute: r.value for r in rows if r.attribute in ("name", "description")}
    return d.get("name") or default_name, d.get("description", "")


def to_tree(t: Table) -> etree._ElementTree:
    from . import lchs_to_lccs3
    _containers.clear()
    taken = {r.class_id for r in t.rows} | {r.hp_id for r in t.rows} | {r.stratum_id for r in t.rows}
    ids = _Ids(taken - {""})
    root = etree.Element("LC_Legend", nsmap=NSMAP)
    root.set("id", "1")
    root.set("lccs_sort", "0")
    root.set("uuid", _new_uuid())
    root.set(f"{{{XSI}}}noNamespaceSchemaLocation", "lccs3.xsd")
    root.set(XSI_TYPE, "LC_Legend")
    meta = dict(t.meta)
    for r in t.rows:
        if r.record == "legend" and r.attribute not in meta:
            meta[r.attribute] = r.value
    # LCCS3 requires at least one horizontal pattern per class; classes without a
    # decomposition cannot be represented and are omitted with an explicit note.
    omitted = [(cid, code, cname) for cid, code, cname in t.classes() if not t.hps(cid)]
    desc = meta.get("legend_description") or ""
    if omitted:
        desc = (desc + " " if desc else "") + (f"{len(omitted)} class(es) without an element decomposition are omitted from this "
                                               f"LCCS3 file (LCCS3 cannot hold an empty class): " + ", ".join(f"{c or cid} {n}" for cid, c, n in omitted) + ".")
        t.meta["omitted_on_lccs3_write"] = [{"class_id": cid, "code": c, "name": n} for cid, c, n in omitted]
    etree.SubElement(root, "name").text = meta.get("legend_name") or "New Legend"
    etree.SubElement(root, "description").text = desc
    top = etree.SubElement(root, "elements")
    dropped_log = []

    for cid, code, cname in t.classes():
        if not t.hps(cid):
            continue
        crow = t.attrs(class_id=cid, record="class")
        cls = _base_node(top, "LC_LandCoverClass", "LC_LandCoverClass", cid, ids, cname,
                         crow["class_description"].value if "class_description" in crow else "")
        if "uuid" in crow and crow["uuid"].value:
            cls.set("uuid", crow["uuid"].value)
        etree.SubElement(cls, "map_code").text = code
        cels = etree.SubElement(cls, "elements")

        cc_rows = [r for r in t.rows if r.record == "class_char" and r.class_id == cid]
        cc_native = _is_lccs3_native(t, cid) or any(r.ref.startswith("LC_") for r in cc_rows)
        groups = _unique((r.char_id, r.ref) for r in cc_rows) if cc_native else _unique(("", r.ref) for r in cc_rows)
        for chid, ref in groups:
            mine = [r for r in cc_rows if (r.char_id, r.ref) == (chid, ref)] if cc_native else [r for r in cc_rows if r.ref == ref]
            if not cc_native:
                ref, mine = lchs_to_lccs3.class_char(mine, ref)
                if not ref:
                    continue
            n, d = _name_desc(mine, ref[3:] if ref.startswith("LC_") else ref)
            ch = _base_node(cels, "LC_Characteristic", ref, "", ids, n, d)
            head, nested, tails, rest = _partition(mine, ())
            _put(ch, _sort_by_schema(nested + rest, ref), ids)

        for hid in t.hps(cid):
            hrows = [r for r in t.rows if r.record == "hp" and r.class_id == cid and r.hp_id == hid]
            hrows = lchs_to_lccs3.hp_rows(hrows) if not _is_lccs3_native(t, cid) else hrows
            n, d = _name_desc(hrows, "Horizontal Pattern 1")
            hp = _base_node(cels, "LC_HorizontalPattern", "LC_HorizontalPattern", hid, ids, n, d)
            hels = etree.SubElement(hp, "elements")
            for sid in t.strata(cid, hid):
                srows = [r for r in t.rows if r.record == "stratum" and (r.class_id, r.hp_id, r.stratum_id) == (cid, hid, sid)]
                srows = lchs_to_lccs3.stratum_rows(srows) if not _is_lccs3_native(t, cid) else srows
                ontop = next((r.value for r in srows if r.attribute == "@ontop"), "0") or "0"
                n, d = _name_desc(srows, "Stratum 1")
                st = _base_node(hels, "LC_Stratum", "LC_Stratum", sid, ids, n, d, {"ontop": ontop})
                sels = etree.SubElement(st, "elements")
                for bid, ref in t.blocks(cid, hid, sid):
                    erows = [r for r in t.rows if r.record == "element" and
                             (r.class_id, r.hp_id, r.stratum_id, r.block_id) == (cid, hid, sid, bid)]
                    typ = next((r.value for r in erows if r.attribute == "lccs3_type"), "")
                    native = bool(typ)
                    if not typ:
                        typ, erows, dropped = lchs_to_lccs3.element(erows, ref)
                        if dropped:
                            dropped_log.append({"class_id": cid, "stratum_id": sid, "block_id": bid, "ref": ref, "properties": dropped})
                    n, d = _name_desc(erows, typ[3:] if typ.startswith("LC_") else typ)
                    el = _base_node(sels, "LC_LandCoverElement", typ, "", ids, n, d)
                    head, nested, tails, rest = _partition(erows, ELEMENT_BASE_TAIL)
                    chs = t.chars(cid, hid, sid, bid)
                    if chs:
                        eels = etree.SubElement(el, "elements")
                        for chid, cref in chs:
                            crows = [r for r in t.rows if r.record == "characteristic" and
                                     (r.class_id, r.hp_id, r.stratum_id, r.block_id, r.char_id) == (cid, hid, sid, bid, chid)]
                            ctyp = next((r.value for r in crows if r.attribute == "lccs3_type"), "")
                            if not ctyp:
                                ctyp, crows, cdropped = lchs_to_lccs3.characteristic(crows, cref)
                                if cdropped:
                                    dropped_log.append({"class_id": cid, "stratum_id": sid, "block_id": bid, "char": cref, "fields": cdropped})
                            n, d = _name_desc(crows, ctyp[3:] if ctyp.startswith("LC_") else ctyp)
                            if not ctyp or ctyp not in _load_vocab().types:
                                # unknown in LCCS3: keep it as a user-defined characteristic named after itself
                                ctyp, crows = "LC_UserDefinedElementCharacteristic", crows + [
                                    Row(**{**crows[0].__dict__, "attribute": "userid", "value": n, "min": "", "max": ""})]
                            ch = _base_node(eels, "LC_Characteristic", ctyp, "", ids, n, d)
                            h2, nested2, tails2, rest2 = _partition(crows, ())
                            body_rows = nested2 + rest2
                            if not native:
                                body_rows, dr = _only_schema_fields(body_rows, ctyp)
                                if dr:
                                    dropped_log.append({"class_id": cid, "stratum_id": sid, "block_id": bid, "char": cref, "fields": dr})
                            _put(ch, _sort_by_schema(body_rows, ctyp), ids)
                    _put(el, tails, ids)
                    if not native:
                        rest, dr = _only_schema_fields(rest, typ)
                        if dr:
                            dropped_log.append({"class_id": cid, "stratum_id": sid, "block_id": bid, "ref": ref, "properties": dr})
                    _put(el, _sort_by_schema(rest, typ), ids)
                _put(st, [r for r in srows if r.attribute == "presence_type"], ids)
            _put(hp, sorted([r for r in hrows if r.attribute in HP_TAIL], key=lambda r: HP_TAIL.index(r.attribute)), ids)

    if dropped_log:
        t.meta["dropped_on_lccs3_write"] = dropped_log
    extra = meta.get("lccs3_extra") or {}
    if "LC_MixedClasses" in extra:
        root.append(_fix_base_order(etree.fromstring(extra["LC_MixedClasses"])))
    else:
        mc = etree.SubElement(root, "LC_MixedClasses", id=ids.next(), uuid=_new_uuid())
        mc.set(XSI_TYPE, "LC_MixedClasses")
        etree.SubElement(mc, "name").text = "Mixed Classes"
        etree.SubElement(mc, "description").text = "Contains the mixed classes of the Legend"
    if "views" in extra:
        root.append(_fix_base_order(etree.fromstring(extra["views"])))
    return etree.ElementTree(root)


def _fix_base_order(node):
    """FAO's tool writes description before name; the schema wants name first. Fix recursively."""
    for el in node.iter():
        if not isinstance(el.tag, str):
            continue
        kids = [c for c in el if isinstance(c.tag, str)]
        names = [c for c in kids if c.tag == "name"]
        descs = [c for c in kids if c.tag == "description"]
        if names and descs and kids.index(descs[0]) < kids.index(names[0]):
            el.remove(names[0])
            el.insert(kids.index(descs[0]), names[0])
    return node


def _is_lccs3_native(t: Table, cid: str) -> bool:
    return any(r.attribute == "lccs3_type" for r in t.rows if r.class_id == cid)


def _unique(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def write(t: Table, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    to_tree(t).write(str(path), encoding="UTF-8", xml_declaration=True, pretty_print=True, standalone=False)
    return path
