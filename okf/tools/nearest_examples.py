"""nearest_examples: registry classes whose name and definition are closest to a query.

    python okf/tools/nearest_examples.py --text "Closed forest, canopy > 40 %, evergreen" [--k 5] [--registered-only]
    python okf/tools/nearest_examples.py --system <slug> --code <code>

Deterministic lexical scoring, no embeddings: token overlap on stemmed words
with extra weight on cover-type words (tree, shrub, grass, water, urban, crop,
bare, snow, mangrove ...) and on numeric thresholds. Returns node ids and
paths the decompose skill then opens. Only classes that have a decomposition
in the registry file are returned unless --all.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import OKF_ROOT, out, fail, rel
from rocky import okf

REG = OKF_ROOT / "registry"
STOP = {"the", "and", "or", "of", "with", "in", "to", "a", "an", "is", "are", "by", "for", "on", "as", "at",
        "this", "that", "it", "be", "from", "than", "more", "other", "area", "areas", "land", "cover", "class",
        "type", "types", "mainly", "usually", "may", "can", "which", "these", "those", "its", "their", "not",
        "no", "also", "such", "some", "all", "any", "per", "cent", "percent", "%"}
KEY = {"tree": 3, "trees": 3, "forest": 3, "shrub": 3, "shrubs": 3, "scrub": 3, "bush": 2, "grass": 3, "grassland": 3,
       "herb": 3, "herbaceous": 3, "graminoid": 3, "forb": 2, "crop": 3, "crops": 3, "cropland": 3, "cultivated": 3,
       "irrigated": 3, "rainfed": 3, "plantation": 3, "orchard": 3, "urban": 3, "built": 3, "building": 3,
       "road": 2, "bare": 3, "soil": 2, "rock": 3, "sand": 3, "dune": 3, "water": 3, "lake": 2, "river": 2,
       "sea": 2, "wetland": 3, "marsh": 3, "swamp": 3, "flooded": 3, "mangrove": 4, "snow": 3, "ice": 3,
       "glacier": 3, "evergreen": 3, "deciduous": 3, "broadleaved": 3, "needleleaved": 3, "coniferous": 3,
       "closed": 2, "open": 2, "sparse": 2, "dense": 2, "mosaic": 2, "pasture": 3, "grazing": 2, "mining": 3,
       "aquaculture": 3, "salt": 2, "lichen": 3, "moss": 3, "savanna": 3, "steppe": 3, "peat": 3, "bog": 3}


def tokens(s: str) -> list[str]:
    s = (s or "").lower()
    toks = re.findall(r"[a-záéíóúãõçñü]+|\d+(?:\.\d+)?", s)
    out = []
    for t in toks:
        if t in STOP:
            continue
        if t.isdigit() or re.match(r"\d+\.\d+", t):
            out.append("#" + t)
            continue
        # light stemming
        for suf in ("ings", "ing", "ies", "es", "s", "ed"):
            if len(t) > 4 and t.endswith(suf):
                t = t[: -len(suf)] + ("y" if suf == "ies" else "")
                break
        out.append(t)
    return out


def weight(tok: str) -> float:
    if tok.startswith("#"):
        return 2.0
    return float(KEY.get(tok, 1))


def score(q: list[str], d: list[str]) -> float:
    qs, ds = set(q), set(d)
    inter = qs & ds
    if not inter:
        return 0.0
    num = sum(weight(t) for t in inter)
    den = sum(weight(t) for t in qs) + 0.5 * sum(weight(t) for t in ds - qs)
    return num / den if den else 0.0


def load_corpus(registered_only: bool = True) -> list[dict]:
    corpus = []
    for p in sorted(REG.glob("*/classes/*.md")):
        n = okf.read_node(p)
        if registered_only and not n.front.get("decomposed"):
            continue
        text = f"{n.front.get('name','')} {n.front.get('code','')} {n.body.split('## Decomposition')[0]}"
        corpus.append({"id": n.id, "path": rel(p), "system": n.front.get("system"), "code": n.front.get("code"),
                       "name": n.front.get("name"), "element_refs": n.front.get("element_refs", []),
                       "tokens": tokens(text)})
    return corpus


def nearest(text: str, k: int = 5, registered_only: bool = True, exclude_system: str = "") -> list[dict]:
    q = tokens(text)
    scored = []
    for c in load_corpus(registered_only):
        if exclude_system and c["system"] == exclude_system:
            continue
        s = score(q, c["tokens"])
        if s > 0:
            scored.append((s, c))
    scored.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [{"score": round(s, 3), "id": c["id"], "path": c["path"], "system": c["system"], "code": c["code"],
             "name": c["name"], "element_refs": c["element_refs"]} for s, c in scored[:k]]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="")
    ap.add_argument("--system", default="")
    ap.add_argument("--code", default="")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--all", action="store_true", help="include registry classes without a decomposition")
    ap.add_argument("--exclude-system", default="", help="registry id to leave out (leave-one-out evaluation)")
    a = ap.parse_args()
    text = a.text
    if a.system and a.code:
        from rocky import system as sysmod
        n = sysmod.read_class(a.system, a.code)
        text = f"{n.front.get('name','')} {n.body.split('## Decomposition')[0]}"
    if not text:
        fail("give --text or --system and --code")
    out({"ok": True, "query": text[:200], "results": nearest(text, a.k, not a.all, a.exclude_system)})


if __name__ == "__main__":
    main()
