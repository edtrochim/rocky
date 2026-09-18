"""eval_registry: leave-one-legend-out evaluation of decompose-class against the FAO registry.

    python okf/tools/eval_registry.py --legend L16 --prepare          # ingest the legend as titles+definitions, write prompts
    python okf/tools/eval_registry.py --legend L16 --score            # score every result.json found against the registry rows
    python okf/tools/eval_registry.py --legend L16 --self-check       # score the registry rows against themselves (must be 1.0)

``--prepare`` creates ``systems/eval_<L#>/`` from the registry's definition
text only (no rows), with nearest-example retrieval excluding that legend,
and writes one prompt bundle per class. A runtime produces the result.json
files (``runner.py run`` with an API key, or any agent from the prompt). ``--score``
applies each result, scores it with ``rocky.scoring`` and writes
``registry/EVAL.md`` plus ``registry/_eval/<L#>.json``.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from _common import OKF_ROOT, REPO_ROOT, out, fail, rel
from rocky import okf, system, scoring, apply
from rocky.table import Table

REG = OKF_ROOT / "registry"
RUNNER = REPO_ROOT / "okf" / "agents" / "runner.py"


def registry_classes(code: str) -> list[dict]:
    out_ = []
    for p in sorted((REG / code / "classes").glob("*.md")):
        n = okf.read_node(p)
        f = n.front
        if not f.get("decomposed"):
            continue
        definition = n.body.split("## Definition (verbatim, FAO LCLR)", 1)[1].split("\n## ", 1)[0].strip() if "## Definition (verbatim, FAO LCLR)" in n.body else ""
        out_.append({"code": f.get("code", ""), "name": f.get("name", ""), "definition": "" if definition.startswith("_none") else definition,
                     "file_class_id": f.get("file_class_id"), "node": p})
    return out_


def prepare(code: str) -> dict:
    slug = f"eval_{code}"
    sysn = okf.read_node(REG / code / "SYSTEM.md").front
    classes = registry_classes(code)
    meta = {"name": f"EVAL {sysn.get('title')}", "publisher": sysn.get("publisher", ""), "jurisdiction": sysn.get("country", ""),
            "sources": [f"registry:{code} (definitions only; rows withheld)"], "mode": "propose"}
    cls_nodes = []
    t = Table()
    for c in classes:
        cid = c["code"] or system.slugify(c["name"])
        cls = {"class_id": cid, "code": c["code"], "name": c["name"], "definition": c["definition"], "status": "titles_only",
               "source_span": f"registry:{code}"}
        cls_nodes.append(cls)
        t.rows.extend(system.rows_from_proposal(slug, cid, c["code"], c["name"], {"definition": c["definition"], "patterns": []}))
    system.write_system(slug, meta, cls_nodes)
    for cls in cls_nodes:
        system.write_class(slug, cls, None)
    system.save_table(slug, t)
    prompts = 0
    errors = []
    for cls in cls_nodes:
        r = subprocess.run([sys.executable, str(RUNNER), "prompt", "decompose-class", "--system", slug, "--code", cls["code"] or cls["name"],
                            "--exclude-system", f"registry:{code}"], capture_output=True, text=True, cwd=REPO_ROOT)
        if r.returncode == 0:
            prompts += 1
        elif len(errors) < 3:
            errors.append((r.stderr or r.stdout)[-600:])
    return {"system": slug, "classes": len(cls_nodes), "prompts": prompts, "errors": errors}


def score(code: str) -> dict:
    slug = f"eval_{code}"
    ref = Table.from_csv(REG / code / "elements.csv")
    classes = registry_classes(code)
    results = []
    for c in classes:
        cc = c["code"] or system.slugify(c["name"])
        rp = system.system_dir(slug) / "_runs" / f"decompose-class-{system.slugify(cc)}" / "result.json"
        if not rp.exists():
            continue
        subprocess.run([sys.executable, str(RUNNER), "apply", "decompose-class", "--system", slug, "--code", cc, "--result", str(rp)],
                       capture_output=True, text=True, cwd=REPO_ROOT)
        prop = system.load_table(slug)
        s = scoring.score_class(ref, c["file_class_id"], prop, cc)
        s["code"] = c["code"]
        s["name"] = c["name"]
        results.append(s)
    agg = scoring.aggregate(results)
    d = REG / "_eval"
    d.mkdir(exist_ok=True)
    (d / f"{code}.json").write_text(json.dumps({"legend": code, "aggregate": agg, "classes": results}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    write_eval_page()
    return {"legend": code, "scored": len(results), "aggregate": agg}


def self_check(code: str) -> dict:
    ref = Table.from_csv(REG / code / "elements.csv")
    results = []
    for c in registry_classes(code):
        s = scoring.score_class(ref, c["file_class_id"], ref, c["file_class_id"])
        results.append(s)
    return {"legend": code, "aggregate": scoring.aggregate(results)}


def write_eval_page() -> None:
    d = REG / "_eval"
    rows = []
    links = []
    for p in sorted(d.glob("*.json")):
        j = json.loads(p.read_text(encoding="utf-8"))
        a = j["aggregate"]
        rows.append(f"| [{j['legend']}]({j['legend']}/SYSTEM.md) | {a.get('classes',0)} | {a.get('element_recall')} | {a.get('element_precision')} | "
                    f"{a.get('family_recall')} | {a.get('presence_agreement')} | {a.get('range_overlap')} | {a.get('stratum_count_ok')} |")
        links.append(okf.link("about", f"registry:{j['legend']}", REG / "EVAL.md", REG / j["legend"] / "SYSTEM.md"))
    front = {"id": "registry-eval", "kind": "eval", "title": "Leave-one-out evaluation against the registry",
             "legends": len(rows), "links": links}
    body = ("# Leave-one-out evaluation against the registry\n\nFor each legend, `decompose-class` saw only the definition text "
            "(and registry examples from other legends). Scores compare the proposal with FAO's own rows.\n\n"
            "| legend | classes | element recall | element precision | family recall | presence agreement | range overlap | strata count ok |\n"
            "|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    okf.write_node(REG / "EVAL.md", front, body)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--legend", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prepare", action="store_true")
    g.add_argument("--score", action="store_true")
    g.add_argument("--self-check", action="store_true")
    a = ap.parse_args()
    if not (REG / a.legend).exists():
        fail(f"no registry legend {a.legend}")
    if a.prepare:
        out({"ok": True, **prepare(a.legend)})
    if a.score:
        out({"ok": True, **score(a.legend)})
    out({"ok": True, **self_check(a.legend)})


if __name__ == "__main__":
    main()
