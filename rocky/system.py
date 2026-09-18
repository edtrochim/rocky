"""The ``systems/<slug>/`` folder: read and write a classification system's nodes.

Every skill's "apply" step goes through here so that class nodes, the table
and SYSTEM.md stay consistent and are written deterministically. The class
node is the human view; ``elements.csv`` is the machine view; both are
derived from the same rows.

Class node frontmatter::

    id: system:<slug>:<code_slug>   kind: class   system: system:<slug>
    code, name, status (titles_only | proposed | accepted | disputed | registered)
    definition_language, parent_code, colour
    element_refs, confidence, land_use_hint, open_questions
    nearest_examples: [registry ids]
    links: in_system, uses_type, named_by, motivated_by, nearest_example
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path

from . import OKF_ROOT, okf
from .table import Row, Table

SYSTEMS = OKF_ROOT / "systems"
STATUSES = ("titles_only", "proposed", "accepted", "disputed", "registered")


def slugify(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", (s or "").strip()).strip("-")
    return s or "x"


def system_dir(slug: str) -> Path:
    return SYSTEMS / slug


def class_path(slug: str, code_or_name: str) -> Path:
    return system_dir(slug) / "classes" / f"{slugify(code_or_name)}.md"


# ------------------------------------------------------------- SYSTEM.md
def write_system(slug: str, meta: dict, classes: list[dict]) -> Path:
    """meta: name, publisher, version, jurisdiction, scope_statement, sources (list), language, notes."""
    d = system_dir(slug)
    p = d / "SYSTEM.md"
    links = [okf.link("has_class", f"system:{slug}:{slugify(c.get('code') or c.get('name'))}", p,
                      class_path(slug, c.get("code") or c.get("name"))) for c in classes]
    front = {"id": f"system:{slug}", "kind": "system", "title": meta.get("name", slug), "slug": slug,
             "publisher": meta.get("publisher", ""), "version": meta.get("version", ""),
             "jurisdiction": meta.get("jurisdiction", ""), "language": meta.get("language", ""),
             "n_classes": len(classes), "mode": meta.get("mode", "propose"),
             "sources": meta.get("sources", []), "run_history": meta.get("run_history", []),
             "links": links}
    rows = "\n".join(f"| {c.get('code','')} | [{c.get('name','')}](classes/{slugify(c.get('code') or c.get('name'))}.md) | {c.get('status','titles_only')} |"
                     for c in classes)
    body = (f"# {meta.get('name', slug)}\n\n"
            f"{meta.get('publisher','(publisher not stated)')} · {meta.get('version','')} · {meta.get('jurisdiction','')}\n\n"
            f"## Scope statement (verbatim)\n\n{meta.get('scope_statement') or '_none found_'}\n\n"
            + (f"## Notes\n\n{meta['notes']}\n\n" if meta.get("notes") else "")
            + "## Framing summary\n\n" + (meta.get("framing_summary") or "_not yet extracted_") + "\n\n"
            + f"## Classes ({len(classes)})\n\n| code | class | status |\n|---|---|---|\n{rows}\n")
    okf.write_node(p, front, body)
    return p


def read_system(slug: str) -> dict:
    n = okf.read_node(system_dir(slug) / "SYSTEM.md")
    return n.front


# ----------------------------------------------------------- class nodes
def decomposition_table(t: Table, cid: str) -> str:
    lines = ["| pattern | stratum | element | presence | cover | other properties | characteristics |",
             "|---|---|---|---|---|---|---|"]
    for hid in t.hps(cid):
        for sid in t.strata(cid, hid):
            st = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, record="stratum")
            spres = st.get("presenceType")
            for bid, ref in t.blocks(cid, hid, sid):
                a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                pres = a.get("elementPresenceType")
                cov = a.get("cover")
                others = []
                for k, r in a.items():
                    if k in ("elementPresenceType", "cover", "name", "description", "instanceIndex"):
                        continue
                    if r.min or r.max:
                        others.append(f"{k} {r.min}–{r.max}")
                    elif r.value:
                        others.append(f"{k}={r.value}")
                chars = []
                for chid, cref in t.chars(cid, hid, sid, bid):
                    ca = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, char_id=chid, record="characteristic")
                    vals = [f"{k}={r.value}" for k, r in ca.items() if r.value and k not in ("name", "description")]
                    chars.append(cref + (" (" + ", ".join(vals[:3]) + ")" if vals else ""))
                lines.append(f"| {hid} | {sid}{' ' + spres.value if spres and spres.value else ''} | `{ref}` | "
                             f"{pres.value if pres else ''} | {cov.min + '–' + cov.max if cov and (cov.min or cov.max) else ''} | "
                             f"{'; '.join(others[:6])} | {'; '.join(chars[:4])} |")
    return "\n".join(lines) if len(lines) > 2 else ""


def write_class(slug: str, cls: dict, table: Table | None = None) -> Path:
    """cls: code, name, definition, description, parent_code, colour, language, source_span, status,
    rationale, evidence (list of {row_path, quote}), open_questions (list), confidence, land_use_hint,
    nearest_examples (list of registry ids), framing (list of framing ids), element_refs (list).
    ``table`` supplies the decomposition rows for this class (class_id == cls['class_id'] or code)."""
    p = class_path(slug, cls.get("code") or cls.get("name"))
    sys_path = system_dir(slug) / "SYSTEM.md"
    cid = cls.get("class_id") or cls.get("code") or slugify(cls.get("name", ""))
    tbl = decomposition_table(table, cid) if table is not None else ""
    element_refs = sorted({r.ref for r in table.for_class(cid) if r.record == "element" and r.ref}) if table is not None else cls.get("element_refs", [])
    links = [okf.link("in_system", f"system:{slug}", p, sys_path)]
    for ref in element_refs:
        vp = OKF_ROOT / "vocab" / "elements" / f"{ref}.md"
        if vp.exists():
            links.append(okf.link("uses_type", f"element:{ref}", p, vp))
    for fid in cls.get("framing") or []:
        fp = system_dir(slug) / "framing" / f"{slugify(fid.split(':')[-1])}.md"
        if fp.exists():
            links.append(okf.link("motivated_by", fid, p, fp))
    for rid in cls.get("nearest_examples") or []:
        # registry ids look like registry:L16:311
        parts = rid.split(":")
        if len(parts) == 3:
            rp = OKF_ROOT / "registry" / parts[1] / "classes" / f"{parts[2]}.md"
            if rp.exists():
                links.append(okf.link("nearest_example", rid, p, rp))
    status = cls.get("status") or ("titles_only" if not tbl else "proposed")
    front = {"id": f"system:{slug}:{slugify(cls.get('code') or cls.get('name'))}", "kind": "class",
             "title": f"{cls.get('code','')} {cls.get('name','')}".strip(), "system": f"system:{slug}",
             "code": cls.get("code", ""), "name": cls.get("name", ""), "class_id": cid,
             "status": status, "parent_code": cls.get("parent_code", ""), "colour": cls.get("colour", ""),
             "definition_language": cls.get("language", ""), "source_span": cls.get("source_span", ""),
             "element_refs": element_refs, "confidence": cls.get("confidence", ""),
             "land_use_hint": cls.get("land_use_hint", ""), "nearest_examples": cls.get("nearest_examples", []),
             "open_questions": cls.get("open_questions", []), "links": links,
             "rows_in": "../elements.csv"}
    ev = "\n".join(f"- `{e.get('row_path','')}`: \"{e.get('quote','')}\"" for e in (cls.get("evidence") or []))
    body = (f"# {front['title']}\n\n## Definition (verbatim)\n\n{cls.get('definition') or '_titles only: no definition in the source_'}\n\n"
            + (f"## Description\n\n{cls['description']}\n\n" if cls.get("description") else "")
            + ("## Decomposition\n\n" + tbl + "\n\n" if tbl else "## Decomposition\n\n_not yet proposed_\n\n")
            + (f"## Rationale\n\n{cls['rationale']}\n\n" if cls.get("rationale") else "")
            + (f"## Evidence\n\n{ev}\n\n" if ev else "")
            + (f"## Nearest registry examples\n\n{cls['examples_note']}\n\n" if cls.get("examples_note") else "")
            + ("## Open questions\n\n" + "\n".join(f"- {q}" for q in cls.get("open_questions") or []) + "\n" if cls.get("open_questions") else ""))
    okf.write_node(p, front, body)
    return p


def read_class(slug: str, code_or_name: str) -> okf.Node:
    return okf.read_node(class_path(slug, code_or_name))


def list_classes(slug: str) -> list[okf.Node]:
    d = system_dir(slug) / "classes"
    return [okf.read_node(p) for p in sorted(d.glob("*.md"))] if d.exists() else []


# ------------------------------------------------------------- the table
def table_path(slug: str) -> Path:
    return system_dir(slug) / "elements.csv"


def load_table(slug: str) -> Table:
    p = table_path(slug)
    return Table.from_csv(p) if p.exists() else Table()


def save_table(slug: str, t: Table) -> Path:
    p = table_path(slug)
    t.to_csv(p)
    meta_p = system_dir(slug) / "elements.meta.json"
    meta_p.write_text(json.dumps(t.meta, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8", newline="\n")
    return p


def replace_class_rows(t: Table, cid: str, rows: list[Row]) -> Table:
    """Return a table with this class's rows replaced (class row kept if the new rows lack one)."""
    keep = [r for r in t.rows if r.class_id != cid]
    has_class_row = any(r.record == "class" for r in rows)
    old_class = [r for r in t.rows if r.class_id == cid and r.record == "class"]
    out = Table(rows=keep + (rows if has_class_row else old_class + rows), meta=dict(t.meta))
    return out


def rows_from_proposal(slug: str, cid: str, code: str, name: str, proposal: dict) -> list[Row]:
    """Turn a skill's decomposition proposal into table rows.

    proposal = {"patterns": [{"cover": [min,max]|null, "occurrence": [..]|null, "strata": [
                  {"presence": "fixed|exclusive|conditionalTemporal|precluded", "onTop": bool,
                   "elements": [{"ref": "LC_Tree", "presence": "...", "cover": [10,40]|null, "height": [..]|null,
                                 "properties": {"woodyLeafPhenology": "...", ...},
                                 "characteristics": [{"ref": "LC_VegetationArtificialityCharacteristic",
                                                      "fields": {"vegetationArtificiality": "Natural"}}],
                                 "evidence": "quoted text", "confidence": 0.0-1.0}]}]}]}
    """
    rows: list[Row] = []
    base = dict(system=slug, class_id=cid, class_map_code=code, class_name=name)
    rows.append(Row(**base, record="class", attribute="class_name", value=name))
    rows.append(Row(**base, record="class", attribute="class_map_code", value=code))
    if proposal.get("definition"):
        rows.append(Row(**base, record="class", attribute="class_description", value=proposal["definition"]))
    hp_n = 0
    st_n = 0
    for pat in proposal.get("patterns") or []:
        hp_n += 1
        hid = f"{cid}.hp{hp_n}"
        hb = dict(base, hp_id=hid)
        rows.append(Row(**hb, record="hp", attribute="name", value=f"Horizontal Pattern {hp_n}"))
        for k in ("cover", "occurrence"):
            v = pat.get(k)
            if v:
                rows.append(Row(**hb, record="hp", attribute=k, min=str(v[0]), max=str(v[1])))
        for st in pat.get("strata") or []:
            st_n += 1
            sid = f"{cid}.st{st_n}"
            sb = dict(hb, stratum_id=sid)
            rows.append(Row(**sb, record="stratum", attribute="name", value=f"Stratum {st_n}"))
            rows.append(Row(**sb, record="stratum", attribute="presenceType", value=_presence(st.get("presence"))))
            if st.get("onTop"):
                rows.append(Row(**sb, record="stratum", attribute="onTop", value="1"))
            for bi, el in enumerate(st.get("elements") or [], start=1):
                ref = el.get("ref", "")
                eb = dict(sb, block_id=f"{bi}", ref=ref)
                ev = el.get("evidence", "")
                conf = str(el.get("confidence", ""))
                rows.append(Row(**eb, record="element", attribute="elementPresenceType", value=_presence(el.get("presence")),
                                evidence=ev, confidence=conf, status="proposed"))
                for k in ("cover", "height", "depth", "portioning"):
                    v = el.get(k)
                    if v:
                        rows.append(Row(**eb, record="element", attribute=k, min=str(v[0]), max=str(v[1]), evidence=ev, confidence=conf, status="proposed"))
                for k, v in (el.get("properties") or {}).items():
                    if isinstance(v, (list, tuple)) and len(v) == 2:
                        rows.append(Row(**eb, record="element", attribute=k, min=str(v[0]), max=str(v[1]), evidence=ev, confidence=conf, status="proposed"))
                    elif v not in (None, ""):
                        rows.append(Row(**eb, record="element", attribute=k, value=str(v), evidence=ev, confidence=conf, status="proposed"))
                for ci, ch in enumerate(el.get("characteristics") or [], start=1):
                    cb = dict(eb, char_id=f"{ci}", ref=ch.get("ref", ""))
                    fields = ch.get("fields") or {}
                    if not fields:
                        rows.append(Row(**cb, record="characteristic", attribute="", value="", evidence=ev, confidence=conf, status="proposed"))
                    for k, v in fields.items():
                        if isinstance(v, (list, tuple)) and len(v) == 2:
                            rows.append(Row(**cb, record="characteristic", attribute=k, min=str(v[0]), max=str(v[1]), evidence=ev, confidence=conf, status="proposed"))
                        else:
                            rows.append(Row(**cb, record="characteristic", attribute=k, value=str(v), evidence=ev, confidence=conf, status="proposed"))
    return rows


def _presence(v: str | None) -> str:
    m = {"fixed": "Fixed", "mandatory": "Fixed", "exclusive": "Exclusive", "conditionaltemporal": "Conditional Temporal",
         "conditional temporal": "Conditional Temporal", "optional": "Conditional Temporal", "precluded": "Precluded"}
    return m.get((v or "fixed").strip().lower(), "Fixed")
