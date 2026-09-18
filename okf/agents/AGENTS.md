---
id: agents
kind: guide
title: How agents run this
schema: okf/0.1
links:
- rel: see
  id: start
  path: ../START.md
- rel: see
  id: vocab
  path: ../vocab/INDEX.md
- rel: see
  id: registry
  path: ../registry/INDEX.md
---

# How agents run this

This knowledge base is run by agents on any platform: Claude Code through `skills/*/SKILL.md`, the reference
driver `agents/runner.py`, or any framework that can read Markdown and call a command line. The contract is
the same everywhere.

## The contract

1. Start at [START.md](../START.md). Open only the nodes a step needs.
2. Skills reason and write nodes. Tools are deterministic and never call a model. A skill calls tools, a
   tool never calls a skill.
3. Write only under `systems/<slug>/`, `attention/`, `comparisons/` and `candidates/`. Never edit `vocab/`,
   `registry/`, `standards/`, `ONTOLOGY.md` or `START.md`.
4. Every claim about a class cites evidence: the source span for a proposed row, or the registry class it
   was modelled on.
5. Finish a step by running `okf_build.py --check`. A step that leaves the folder invalid is not finished.

## Tools (JSON in, JSON out, non-zero exit on failure)

| tool | purpose |
|---|---|
| `python okf/tools/build_vocab.py` | regenerate `vocab/` from the two FAO schemas |
| `python okf/tools/build_registry.py [--refresh]` | fetch the FAO registry and regenerate `registry/` |
| `python okf/tools/ingest.py <file> --system <slug> [--select <key>] [--name ..]` | create `systems/<slug>/` from a table, JSON, document or FAO file; tables need no model |
| `python okf/tools/nearest_examples.py --text ".." \| --system <slug> --code <code>` | registry classes closest to a definition (lexical, deterministic) |
| `python okf/tools/registry_search.py --q <term>` | find registered legends by country, publisher, year or word |
| `python okf/tools/convert.py <file> --to csv\|lchs\|lccs3 --out <path>` | move a legend between the table and the FAO formats, with validation |
| `python okf/tools/convert.py <file> --validate` | vocabulary and structure findings for a legend or table |
| `python okf/tools/equivalence.py --a <slug\|registry:L#> --b <..>` | mechanical comparison of two systems into `comparisons/` |
| `python okf/tools/submission_check.py --system <slug> [--build]` | build and verify the registry-ready package |
| `python okf/tools/okf_build.py [--check]` | regenerate `ONTOLOGY.md` and `_index.json`; `--check` fails on any invalid node or pending change |
| `python okf/agents/runner.py prompt\|run\|apply <skill> --system <slug> [--code ..]` | build a skill's prompt bundle, run it through the Anthropic API, or apply a result JSON produced elsewhere |
| `python okf/agents/runner.py critique --system <slug> [--compare <slug> ..]` | rule critics only, no model |

Library code lives in `rocky/`; `rocky.table` is the row model every projection uses.
`ROCKY_OKF_ROOT` points every tool at another knowledge-base folder (tests use a temporary one).

## Running a skill without the API

`runner.py prompt <skill> ...` writes `systems/<slug>/_runs/<skill>[-<code>]/prompt.md` and `schema.json`.
Any agent that can read a file and write JSON matching the schema can produce `result.json`; then
`runner.py apply ... --result result.json` writes the nodes. This is how a Claude Code session, a person,
or another platform runs a skill; `runner.py run` does the same through the Anthropic API.

## Skill order for one classification system

| step | skill | reads | writes |
|---|---|---|---|
| 0 | `discover-systems` (on request) | registry index, the web | `candidates/<slug>.md` |
| 1 | `ingest-classification` | the source document | `systems/<slug>/SYSTEM.md`, `classes/<code>.md` |
| 2 | `extract-framing` | SYSTEM.md, class nodes, source | `systems/<slug>/framing/<instrument>.md`, links on class nodes |
| 3 | `decompose-class` (per class) | class node, siblings, `vocab/`, nearest registry classes | rows on the class node and `elements.csv` |
| 4 | `critique-system` | all class and framing nodes | `attention/<slug>.md` |
| 5 | emit (tool only) | `elements.csv` | `<slug>.LChS`, `<slug>.lccs` |
| 6 | `compare-systems` (with `--compare`) | two systems' `elements.csv` | `comparisons/<a>__<b>.md` |
| 7 | `prepare-submission` | the system folder | `systems/<slug>/package/` |
| 8 | `submit-to-registry` (with `--submit`) | the package | a drafted, unsent message |

Modes: `propose` when the input is a document or table; `refine` when the input is already `.LChS` or
`.lccs`, in which case steps 3 and 4 critique the existing rows and every change is a diff.

## What a class node looks like when a step is done

Frontmatter: `id`, `kind: class`, `system`, `code`, `name`, `status` (`titles_only` | `proposed` | `accepted` |
`disputed` | `registered`), `element_refs`, `confidence`, `links` (`in_system`, `uses_type`, `named_by`,
`motivated_by`, `nearest_example`). Body: the verbatim definition, the decomposition table, rationale,
nearest registry examples and how this class differs from each, open questions.
