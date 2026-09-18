# Rocky

Rocky turns written land cover classification systems into ISO 19144-2 LCML element descriptions,
writes them in FAO's LChS and LCCS3 formats, and produces the ranked list of classes stakeholders
must decide on. It is an Open Knowledge Format folder (`okf/`) run by agents through skills and
deterministic tools, plus a Python library (`rocky/`).

- Design and build plan: [docs/PLAN.md](docs/PLAN.md)
- Entry point for agents and people: [okf/START.md](okf/START.md), then [okf/agents/AGENTS.md](okf/agents/AGENTS.md)

## Folder structure

```
rocky/                       Python library: deterministic, no model calls
  xsd_vocab.py, lchs_vocab.py    parse the two FAO schemas into the LCML vocabulary
  schemas.py                     schema loading with the in-memory patches FAO's LChS XSD needs; validators
  table.py                       the long-form row model every projection is derived from; csv in/out; diff
  lchs.py, lccs.py               readers and writers for .LChS (ISO 19144-2:2023) and .lccs (LCCS v3)
  crosswalk.py                   type names LCCS3 <-> LChS, presence values, BlockID codes
  lchs_to_lccs3.py, lccs3_to_lchs.py   property-level mapping when writing across formats
  validate.py                    structural check of a table against the vocabulary
  readers.py                     JSON, CSV, XLSX, PDF, DOCX, HTML, text -> raw blocks and class records
  registry.py                    fetch of the FAO Land Cover Legend Registry
  okf.py                         OKF node grammar: frontmatter, links, index, folder check, ontology
  system.py                      read/write of systems/<slug>/ (SYSTEM.md, class nodes, elements.csv)
  apply.py                       turns a skill's JSON result into nodes (ingest, decompose, framing, critique)
  critics.py                     rule-based ambiguity finders and ranking
  equivalence.py                 mechanical comparison of two systems
  scoring.py                     leave-one-out scores against registry rows

okf/                         the knowledge base (Markdown nodes with YAML frontmatter, typed links)
  START.md                       where every agent starts
  ONTOLOGY.md                    node kinds and relations, generated from rocky/okf.py
  _index.json                    id -> path, kind, sha256 (generated)
  vocab/                         generated from the schemas: elements/, characteristics/, records/, enums/, *.json
  standards/                     two reviewed pages: LCML rules, land-use activities that masquerade as cover
  registry/                      FAO registry as worked examples: INDEX.md, L<n>/SYSTEM.md, classes/, elements.csv
    _raw/                        verbatim downloaded files and manifest (not indexed)
    _eval/, EVAL.md              leave-one-out scores (written by eval_registry.py)
  systems/<slug>/                one ingested classification system
    SYSTEM.md                    publisher, scope, framing summary, run history, class list
    classes/<code>.md            definition, decomposition table, rationale, evidence, open questions
    framing/<instrument>.md      laws, programmes and conventions that shape the names
    elements.csv                 the table projection (machine form of every class)
    <slug>.LChS, <slug>.lccs     the FAO files
    package/                     registry submission package (not indexed as nodes)
    _ingest/, _runs/             source blocks and prompt/result bundles (not indexed)
  attention/<slug>.md + .json    ranked list of classes stakeholders should look at
  comparisons/<a>__<b>.md        equivalence matrix between two systems
  candidates/                    systems found by discover-systems but not yet ingested
  skills/<name>/SKILL.md         instructions for each agent step
  agents/
    AGENTS.md                    the contract any agent platform follows
    runner.py                    reference driver: prompt | run | apply | critique
    manifests/<skill>.json       what a skill reads, its output JSON schema, its apply step
  tools/                         CLIs, JSON in/out: build_vocab, build_registry, ingest, nearest_examples,
                                 registry_search, convert, equivalence, submission_check, eval_registry, okf_build

schemas/                     lccs3.xsd (FAO LCCS v3), lchs.xsd (FAO Land Characterization System, verbatim from the registry)
tests/                       pytest: round trips over every registry file, readers, pipeline regression on MapBiomas
docs/PLAN.md                 the approved design and build plan

mapbiomas_doc/               source material: ten MapBiomas legends and their hand-built harmonisation (the regression ground truth)
cd6226en_doc/, cd6231en_doc/, cd6247en_doc/   graphify knowledge graphs of ISO 19144-1, 19144-3 and 19144-2:2023
g4g2026_ideathon.xsd, .lccs  the LCCS3 schema and a minimal sample legend from the ideathon
```

## Quick start

```bash
python -m pip install lxml pyyaml requests pandas openpyxl pdfplumber beautifulsoup4 pytest anthropic
python okf/tools/build_vocab.py                      # vocabulary from the FAO schemas
python okf/tools/build_registry.py --refresh         # FAO Land Cover Legend Registry as worked examples
python okf/tools/ingest.py <legend file> --system my_system --name "My system"
python okf/agents/runner.py prompt decompose-class --system my_system --code <code>   # or `run` with an API key
python okf/agents/runner.py critique --system my_system
python okf/tools/convert.py okf/systems/my_system/elements.csv --to lchs --out okf/systems/my_system/my_system.LChS
python okf/tools/okf_build.py --check
python -m pytest tests -q
```

Set `ROCKY_OKF_ROOT` to run against another knowledge-base folder.
