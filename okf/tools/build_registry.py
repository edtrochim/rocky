"""build_registry: turn the raw LCLR cache into OKF nodes.

    python okf/tools/build_registry.py [--refresh]

Reads ``okf/registry/_raw`` (fetching it first with ``--refresh`` or when
missing) and writes, per registered legend, a ``SYSTEM.md`` node, one class
node per class with the definition text and the element rows parsed from the
legend file, and ``elements.csv``. Plus ``registry/INDEX.md``. Files in
``_raw`` stay verbatim and are the provenance for everything here.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import OKF_ROOT, out, rel
from rocky import registry, lchs, lccs, okf, validate
from rocky.table import Table

REG = OKF_ROOT / "registry"
RAW = REG / "_raw"


def slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", s.strip()).strip("-")
    return s or "class"


def short(s: str, n: int = 160) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def class_table(t: Table, cid: str) -> tuple[str, list[dict]]:
    """A compact per-class decomposition table and the rows as dicts (non-empty fields only)."""
    lines = ["| pattern | stratum | element | presence | cover | other properties | characteristics |",
             "|---|---|---|---|---|---|---|"]
    rows_out = []
    for hid in t.hps(cid):
        for sid in t.strata(cid, hid):
            st = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, record="stratum")
            spres = st.get("presenceType", st.get("presence_type"))
            for bid, ref in t.blocks(cid, hid, sid):
                a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                pres = a.get("elementPresenceType", a.get("presence_type"))
                cov = a.get("cover")
                others = []
                for k, r in a.items():
                    if k in ("elementPresenceType", "presence_type", "cover", "lccs3_type", "name", "description",
                             "instanceIndex", "uuid") or k.startswith("@"):
                        continue
                    if r.min or r.max:
                        if (r.min, r.max) in (("0", "100"), ("0.0", "100.0"), ("1", "12")):
                            continue
                        others.append(f"{k} {r.min}–{r.max}")
                    elif r.value:
                        others.append(f"{k}={r.value}")
                chars = []
                for chid, cref in t.chars(cid, hid, sid, bid):
                    ca = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, char_id=chid, record="characteristic")
                    vals = [f"{k}={r.value}" for k, r in ca.items()
                            if r.value and k not in ("name", "description", "lccs3_type", "CharacteristicLabel", "BlockReference", "instanceIndex")]
                    chars.append(cref + (" (" + ", ".join(vals[:3]) + ")" if vals else ""))
                lines.append(f"| {hid} | {sid}{' ' + spres.value if spres and spres.value else ''} | `{ref}` | "
                             f"{pres.value if pres else ''} | {cov.min + '–' + cov.max if cov and (cov.min or cov.max) else ''} | "
                             f"{'; '.join(others[:6])} | {'; '.join(chars[:4])} |")
    for r in t.for_class(cid):
        d = {k: v for k, v in r.__dict__.items() if v and k not in ("system", "class_name", "class_map_code", "evidence", "framing_ref", "confidence", "status")}
        rows_out.append(d)
    return "\n".join(lines), rows_out


def build_legend(entry: dict, index_path: Path) -> dict | None:
    code = entry.get("alphaCode")
    fmt = registry.legend_format(entry)
    d = REG / code
    files = sorted((RAW / code).glob("*")) if (RAW / code).exists() else []
    if not files:
        return None
    src = next((f for f in files if f.suffix.lower() in (".lchs", ".lccs")), None)
    t = None
    if src is not None:
        t = lchs.read(src, code) if src.suffix.lower() == ".lchs" else lccs.read(src, code)
        t.to_csv(d / "elements.csv")
    findings = validate.validate(t) if t is not None else []
    vsum = validate.summary(findings)

    # class nodes: index classes joined to file classes by map code, then by name
    file_classes = {c[1]: c for c in t.classes()} if t is not None else {}
    by_name = {c[2].strip().lower(): c for c in t.classes()} if t is not None else {}
    class_links = []
    n_matched = 0
    seen_slugs: set[str] = set()
    for c in entry.get("class") or []:
        ccode = str(c.get("code") or c.get("alpha_Code") or "").strip()
        name = (c.get("name") or "").strip()
        s = slug(ccode or name)
        while s in seen_slugs:
            s += "_"
        seen_slugs.add(s)
        path = d / "classes" / f"{s}.md"
        fc = file_classes.get(ccode) or by_name.get(name.lower())
        rows, tbl = [], ""
        element_refs: list[str] = []
        cid = ""
        if fc is not None:
            n_matched += 1
            cid = fc[0]
            tbl, rows = class_table(t, cid)
            element_refs = sorted({r.ref for r in t.for_class(cid) if r.record == "element" and r.ref})
        links = [okf.link("in_system", f"registry:{code}", path, d / "SYSTEM.md")]
        for ref in element_refs:
            vp = OKF_ROOT / "vocab" / "elements" / f"{ref}.md"
            if vp.exists():
                links.append(okf.link("uses_type", f"element:{ref}", path, vp))
        front = {
            "id": f"registry:{code}:{s}", "kind": "class", "title": f"{ccode} {name}".strip(),
            "system": f"registry:{code}", "code": ccode, "name": name,
            "status": "registered", "decomposed": fc is not None, "file_class_id": cid,
            "n_rows": len(rows), "rows_in": "../elements.csv",
            "element_refs": element_refs, "links": links,
            "sources": [rel(src)] if src else [],
        }
        definition = (c.get("definition") or "").strip()
        desc = (c.get("description") or "").strip()
        head = (f"# {ccode} {name}\n\n## Definition (verbatim, FAO LCLR)\n\n{definition or '_none given_'}\n\n"
                + (f"## Description\n\n{desc}\n\n" if desc and desc != "-" else ""))
        if tbl:
            body = head + "## Decomposition (from the registry file)\n\n" + tbl + "\n\nFull rows: `../elements.csv`, class_id `" + cid + "`.\n"
        else:
            body = head + "## Decomposition\n\n_This class was not found in the legend file by code or name; rows are empty._\n"
        try:
            okf.write_node(path, front, body)
        except ValueError:
            lines = tbl.split("\n")
            body = head + "## Decomposition (from the registry file, first rows)\n\n" + "\n".join(lines[:40]) + \
                f"\n\n_{len(lines) - 2} element rows in total; see `../elements.csv`, class_id `{cid}`._\n"
            okf.write_node(path, front, body)
        class_links.append(okf.link("has_class", front["id"], d / "SYSTEM.md", path))

    ref = entry.get("references") if isinstance(entry.get("references"), dict) else {}
    datasets = entry.get("dataset") or []
    sys_path = d / "SYSTEM.md"
    front = {
        "id": f"registry:{code}", "kind": "system", "title": entry.get("name", code),
        "alpha_code": code, "country": entry.get("country"), "m49": entry.get("M49CountryCode"),
        "iso3": entry.get("ISO3CountryCode"), "year": entry.get("year"), "status": entry.get("status"),
        "legend_type": entry.get("legend_Type"), "format": fmt,
        "publisher": ref.get("PublisherOrg") or ref.get("AuthorOrganization") or "",
        "reference_link": ref.get("refLink") or "", "reference_file": ref.get("FileName") or "",
        "n_classes_index": len(entry.get("class") or []), "n_classes_file": len(t.classes()) if t is not None else 0,
        "n_classes_matched": n_matched, "n_datasets": len(datasets),
        "files": [rel(f) for f in files], "vocabulary": vsum,
        "links": [okf.link("in_registry", "registry", sys_path, index_path)] + class_links,
        "sources": [registry.INDEX_URL],
    }
    cls_lines = "\n".join(f"| {c.get('code') or ''} | [{c.get('name')}](classes/{slug(str(c.get('code') or c.get('name') or ''))}.md) | {short(c.get('definition'), 110)} |"
                          for c in (entry.get("class") or [])[:120])
    ds_lines = "\n".join(f"- {x.get('name')} ({x.get('GeonetworkIdentifier') or 'no GeoNetwork id'})" for x in datasets[:8])
    body = (f"# {entry.get('name')}\n\n"
            f"{entry.get('country')} · {entry.get('year')} · {entry.get('legend_Type')} · status {entry.get('status')}. "
            f"Publisher: {front['publisher'] or 'not stated'}. "
            f"{len(entry.get('class') or [])} classes in the registry index, {front['n_classes_file']} in the legend file, {n_matched} matched by code or name.\n\n"
            + (f"Reference: {ref.get('Name') or ''} ({ref.get('publishedYear') or ''}), {ref.get('refLink') or ''}\n\n" if ref else "")
            + (f"## Datasets ({len(datasets)})\n\n{ds_lines}\n\n" if datasets else "")
            + f"## Vocabulary check of the registry file\n\n{vsum['errors']} errors, {vsum['warnings']} warnings from `rocky.validate` (see `elements.csv`).\n\n"
            + f"## Classes\n\n| code | class | definition |\n|---|---|---|\n{cls_lines}\n")
    try:
        okf.write_node(sys_path, front, body)
    except ValueError:
        body = body.split("## Classes")[0] + "## Classes\n\nSee `classes/` (too many to list here).\n"
        okf.write_node(sys_path, front, body)
    return {"code": code, "format": fmt, "classes": len(entry.get("class") or []), "matched": n_matched,
            "vocabulary": vsum}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    if a.refresh or not (RAW / "index.json").exists():
        registry.fetch_all(RAW, refresh=a.refresh, log=lambda s: None)
    index = registry.load_index(RAW)
    index_path = REG / "INDEX.md"
    results = []
    links = []
    for entry in index:
        r = build_legend(entry, index_path)
        if r:
            results.append(r)
            links.append(okf.link("see", f"registry:{r['code']}", index_path, REG / r["code"] / "SYSTEM.md"))
    rows = "\n".join(
        f"| [{e.get('alphaCode')}]({e.get('alphaCode')}/SYSTEM.md) | {e.get('name')} | {e.get('country')} | {e.get('year')} | "
        f"{e.get('legend_Type')} | {registry.legend_format(e)} | {len(e.get('class') or [])} |"
        for e in index if (RAW / (e.get('alphaCode') or '')).exists())
    manifest = json.loads((RAW / "manifest.json").read_text(encoding="utf-8"))
    fetched = manifest.get("_index", {}).get("fetched", "")
    front = {"id": "registry", "kind": "registry_index", "title": "FAO Land Cover Legend Registry",
             "fetched": fetched, "legends": len(results), "sources": [registry.INDEX_URL, registry.BUCKET], "links": links}
    body = (f"# FAO Land Cover Legend Registry (LCLR)\n\nFetched {fetched} from {registry.INDEX_URL}. "
            f"{len(results)} legends with files. Each legend folder holds `SYSTEM.md`, one node per class under `classes/`, "
            f"and `elements.csv` (the table projection of the FAO file). Verbatim files are under `_raw/<code>/`.\n\n"
            "Use these as worked examples: every class pairs a prose definition with FAO's own element decomposition. "
            "`lchs` legends follow ISO 19144-2:2023; `lccs3` legends the 2012 edition.\n\n"
            "| code | legend | country | year | type | format | classes |\n|---|---|---|---|---|---|---|\n" + rows + "\n")
    okf.write_node(index_path, front, body)
    out({"ok": True, "legends": len(results),
         "by_format": {f: sum(1 for r in results if r["format"] == f) for f in ("lchs", "lccs3", "none")},
         "classes": sum(r["classes"] for r in results), "matched": sum(r["matched"] for r in results)})


if __name__ == "__main__":
    main()
