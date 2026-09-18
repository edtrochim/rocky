"""Read and write FAO LChS legend files (ISO 19144-2:2023 serialisation).

``read(path) -> Table`` and ``write(table, path)`` are inverses at the level
of the table: read → write → read yields an equal table. Byte identity with
FAO's own output is not a goal (attribute order on the root differs), record
content and order are preserved.

File shape::

    LC_Legend @id @legend_name @legend_description @legend_author ...
      objects
        LC_Class*                 class_id, class_name, class_description, class_map_code, class_color_code, ...
        LC_ClassCharacteristics?  _<class_id>* > <group>* > <field>*
        LC_HorizontalPatterns*    class_id, horizontal_pattern_id, name, description, cover x2, occurrence x2, type
        LC_Strata*                HPID, stratumID, name, description, presenceType, portioning x2, onTop, onTopType ...
        LC_Properties*            StratumID, BlockID, BlockReference, instanceIndex?, <property>* (ranges repeated twice)
        LC_Characteristics*       StratumID, BlockID, BlockReference, CharacteristicID, CharacteristicReference, <field>*

Ids: ``BlockID`` is a type code (1005 = LC_Tree), not a per-block id; a block
inside a stratum is identified by (StratumID, BlockID, instanceIndex). The
table's ``block_id`` is ``BlockID`` or ``BlockID.instanceIndex``.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from lxml import etree

from .table import Row, Table
from . import lchs_vocab

ROOT_ATTRS = ("id", "legend_name", "legend_description", "legend_author",
              "legend_version", "legend_date", "uuid")
INTERNAL = {"elementID", "formElementID", "objectID", "objectReference"}   # UI internals, dropped
CLASS_FIELDS = ("legend_id", "class_id", "class_name", "class_description",
                "class_map_code", "class_color_code")
HP_KEYS = ("class_id", "horizontal_pattern_id")
ST_KEYS = ("HPID", "stratumID")
PR_KEYS = ("StratumID", "BlockID", "BlockReference", "instanceIndex")
CH_KEYS = ("StratumID", "BlockID", "BlockReference", "CharacteristicID", "CharacteristicReference", "instanceIndex")

_vocab: lchs_vocab.LchsVocab | None = None


def vocab() -> lchs_vocab.LchsVocab:
    global _vocab
    if _vocab is None:
        _vocab = lchs_vocab.load()
    return _vocab


# ------------------------------------------------------------------ helpers
def _grouped(el: etree._Element, skip: set[str]) -> list[tuple[str, list[str]]]:
    """Child tags in order with their texts, repeated tags merged (ranges)."""
    order: list[str] = []
    vals: dict[str, list[str]] = defaultdict(list)
    for c in el:
        if not isinstance(c.tag, str) or c.tag in skip or c.tag in INTERNAL:
            continue
        if c.tag not in vals:
            order.append(c.tag)
        vals[c.tag].append((c.text or "").strip())
    return [(t, vals[t]) for t in order]


def _attr_rows(base: Row, record: str, el: etree._Element, skip: set[str]) -> list[Row]:
    rows = []
    for tag, texts in _grouped(el, skip):
        r = Row(**{**base.__dict__, "record": record, "attribute": tag})
        if len(texts) == 2:
            r.min, r.max = texts
        elif len(texts) == 1:
            r.value = texts[0]
        else:  # 3+ repeats: keep as ';'-joined value, note it
            r.value = ";".join(texts)
            r.note = f"{len(texts)} repeats"
        rows.append(r)
    return rows


def _norm_name(n: str) -> str:
    return re.sub(r"[^a-z0-9]", "", n.lower())


def infer_ref(name: str, kind: str) -> str | None:
    """Map a display name ('Trees', 'Bare Rocks') to a vocabulary ref (LC_Tree, LC_BareRock)."""
    v = vocab()
    pool = v.elements() if kind == "element" else v.characteristics()
    by_norm = {_norm_name(ref[3:]): ref for ref in pool}
    n = _norm_name(name)
    for cand in (n, n[:-1] if n.endswith("s") else n, n + "s"):
        if cand in by_norm:
            return by_norm[cand]
    # documentation match ('Vegetation Artificiality Characteristic')
    for ref, t in pool.items():
        if _norm_name(t.doc) in (n, n + "characteristic"):
            return ref
    # legacy exports use LCCS3 display names ('Rainfed', 'Urban Park'): go through the crosswalk
    from . import crosswalk
    table = crosswalk.CHAR_LCCS3_TO_LCHS if kind == "characteristic" else crosswalk.ELEMENT_LCCS3_TO_LCHS
    for lccs3_type, (lchs_ref, _note) in table.items():
        if _norm_name(lccs3_type[3:]) == n:
            return lchs_ref
    return None


# --------------------------------------------------------------------- read
def read(path: str | Path, system: str = "") -> Table:
    tree = etree.parse(str(path))
    root = tree.getroot()
    t = Table()
    t.meta = {k: root.get(k) for k in ROOT_ATTRS if root.get(k) is not None}
    t.meta["format"] = "lchs"
    t.meta["source"] = str(path)
    for k, v in t.meta.items():
        if k in ROOT_ATTRS:
            t.add(system=system, record="legend", attribute=k, value=v)
    objs = root.find("objects")
    if objs is None:
        return t

    # classes
    class_info: dict[str, tuple[str, str]] = {}
    for c in objs.findall("LC_Class"):
        cid = (c.findtext("class_id") or "").strip()
        name = (c.findtext("class_name") or "").strip()
        code = (c.findtext("class_map_code") or "").strip()
        class_info[cid] = (code, name)
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name)
        t.extend(_attr_rows(base, "class", c, set()))

    # class characteristics: <LC_ClassCharacteristics><_5><geographical_aspects><...>
    cc = objs.find("LC_ClassCharacteristics")
    if cc is not None:
        for cnode in cc:
            if not isinstance(cnode.tag, str):
                continue
            cid = cnode.tag.lstrip("_")
            code, name = class_info.get(cid, ("", ""))
            base = Row(system=system, class_id=cid, class_map_code=code, class_name=name)
            for grp in cnode:
                if not isinstance(grp.tag, str):
                    continue
                if len(grp) == 0:
                    r = Row(**{**base.__dict__, "record": "class_char", "ref": grp.tag,
                               "attribute": "", "value": (grp.text or "").strip()})
                    t.rows.append(r)
                else:
                    gb = Row(**{**base.__dict__, "ref": grp.tag})
                    t.extend(_attr_rows(gb, "class_char", grp, set()))

    # horizontal patterns
    hp_class: dict[str, str] = {}
    for hp in objs.findall("LC_HorizontalPatterns"):
        cid = (hp.findtext("class_id") or "").strip()
        hid = (hp.findtext("horizontal_pattern_id") or "").strip()
        hp_class[hid] = cid
        code, name = class_info.get(cid, ("", ""))
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name, hp_id=hid)
        t.extend(_attr_rows(base, "hp", hp, set(HP_KEYS)))

    # strata
    st_hp: dict[str, str] = {}
    for st in objs.findall("LC_Strata"):
        hid = (st.findtext("HPID") or "").strip()
        sid = (st.findtext("stratumID") or "").strip()
        st_hp[sid] = hid
        cid = hp_class.get(hid, "")
        code, name = class_info.get(cid, ("", ""))
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name, hp_id=hid, stratum_id=sid)
        t.extend(_attr_rows(base, "stratum", st, set(ST_KEYS)))

    def ctx(sid: str) -> tuple[str, str, str, str]:
        hid = st_hp.get(sid, "")
        cid = hp_class.get(hid, "")
        code, name = class_info.get(cid, ("", ""))
        return cid, code, name, hid

    # properties (elements). FAO files may repeat (StratumID, BlockID, instanceIndex);
    # a '#n' suffix keeps such blocks apart in the table and is stripped on write.
    seen_blocks: dict[tuple[str, str], int] = {}
    seen_chars: dict[tuple[str, str, str], int] = {}
    for p in objs.findall("LC_Properties"):
        sid = (p.findtext("StratumID") or "").strip()
        bid = (p.findtext("BlockID") or "").strip()
        inst = (p.findtext("instanceIndex") or "").strip()
        ref = (p.findtext("BlockReference") or "").strip()
        note = ""
        if not ref:
            ref = infer_ref(p.findtext("name") or "", "element") or ""
            note = "ref inferred from name" if ref else "ref unknown"
        cid, code, name, hid = ctx(sid)
        block = f"{bid}.{inst}" if inst else bid
        n = seen_blocks.get((sid, block), 0) + 1
        seen_blocks[(sid, block)] = n
        if n > 1:
            block = f"{block}#{n}"
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name,
                   hp_id=hid, stratum_id=sid, block_id=block, ref=ref)
        rows = _attr_rows(base, "element", p, {"StratumID", "BlockID", "BlockReference"})
        if not rows:  # an element with no properties at all still needs a row
            rows = [Row(**{**base.__dict__, "record": "element", "attribute": "elementPresenceType", "value": ""})]
        if note:
            rows[0].note = note
        t.extend(rows)

    # characteristics
    for c in objs.findall("LC_Characteristics"):
        sid = (c.findtext("StratumID") or "").strip()
        bid = (c.findtext("BlockID") or "").strip()
        inst = (c.findtext("instanceIndex") or "").strip()
        chid = (c.findtext("CharacteristicID") or "").strip()
        ref = (c.findtext("CharacteristicReference") or "").strip()
        bref = (c.findtext("BlockReference") or "").strip()
        note = ""
        if not ref:
            ref = infer_ref(c.findtext("name") or c.findtext("CharacteristicLabel") or "", "characteristic") or ""
            note = "ref inferred from name" if ref else "ref unknown"
        cid, code, name, hid = ctx(sid)
        block = f"{bid}.{inst}" if inst else bid
        char = f"{chid}.{inst}" if inst else chid
        n = seen_chars.get((sid, block, char), 0) + 1
        seen_chars[(sid, block, char)] = n
        if n > 1:
            char = f"{char}#{n}"
        base = Row(system=system, class_id=cid, class_map_code=code, class_name=name,
                   hp_id=hid, stratum_id=sid, block_id=block, char_id=char, ref=ref)
        rows = _attr_rows(base, "characteristic", c,
                          {"StratumID", "BlockID", "BlockReference", "CharacteristicID", "CharacteristicReference"})
        if bref:
            rows.insert(0, Row(**{**base.__dict__, "record": "characteristic", "attribute": "BlockReference", "value": bref}))
        if not rows:
            rows = [Row(**{**base.__dict__, "record": "characteristic", "attribute": "", "value": ""})]
        if note:
            rows[0].note = note
        t.extend(rows)
    return t


# -------------------------------------------------------------------- write
def _put(parent: etree._Element, tag: str, row: Row) -> None:
    if tag.startswith("@") or "/" in tag or "[" in tag or tag in ("lccs3_type", "uuid"):
        return  # table-only or LCCS3-native rows never become LChS tags
    if row.min != "" or row.max != "":
        etree.SubElement(parent, tag).text = row.min
        etree.SubElement(parent, tag).text = row.max
    else:
        etree.SubElement(parent, tag).text = row.value


def _unique(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def _split_block(block_id: str) -> tuple[str, str]:
    """'1005.0#2' -> ('1005', '0'): the '#n' disambiguator is table-only."""
    block_id = block_id.split("#", 1)[0]
    if "." in block_id:
        b, i = block_id.split(".", 1)
        return b, i
    return block_id, ""


def _normalise(t: Table) -> Table:
    """Rows in LChS terms. Tables read from LCCS3 carry LCCS3 attribute names and
    an ``lccs3_type`` marker per element; convert those and drop table-only rows."""
    from . import lccs3_to_lchs, crosswalk
    if not any(r.attribute == "lccs3_type" for r in t.rows):
        return t
    out = Table()
    out.meta = dict(t.meta)
    dropped = []
    groups: dict[tuple, list[Row]] = {}
    order: list[tuple] = []
    for r in t.rows:
        k = (r.record, r.class_id, r.hp_id, r.stratum_id, r.block_id, r.char_id)
        if k not in groups:
            groups[k] = []
            order.append(k)
        groups[k].append(r)
    blk_ord: dict[tuple, int] = {}
    for k in order:
        rows = [Row(**r.__dict__) for r in groups[k]]   # never mutate the caller's table
        rec = k[0]
        if rec == "hp":
            out.extend(lccs3_to_lchs.hp_rows(rows))
        elif rec == "stratum":
            out.extend(lccs3_to_lchs.stratum_rows(rows))
        elif rec == "element":
            typ = next((r.value for r in rows if r.attribute == "lccs3_type"), "")
            ref, new, drop = lccs3_to_lchs.element(rows, typ)
            code = crosswalk.LCHS_BLOCK_CODES.get(ref)
            sid = k[3]
            n = blk_ord.get((sid, ref), 0)
            blk_ord[(sid, ref)] = n + 1
            bid = f"{code}.{n}" if code else k[4]
            for r in new:
                r.ref = ref
                r.block_id = bid
            if not any(r.attribute == "instanceIndex" for r in new):
                new.append(Row(**{**new[0].__dict__, "attribute": "instanceIndex", "value": str(n), "min": "", "max": ""}))
            out.extend(new)
            if drop:
                dropped.append({"class_id": k[1], "stratum_id": sid, "ref": ref, "attributes": drop})
        elif rec == "characteristic":
            typ = next((r.value for r in rows if r.attribute == "lccs3_type"), "")
            ref, new, drop = lccs3_to_lchs.characteristic(rows, typ)
            code = crosswalk.LCHS_CHAR_CODES.get(ref)
            # the block this characteristic belongs to was renumbered above
            parent = next((r for r in out if r.record == "element" and (r.class_id, r.hp_id, r.stratum_id) == k[1:4]
                           and r.block_id.split(".")[0] in (crosswalk.LCHS_BLOCK_CODES.get(r.ref, ""), k[4])
                           and (r.block_id == k[4] or r.block_id.endswith(f".{int(k[4]) - 1 if k[4].isdigit() else 0}"))), None)
            bid = parent.block_id if parent else k[4]
            for r in new:
                r.ref = ref
                r.block_id = bid
                r.char_id = f"{code}.{bid.split('.')[-1]}" if code and "." in bid else (code or k[5])
            out.extend(new)
            if drop:
                dropped.append({"class_id": k[1], "stratum_id": k[3], "char": ref, "fields": drop})
        elif rec == "class":
            out.extend(r for r in rows if r.attribute != "uuid")
        elif rec == "class_char" and rows and rows[0].ref.startswith("LC_"):
            group, new, drop = lccs3_to_lchs.class_char(rows, rows[0].ref)
            out.extend(new)
            if drop:
                dropped.append({"class_id": k[1], "class_char": rows[0].ref, "fields": drop})
        else:
            out.extend(rows)
    if dropped:
        out.meta["dropped_on_lchs_write"] = dropped
    return out


def to_tree(t: Table) -> etree._ElementTree:
    t = _normalise(t)
    meta = dict(t.meta)
    for r in t.rows:
        if r.record == "legend" and r.attribute in ROOT_ATTRS and r.attribute not in meta:
            meta[r.attribute] = r.value
    root = etree.Element("LC_Legend")
    for k in ROOT_ATTRS:
        if meta.get(k) is not None:
            root.set(k, str(meta[k]))
    objs = etree.SubElement(root, "objects")

    classes = _unique(r.class_id for r in t.rows if r.record == "class")
    for cid in classes:
        el = etree.SubElement(objs, "LC_Class")
        mine = [r for r in t.rows if r.record == "class" and r.class_id == cid]
        attrs = {r.attribute for r in mine}
        if "legend_id" not in attrs:
            etree.SubElement(el, "legend_id").text = str(meta.get("id") or "1")
        if "class_id" not in attrs:
            etree.SubElement(el, "class_id").text = cid
        for r in mine:
            _put(el, r.attribute, r)

    cc_rows = [r for r in t.rows if r.record == "class_char"]
    if cc_rows:
        cc = etree.SubElement(objs, "LC_ClassCharacteristics")
        for cid in _unique(r.class_id for r in cc_rows):
            cnode = etree.SubElement(cc, f"_{cid}")
            for grp in _unique(r.ref for r in cc_rows if r.class_id == cid):
                g = etree.SubElement(cnode, grp)
                for r in cc_rows:
                    if r.class_id == cid and r.ref == grp:
                        if r.attribute == "":
                            g.text = r.value
                        else:
                            _put(g, r.attribute, r)

    hp_rows = [r for r in t.rows if r.record == "hp"]
    for cid, hid in _unique((r.class_id, r.hp_id) for r in hp_rows):
        el = etree.SubElement(objs, "LC_HorizontalPatterns")
        etree.SubElement(el, "class_id").text = cid
        etree.SubElement(el, "horizontal_pattern_id").text = hid
        for r in hp_rows:
            if (r.class_id, r.hp_id) == (cid, hid):
                _put(el, r.attribute, r)

    st_rows = [r for r in t.rows if r.record == "stratum"]
    for hid, sid in _unique((r.hp_id, r.stratum_id) for r in st_rows):
        el = etree.SubElement(objs, "LC_Strata")
        etree.SubElement(el, "HPID").text = hid
        etree.SubElement(el, "stratumID").text = sid
        for r in st_rows:
            if (r.hp_id, r.stratum_id) == (hid, sid):
                _put(el, r.attribute, r)

    el_rows = [r for r in t.rows if r.record == "element"]
    for sid, block, ref in _unique((r.stratum_id, r.block_id, r.ref) for r in el_rows):
        el = etree.SubElement(objs, "LC_Properties")
        bid, inst = _split_block(block)
        etree.SubElement(el, "StratumID").text = sid
        etree.SubElement(el, "BlockID").text = bid
        if ref:
            etree.SubElement(el, "BlockReference").text = ref
        for r in el_rows:
            if (r.stratum_id, r.block_id) == (sid, block):
                _put(el, r.attribute, r)

    ch_rows = [r for r in t.rows if r.record == "characteristic"]
    for sid, block, char, ref in _unique((r.stratum_id, r.block_id, r.char_id, r.ref) for r in ch_rows):
        el = etree.SubElement(objs, "LC_Characteristics")
        bid, _inst = _split_block(block)
        chid, _ = _split_block(char)
        etree.SubElement(el, "StratumID").text = sid
        etree.SubElement(el, "BlockID").text = bid
        mine = [r for r in ch_rows if (r.stratum_id, r.block_id, r.char_id) == (sid, block, char)]
        for r in mine:
            if r.attribute == "BlockReference":
                etree.SubElement(el, "BlockReference").text = r.value
        etree.SubElement(el, "CharacteristicID").text = chid
        if ref:
            etree.SubElement(el, "CharacteristicReference").text = ref
        for r in mine:
            if r.attribute in ("", "BlockReference"):
                continue
            _put(el, r.attribute, r)
    return etree.ElementTree(root)


def write(t: Table, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tree = to_tree(t)
    tree.write(str(path), encoding="UTF-8", xml_declaration=True, pretty_print=True, standalone=True)
    return path
