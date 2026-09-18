"""submission_check: assemble and verify a registry-ready package for a system.

    python okf/tools/submission_check.py --system <slug> [--build]

The package (systems/<slug>/package/) holds what the FAO LCLR lists per
legend: <code>.LChS, <code>.lccs, <code>.csv (id, hex, class code, class name),
reference.json (publisher, year, link) and README.md with the unresolved
attention items. Checks: both XML files schema-valid, csv and XML agree on the
class set, no placeholder names, every class decomposed or listed as omitted.
"""

from __future__ import annotations

import argparse
import csv
import json

from _common import OKF_ROOT, out, fail, rel
from rocky import system, lchs, lccs, schemas, apply, validate
from rocky.table import Table

PLACEHOLDERS = ("new legend", "describe the", "horizontal pattern 1", "stratum 1")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", required=True)
    ap.add_argument("--build", action="store_true", help="(re)write the package files before checking")
    a = ap.parse_args()
    slug = a.system
    d = system.system_dir(slug)
    if not (d / "SYSTEM.md").exists():
        fail(f"no system {slug}")
    meta = system.read_system(slug)
    t = system.load_table(slug)
    classes = apply._classes_of(slug)
    pkg = d / "package"
    problems, warnings = [], []
    if a.build:
        pkg.mkdir(exist_ok=True)
        t.meta.setdefault("legend_name", meta.get("title"))
        t.meta.setdefault("legend_description", "")
        t.meta.setdefault("legend_author", meta.get("publisher", ""))
        lchs.write(t, pkg / f"{slug}.LChS")
        lccs.write(t, pkg / f"{slug}.lccs")
        with (pkg / f"{slug}.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["ID", "Hex", "Class Code", "Class Name"])
            for i, c in enumerate(classes, start=1):
                w.writerow([i, c.get("colour", ""), c.get("code", ""), c.get("name", "")])
        (pkg / "reference.json").write_text(json.dumps({"name": meta.get("title"), "publisher": meta.get("publisher"),
                                                        "version": meta.get("version"), "jurisdiction": meta.get("jurisdiction"),
                                                        "sources": meta.get("sources", [])}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        att = OKF_ROOT / "attention" / f"{slug}.json"
        items = json.loads(att.read_text(encoding="utf-8")) if att.exists() else []
        undec = [c for c in classes if c.get("status") in ("titles_only", "")]
        readme = (f"# Registry submission package: {meta.get('title')}\n\n{len(classes)} classes; {len(classes) - len(undec)} decomposed, "
                  f"{len(undec)} without decomposition (present in the LChS file, omitted from the LCCS3 file).\n\n"
                  f"## Unresolved attention items ({len(items)})\n\n" + "\n".join(f"- {i.get('code','')} {i.get('name','')}: {i['kind']} - {i.get('explanation','')[:160]}" for i in items[:40]) + "\n")
        (pkg / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    for fname in (f"{slug}.LChS", f"{slug}.lccs", f"{slug}.csv"):
        if not (pkg / fname).exists():
            problems.append(f"missing {fname} (run with --build)")
    if problems:
        out({"ok": False, "problems": problems}, 1)
    e1 = schemas.validate_lchs(pkg / f"{slug}.LChS")
    e2 = schemas.validate_lccs3(pkg / f"{slug}.lccs")
    if e1:
        problems.append(f"LChS schema: {e1[0]}")
    if e2:
        problems.append(f"LCCS3 schema: {e2[0]}")
    t1 = lchs.read(pkg / f"{slug}.LChS", slug)
    codes_xml = {c[1] for c in t1.classes()}
    with (pkg / f"{slug}.csv").open(encoding="utf-8") as f:
        codes_csv = {r["Class Code"] for r in csv.DictReader(f)}
    if codes_xml != codes_csv:
        problems.append(f"csv/XML class sets differ: only csv {sorted(codes_csv - codes_xml)[:5]}, only XML {sorted(codes_xml - codes_csv)[:5]}")
    for cid, code, name in t1.classes():
        if any(p in name.lower() for p in PLACEHOLDERS):
            problems.append(f"placeholder class name '{name}'")
    undec = [c["code"] for c in classes if c.get("status") in ("titles_only", "")]
    if undec:
        warnings.append(f"{len(undec)} classes without decomposition: {undec[:10]}")
    v = validate.summary(validate.validate(t))
    out({"ok": not problems, "package": rel(pkg), "problems": problems, "warnings": warnings, "vocabulary": v,
         "classes": len(classes)}, 0 if not problems else 1)


if __name__ == "__main__":
    main()
