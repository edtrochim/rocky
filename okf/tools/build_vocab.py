"""build_vocab: generate okf/vocab/ from the two FAO schemas.

    python okf/tools/build_vocab.py

One node per LChS element type, characteristic type, record type and
enumeration, with the schema's own documentation, the properties each type
allows (with enum values and range flags), and the LCCS3 type names that map
to it. Also writes vocab/lchs_schema.json and vocab/lccs3_schema.json for
tools, and vocab/INDEX.md for agents.
"""

from __future__ import annotations

import json

from _common import OKF_ROOT, REPO_ROOT, out
from rocky import lchs_vocab, xsd_vocab, crosswalk, okf
from rocky.schemas import LCCS3_XSD, LCHS_XSD

VOCAB = OKF_ROOT / "vocab"


def _links_for_type(t: lchs_vocab.LchsType, v: lchs_vocab.LchsVocab, here) -> list[dict]:
    links = []
    seen = set()
    for p in t.props:
        if p.is_enum and p.type in v.enums and p.type not in seen:
            seen.add(p.type)
            links.append(okf.link("allows", f"enum:{p.type}", here, VOCAB / "enums" / f"{p.type}.md"))
    return links


def _prop_table(t: lchs_vocab.LchsType, v: lchs_vocab.LchsVocab) -> str:
    lines = ["| property | type | values / range | required | meaning |", "|---|---|---|---|---|"]
    for p in t.props:
        if p.is_enum:
            vals = ", ".join(f"`{x}`" for x in v.enum_values(p.type)[:12])
            if len(v.enum_values(p.type)) > 12:
                vals += f" … ({len(v.enum_values(p.type))} values, see enum)"
        elif p.is_range:
            vals = "min, max"
        else:
            vals = ""
        lines.append(f"| `{p.name}` | {p.type} | {vals} | {'yes' if p.min_occurs else ''} | {p.doc} |")
    return "\n".join(lines)


def main() -> None:
    v = lchs_vocab.load()
    x = xsd_vocab.load(LCCS3_XSD)
    written = []

    lccs3_for_ref: dict[str, list[str]] = {}
    for k, (ref, _n) in crosswalk.ELEMENT_LCCS3_TO_LCHS.items():
        lccs3_for_ref.setdefault(ref, []).append(k)
    for k, (ref, _n) in crosswalk.CHAR_LCCS3_TO_LCHS.items():
        lccs3_for_ref.setdefault(ref, []).append(k)

    # elements and characteristics
    for kind, items, folder in (("vocab_element", v.elements(), "elements"),
                                ("vocab_characteristic", v.characteristics(), "characteristics")):
        for ref, t in items.items():
            path = VOCAB / folder / f"{ref}.md"
            front = {
                "id": f"{folder[:-1] if folder != 'characteristics' else 'characteristic'}:{ref}",
                "kind": kind, "title": ref,
                "lchs_type": t.name, "lccs3_types": lccs3_for_ref.get(ref, []),
                "properties": [p.name for p in t.props],
                "links": _links_for_type(t, v, path),
                "sources": [LCHS_XSD.name],
            }
            body = (f"# {ref}\n\n{t.doc or '(no documentation in the schema)'}\n\n"
                    f"LChS reference name `{ref}` (schema type `{t.name}`). "
                    + (f"LCCS3 `xsi:type`: {', '.join('`' + s + '`' for s in lccs3_for_ref[ref])}.\n\n"
                       if ref in lccs3_for_ref else "No LCCS3 equivalent.\n\n")
                    + "## Properties\n\n" + _prop_table(t, v) + "\n\n"
                    + "Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.\n")
            okf.write_node(path, front, body)
            written.append(path)

    # records
    for name, t in v.records().items():
        path = VOCAB / "records" / f"{name}.md"
        front = {"id": f"record:{name}", "kind": "vocab_record", "title": name, "sources": [LCHS_XSD.name],
                 "fields": [p.name for p in t.props]}
        body = f"# {name}\n\n{t.doc or ''}\n\n## Fields\n\n" + _prop_table(t, v) + "\n"
        okf.write_node(path, front, body)
        written.append(path)

    # enums
    for name, e in v.enums.items():
        path = VOCAB / "enums" / f"{name}.md"
        front = {"id": f"enum:{name}", "kind": "vocab_enum", "title": name, "sources": [LCHS_XSD.name],
                 "values": list(e.values)}
        rows = "\n".join(f"| `{code}` | {doc} |" for code, doc in e.values.items())
        body = (f"# {name}\n\n{e.doc}\n\nFAO's files write the label column; the schema declares the code column. "
                f"Both are accepted.\n\n| code | label |\n|---|---|\n{rows}\n")
        okf.write_node(path, front, body)
        written.append(path)

    # machine-readable copies
    (VOCAB / "lchs_schema.json").write_text(json.dumps(v.to_dict(), indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    (VOCAB / "lccs3_schema.json").write_text(json.dumps(x.to_dict(), indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    # index pages: one per folder (kept small), one top page
    def list_page(folder: str, kind_id: str, items: dict, title: str, intro: str) -> Path:
        p = VOCAB / folder / "INDEX.md"
        lines = "\n".join(f"- [{ref}](./{ref}.md): {t.doc}" for ref, t in items.items())
        links = [okf.link("see", f"{kind_id}:{ref}", p, VOCAB / folder / f"{ref}.md") for ref in items]
        okf.write_node(p, {"id": f"vocab-{folder}", "kind": "guide", "title": title,
                           "sources": [LCHS_XSD.name], "links": links},
                       f"# {title}\n\n{intro}\n\n{lines}\n")
        return p

    p_el = list_page("elements", "element", v.elements(), "LCML elements",
                     "The atomic element types a stratum may contain, from the LChS schema. "
                     "Prefer the most specific type the definition supports (LC_Tree over LC_WoodyGrowthForm).")
    p_ch = list_page("characteristics", "characteristic", v.characteristics(), "LCML characteristics",
                     "Characteristics an element may carry (vegetation artificiality, water salinity, crop parameters ...).")
    written += [p_el, p_ch]

    idx = VOCAB / "INDEX.md"
    links = [okf.link("see", "vocab-elements", idx, p_el), okf.link("see", "vocab-characteristics", idx, p_ch)]
    front = {"id": "vocab", "kind": "guide", "title": "LCML vocabulary",
             "counts": {"elements": len(v.elements()), "characteristics": len(v.characteristics()),
                        "records": len(v.records()), "enums": len(v.enums)},
             "sources": [LCHS_XSD.name, LCCS3_XSD.name], "links": links}
    body = ("# LCML vocabulary\n\nGenerated from FAO's LChS schema (ISO 19144-2:2023) with LCCS3 names cross-walked. "
            "Do not edit by hand; rerun `okf/tools/build_vocab.py`.\n\n"
            "A class is one or more **horizontal patterns**, each a stack of **strata**, each holding **elements**, "
            "each element carrying properties and optional **characteristics**.\n\n"
            f"- [Elements]({p_el.relative_to(VOCAB).as_posix()}): {len(v.elements())} types\n"
            f"- [Characteristics]({p_ch.relative_to(VOCAB).as_posix()}): {len(v.characteristics())} types\n"
            f"- Records: the flat LChS file records, {', '.join(f'[{n}](records/{n}.md)' for n in v.records())}\n"
            f"- Enumerations: {len(v.enums)} under `enums/`, one per file, linked from the type that uses them\n"
            "- `lchs_schema.json`, `lccs3_schema.json`: the same vocabulary for tools\n")
    okf.write_node(idx, front, body)
    written.append(idx)
    out({"ok": True, "written": len(written), "elements": len(v.elements()),
         "characteristics": len(v.characteristics()), "enums": len(v.enums)})


if __name__ == "__main__":
    main()
