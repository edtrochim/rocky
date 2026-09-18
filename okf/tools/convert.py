"""convert: move a legend between the table and the two FAO formats, validating on the way.

    python okf/tools/convert.py <input> --to csv|lchs|lccs3 --out <path> [--system <slug>]
    python okf/tools/convert.py <input> --validate

Input may be .LChS, .lccs or a table .csv. Output JSON reports schema errors
(for XML written), vocabulary findings, and any properties dropped by a
cross-format write.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from _common import out, fail, rel
from rocky import lchs, lccs, validate, schemas
from rocky.table import Table


def load(path: Path, system: str) -> Table:
    ext = path.suffix.lower()
    if ext == ".lchs":
        return lchs.read(path, system)
    if ext == ".lccs":
        return lccs.read(path, system)
    if ext == ".csv":
        return Table.from_csv(path)
    fail(f"unknown input type {path.suffix}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--to", choices=["csv", "lchs", "lccs3"])
    ap.add_argument("--out")
    ap.add_argument("--system", default="")
    ap.add_argument("--validate", action="store_true")
    a = ap.parse_args()

    src = Path(a.input)
    if not src.exists():
        fail(f"{src} does not exist")
    t = load(src, a.system or src.stem)
    findings = validate.validate(t)
    report = {"ok": True, "input": rel(src), "format": t.meta.get("format", "table"),
              "classes": len(t.classes()), "rows": len(t),
              "vocabulary": validate.summary(findings),
              "findings": findings[:50]}
    if a.validate or not a.to:
        out(report)

    dest = Path(a.out) if a.out else src.with_suffix({"csv": ".csv", "lchs": ".LChS", "lccs3": ".lccs"}[a.to])
    if a.to == "csv":
        t.to_csv(dest)
    elif a.to == "lchs":
        lchs.write(t, dest)
        report["schema_errors"] = schemas.validate_lchs(dest)[:20]
        report["dropped"] = t.meta.get("dropped_on_lchs_write", [])
    else:
        lccs.write(t, dest)
        report["schema_errors"] = schemas.validate_lccs3(dest)[:20]
        report["dropped"] = t.meta.get("dropped_on_lccs3_write", [])
        report["omitted_classes"] = t.meta.get("omitted_on_lccs3_write", [])
    report["output"] = rel(dest)
    report["ok"] = not report.get("schema_errors")
    out(report, 0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
