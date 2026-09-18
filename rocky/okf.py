"""Open Knowledge Format (OKF) nodes: Markdown files with YAML frontmatter and
typed relative links, one file per concept, traversed deterministically.

This module is the only place that knows the node grammar. It writes nodes,
parses them, builds ``_index.json`` and checks the folder: every link
resolves, every relation is in the ontology, every node has the required
fields and stays under the size cap. ``okf_build --check`` runs it twice and
fails if the second run would change any byte.

Frontmatter fields, common to every node::

    id, kind, title, schema: okf/0.1
    links: [{rel, id, path}]           typed edges; path is relative to this file
    sources: [...]                     documents or files this node was built from
    built_from: <sha256 prefix>        input digest, for regeneration checks

Kinds and relations are declared in ``KINDS`` and ``RELATIONS`` and rendered
into ``ONTOLOGY.md`` so agents read the same vocabulary the build enforces.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import OKF_ROOT

SCHEMA = "okf/0.1"
MAX_NODE_CHARS = 12000

KINDS: dict[str, str] = {
    "start": "the single entry point; links to everything an agent may need",
    "ontology": "the node kinds and relations, rendered from code",
    "vocab_element": "one LCML atomic element type (LChS BlockReference), from the schema",
    "vocab_characteristic": "one LCML characteristic type (LChS CharacteristicReference), from the schema",
    "vocab_enum": "one enumeration with its documented values",
    "vocab_record": "one flat record type of the LChS file format",
    "standard": "a reviewed digest of an ISO 19144 rule or concept",
    "registry_index": "the FAO LCLR legend list",
    "system": "one classification system: publisher, scope, sources, framing summary",
    "class": "one class of a system: definition, element rows, rationale, open questions",
    "framing": "an institution, instrument or purpose that shapes class names or thresholds",
    "candidate": "a classification system found but not yet ingested",
    "attention": "the ranked list of classes stakeholders should look at, for one system",
    "comparison": "an equivalence matrix between two described systems",
    "eval": "scores from a leave-one-out or regression run",
    "guide": "instructions for agents or people (AGENTS.md, skill pages)",
}

# rel -> (from kinds, to kinds, meaning)
RELATIONS: dict[str, tuple[tuple[str, ...], tuple[str, ...], str]] = {
    "see": (("*",), ("*",), "navigation: the target is worth opening next"),
    "has_class": (("system",), ("class",), "the system defines this class"),
    "in_system": (("class", "framing", "attention"), ("system",), "belongs to this system"),
    "uses_type": (("class",), ("vocab_element", "vocab_characteristic"), "the class description uses this LCML type"),
    "allows": (("vocab_element", "vocab_characteristic"), ("vocab_enum",), "a property of this type takes values from this enum"),
    "specialises": (("vocab_element",), ("vocab_element",), "subtype of, per the schema documentation"),
    "named_by": (("class",), ("framing",), "the class name comes from this institution or instrument"),
    "motivated_by": (("class",), ("framing",), "a threshold or split in this class exists because of this instrument"),
    "evidenced_by": (("class", "framing"), ("system",), "the evidence span is in this system's source documents"),
    "nearest_example": (("class",), ("class",), "a registered class whose definition is closest; used as a worked example"),
    "same_physical_as": (("class",), ("class",), "element rows are equivalent (comparison)"),
    "overlaps": (("class",), ("class",), "element rows intersect but differ (comparison)"),
    "disjoint_from": (("class",), ("class",), "element rows are disjoint (comparison)"),
    "about": (("attention", "eval"), ("class", "system"), "the item concerns this node"),
    "hinges_on": (("attention",), ("framing",), "the decision belongs to whoever owns this instrument"),
    "compares": (("comparison",), ("system",), "one of the two systems compared"),
    "in_registry": (("system",), ("registry_index",), "this system is a registered FAO legend"),
    "supersedes": (("system",), ("system",), "a newer version of the same system"),
}


@dataclass
class Node:
    path: Path
    front: dict
    body: str

    @property
    def id(self) -> str:
        return self.front.get("id", "")

    @property
    def kind(self) -> str:
        return self.front.get("kind", "")


_FM = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)


def parse(text: str) -> tuple[dict, str]:
    m = _FM.match(text)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)


def read_node(path: Path) -> Node:
    fm, body = parse(Path(path).read_text(encoding="utf-8"))
    return Node(Path(path), fm, body)


def render(front: dict, body: str) -> str:
    fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True, width=1000).rstrip("\n")
    return f"---\n{fm}\n---\n\n{body.rstrip()}\n"


def write_node(path: Path, front: dict, body: str, root: Path = OKF_ROOT) -> Path:
    path = Path(path)
    front = dict(front)
    front.setdefault("schema", SCHEMA)
    text = render(front, body)
    if len(text) > MAX_NODE_CHARS:
        raise ValueError(f"{path}: node is {len(text)} chars, cap is {MAX_NODE_CHARS}")
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != text:
        path.write_text(text, encoding="utf-8", newline="\n")
    return path


def link(rel: str, target_id: str, from_path: Path, to_path: Path) -> dict:
    rel_path = os.path.relpath(Path(to_path), Path(from_path).parent).replace(os.sep, "/")
    return {"rel": rel, "id": target_id, "path": rel_path}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ index
NON_NODE_DIRS = {"package"}   # deliverable folders hold plain files (README.md, SUBMISSION.md), not nodes


def iter_nodes(root: Path = OKF_ROOT):
    for p in sorted(Path(root).rglob("*.md")):
        parts = p.relative_to(root).parts
        if any(part.startswith("_") or part in NON_NODE_DIRS for part in parts):
            continue
        yield p


def build_index(root: Path = OKF_ROOT) -> dict:
    index = {}
    for p in iter_nodes(root):
        text = p.read_text(encoding="utf-8")
        fm, _ = parse(text)
        if not fm.get("id"):
            continue
        index[fm["id"]] = {
            "path": p.relative_to(root).as_posix(),
            "kind": fm.get("kind", ""),
            "title": fm.get("title", ""),
            "sha256": sha(text),
        }
    return dict(sorted(index.items()))


def write_index(root: Path = OKF_ROOT) -> Path:
    idx = build_index(root)
    out = Path(root) / "_index.json"
    text = json.dumps({"schema": SCHEMA, "nodes": idx}, indent=1, ensure_ascii=False) + "\n"
    if not out.exists() or out.read_text(encoding="utf-8") != text:
        out.write_text(text, encoding="utf-8", newline="\n")
    return out


def check(root: Path = OKF_ROOT) -> list[str]:
    """Problems with the folder: missing fields, bad kinds/relations, dangling links, oversize."""
    root = Path(root)
    problems: list[str] = []
    ids: dict[str, Path] = {}
    nodes: list[Node] = []
    for p in iter_nodes(root):
        text = p.read_text(encoding="utf-8")
        if len(text) > MAX_NODE_CHARS:
            problems.append(f"{p.relative_to(root)}: {len(text)} chars > cap {MAX_NODE_CHARS}")
        fm, body = parse(text)
        rel = p.relative_to(root).as_posix()
        if not fm:
            problems.append(f"{rel}: no frontmatter")
            continue
        for k in ("id", "kind", "title", "schema"):
            if k not in fm:
                problems.append(f"{rel}: missing '{k}'")
        if fm.get("schema") != SCHEMA:
            problems.append(f"{rel}: schema {fm.get('schema')!r} != {SCHEMA}")
        if fm.get("kind") not in KINDS:
            problems.append(f"{rel}: unknown kind {fm.get('kind')!r}")
        if fm.get("id") in ids:
            problems.append(f"{rel}: duplicate id {fm.get('id')!r} (also {ids[fm['id']].relative_to(root)})")
        ids[fm.get("id", rel)] = p
        nodes.append(Node(p, fm, body))
    for n in nodes:
        rel = n.path.relative_to(root).as_posix()
        for ln in n.front.get("links") or []:
            r = ln.get("rel")
            if r not in RELATIONS:
                problems.append(f"{rel}: unknown relation {r!r}")
            target = (n.path.parent / ln.get("path", "")).resolve()
            if not target.exists():
                problems.append(f"{rel}: link {r} -> {ln.get('path')} does not exist")
                continue
            tid = ln.get("id")
            if tid and tid in ids and ids[tid].resolve() != target:
                problems.append(f"{rel}: link id {tid!r} does not match file {ln.get('path')}")
            if r in RELATIONS:
                frm, to, _ = RELATIONS[r]
                if "*" not in frm and n.kind not in frm:
                    problems.append(f"{rel}: relation {r} not allowed from kind {n.kind}")
                if tid in ids and "*" not in to:
                    tk = parse(ids[tid].read_text(encoding="utf-8"))[0].get("kind")
                    if tk not in to:
                        problems.append(f"{rel}: relation {r} not allowed to kind {tk}")
    return problems


def ontology_markdown() -> str:
    lines = ["# Ontology", "",
             "Node kinds and typed relations of this knowledge base. The build rejects any other kind or relation.",
             "", "## Kinds", "", "| kind | meaning |", "|---|---|"]
    for k, v in KINDS.items():
        lines.append(f"| `{k}` | {v} |")
    lines += ["", "## Relations", "", "| relation | from | to | meaning |", "|---|---|---|---|"]
    for r, (frm, to, meaning) in RELATIONS.items():
        lines.append(f"| `{r}` | {', '.join(frm)} | {', '.join(to)} | {meaning} |")
    lines += ["", "## Node grammar", "",
              "Every node is Markdown with a YAML frontmatter block holding `id`, `kind`, `title`, `schema`, "
              "optional `links` (list of `{rel, id, path}` with `path` relative to the node), `sources` and `built_from`. "
              f"Nodes stay under {MAX_NODE_CHARS} characters so an agent reads whole nodes. "
              "Links are the only retrieval mechanism: start at `START.md`, follow the links you need, stop.", ""]
    return "\n".join(lines)
