# Rocky: land cover classification systems → LCML atomic elements, as an OKF knowledge base run by agents

## Context

Every institution publishes land cover classes under its own framing. MapBiomas Brazil calls code 4 "Savanna Formation" because the Cerrado is a political and legal category in Brazil; Argentina calls the same code "Open forests" because its forest law (Ley 26.331) defines forest by canopy, not biome. Chile splits "Primary" from "Secondary" forest because its native forest law pays for one and not the other. The names are outputs of regulation, mandate and history, not of vegetation. A class definition is therefore a **knowledge graph**, not a label: it has a physical part (what is on the ground) and a framing part (who defined it, under which rule, for which purpose), and the two are linked.

ISO 19144-2 Land Cover Meta Language (LCML) gives the physical part a fixed vocabulary of **atomic elements**. FAO serialises that vocabulary in two formats, both present in FAO's Land Cover Legend Registry (LCLR). The usual input to this work is the opposite of either: a list of class titles, sometimes with a paragraph of definition. The gap between "Open forests" and a stratum of LC_Trees with cover 10-40 % plus optional LC_Shrubs is the work.

The unit of work is a **class knowledge graph** whose nodes are the FAO schema's own types. One graph, three projections: an editable table, Markdown nodes in an Open Knowledge Format (OKF) folder, and FAO XML. Framing (institution, instrument, purpose, source span) is part of the graph, linked to the physical elements it motivates, so a reviewer sees *why* two institutions disagree, not only that they do. Agents run **skills** that read the OKF and call deterministic **tools**; no run depends on a database, an embedding index, or one agent platform.

## Target formats

### LCHS (primary): FAO's serialisation of ISO 19144-2:2023

Used by the newest registry legends (`.LChS`). Flat XML: sibling records under `objects`, joined by ids.

```
LC_Legend (attrs: legend_name, legend_description, legend_author)
└─ objects
   ├─ LC_Class                  legend_id, class_id, class_name, class_description, class_map_code, class_color_code
   ├─ LC_ClassCharacteristics   geographical_aspects, topographical_aspects (altitude, slope, exposition)
   ├─ LC_HorizontalPatterns     horizontal_pattern_id, class ref, name, cover, occurrence, type
   ├─ LC_Strata                 HPID, stratumID, presenceType, portioning, onTop / onTopType
   ├─ LC_Properties             StratumID, BlockID, BlockReference (= element type), elementPresenceType,
   │                            height, depth, density, woodyLeafPhenology + evergreen/deciduousPercentage,
   │                            woodyLeafType + broad/needle/aphyllousPercentage, herbaceousLeafPhenology,
   │                            elementHorizontalSpreading, lifeFormSpecialization, temporalType,
   │                            dynamics, position, periodVariationType, persistencePeriod ...
   └─ LC_Characteristics        CharacteristicID, CharacteristicReference, vegetationArtificiality, waterSalinity,
                                artificiality, irrigationType, fieldSize, yield, treePlantation, ploughType ...
```

No schema is published for LCHS. It is reconstructed from the registry's `.LChS` files plus the ISO 19144-2:2023 attribute list in `cd6247en_doc/graphify-out/graph.json`, recorded as `okf/vocab/lchs_schema.json` with provenance. Validation is structural: every id resolves, every BlockReference is a known element, every attribute is in the reconstructed list.

### LCCS3 (secondary): FAO LCCS v3 `.lccs`

Used by the FAO desktop tool and most registry legends. Nested XML with `xsi:type`; the schema is `g4g2026_ideathon.xsd` in this folder, sample legend `g4g2026_ideathon.lccs`.

```
LC_Legend
└─ LC_LandCoverClass            name, description, map_code
   ├─ LC_Characteristic         class-level: LC_Climate, LC_LandForm, LC_GeographicalAspects, LC_TopographicalAspects ...
   └─ LC_HorizontalPattern      type, cover %, occurance %
      └─ LC_Stratum             presence_type {Mandatory, Optional}, ontop
         └─ LC_LandCoverElement xsi:type = one concrete leaf; presence_type, cover %, portioning %, temporal relationship
            └─ LC_Characteristic element-level, enums and min/max ranges
```

Concrete leaf elements (the smallest units a class reduces to):

| group | leaf types |
|---|---|
| vegetation, woody | LC_Trees, LC_Shrubs (height, depth, leaf phenology {Evergreen, Deciduous}, leaf type {Needleleaved, Broadleaved, Aphillous}) |
| vegetation, herbaceous | LC_Graminae, LC_Forbs (height, phenology {Annual, Biennial, Perennial}) |
| vegetation, other | LC_Lichen, LC_Mosses, LC_Algae |
| artificial, linear | LC_Road, LC_Railway, LC_CommunicationsAndOther |
| artificial, non-linear | LC_Building, LC_OtherConstruction, LC_OtherArtificialSurface, LC_DumpSite, LC_Deposit, LC_Extraction |
| natural surface | LC_BareRocks, LC_BareRocksAndCoarseFragments, LC_HardPans, LC_BareSoil, LC_CoarseMineralFragments, LC_LooseAndShiftingSand, LC_Dune, LC_InorganicDeposits, LC_OrganicDeposits |
| water and associated | LC_WaterBody (dynamics, position, salinity, artificiality, periodic variation, aquaculture), LC_Snow, LC_TerrestrialIce, LC_FloatingIce, LC_Permafrost |

Element characteristics (LC_CultivatedAndManagedVegetation, LC_Plantation, LC_CropYield, LC_Irrigation, LC_FieldSize, LC_BurntStatus, LC_Grazing, LC_FloristicAspect ...) and `LC_UserDefined*Characteristic` with typed `LC_Property` for anything the schema lacks. `LC_MixedClasses` (AND / OR with dominant flag) handle mosaics. `views` hold the LCCS dichotomous tree, which is a framing, not a physical fact.

The two formats differ in nesting, not content, so one table feeds both writers.

## The FAO Land Cover Legend Registry (LCLR)

FAO runs the ISO 19144-1 registry this work feeds: https://data.apps.fao.org/lclr-tool/en/. A static site over one JSON endpoint and one public bucket, scriptable without credentials.

| what | where |
|---|---|
| legend list with per-class name, code, definition text and file names | `GET https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend` |
| per-legend files | `https://storage.googleapis.com/fao-hih-gs-website-review/resources/lclr/legend/<L#>.{LChS,lccs,xsd,csv,eapx}` (`.csv` = id, hex, code, name) |
| class illustrations | `.../resources/lclr/class/<code>.jpg` |
| dataset and reference records | `.../lclr/dataset/`, `.../lclr/reference/`, GeoNetwork metadata ids |

Contents on 2026-09-17: 52 entries; 45 in LCCS3 (Globcover L1, CORINE L16 with 45 classes, Anderson L17, SEEA L15, GLC-SHARE L33, Uruguay L20, and national legends from Nigeria to Ukraine), 4 in LCHS (Burkina Faso L37, Nigeria 2025 L49, Libya 2025 L50, Syria L51), the rest empty. Each registry class pairs a **prose definition** with its **element decomposition**, which is exactly the input→output pair the decompose step must produce.

Roles of the registry:

1. **Answer key.** Leave-one-legend-out evaluation: give the decompose skill only the definition text, score against the registry rows.
2. **Worked examples.** Nearest registry classes by definition text are the few-shot examples for decomposition.
3. **Schema check.** Every registry file is round-tripped; any type or attribute the registry uses that the schemas lack is recorded as a gap.
4. **Comparison target.** A new system can be compared to any registered legend, not only to a second upload.
5. **Destination.** Output is shaped for registry submission.

## Other assets in this folder

| asset | role |
|---|---|
| `g4g2026_ideathon.xsd`, `g4g2026_ideathon.lccs` | LCCS3 schema and a minimal round-trip fixture |
| `cd6247en_doc/graphify-out/graph.json` | ISO 19144-2:2023 definitions, attribute list, and rules text |
| `cd6226en_doc`, `cd6231en_doc` graphs | ISO 19144-1 legend/register concepts; ISO/TS 19144-3 LUML activities (for land-use classes that masquerade as cover) |
| `mapbiomas_doc/provenance/legends.json`, `harmonization.py` | ten titles-only systems and a human-built ground truth of their ambiguities |

## The three projections of one class graph

**Graph.** Nodes: `class`, `horizontal_pattern`, `stratum`, `element`, `characteristic`, `value`, and framing nodes `institution`, `instrument` (law, policy, programme, reporting obligation), `purpose`, `source_span`. Edges: `contains` (class→pattern→stratum→element→characteristic), `constrained_by` (element→value), `named_by` (class→institution), `motivated_by` (class or element→instrument), `evidenced_by` (any→source_span), `same_physical_as` / `overlaps` / `disjoint_from` (class→class across systems, produced by comparison).

**Table.** One long-form row per smallest unit. Column names are LCHS field names (`class_id`, `horizontal_pattern_id`, `stratumID`, `BlockReference`, `elementPresenceType`, `woodyLeafPhenology` ...) so the table is a near-verbatim view of the LCHS record set. It is the file people edit in a spreadsheet and the file that diffs cleanly in git.

| column | example |
|---|---|
| system | mapbiomas_brazil_c10 |
| class_map_code / class_name | 4 / Savanna Formation |
| path | hp1/st1/el1 |
| node_type | element |
| BlockReference | LC_Trees |
| attribute | cover |
| min / max / enum | 10 / 40 / |
| elementPresenceType | Mandatory |
| evidence | "arboreal cover between 10 and 40 %" (source doc p.3) |
| framing_ref | instrument:br-cerrado-definition |
| confidence | 0.7 |
| status | proposed / accepted / disputed |

**FAO XML.** `.LChS` and `.lccs`, both written from the table and both readable back into it.

Conversion is deterministic in every direction (`graph ⇄ table ⇄ LChS / lccs`). A stakeholder can correct the table in a spreadsheet and the XML and OKF nodes regenerate. Schema validation (XSD for `.lccs`, structural for `.LChS`) is the acceptance test; opening files in FAO's desktop tools is not required.

## OKF layout

The OKF convention: knowledge is a folder of Markdown files, one per concept, each with YAML frontmatter and typed relative links. Agents read one starting file, follow only the links they need, and stop. No vector index; retrieval is deterministic and hashable.

```
okf/
  START.md                      entry point for every agent: what exists, how to traverse
  ONTOLOGY.md                   node kinds and typed relations (build fails on any other relation)
  vocab/                        GENERATED
    lccs3/elements/LC_Trees.md  from the XSD: parent chain, allowed characteristics, attributes with enum/range
    lccs3/characteristics/...
    lchs_schema.json            reconstructed LCHS record types and attributes, with provenance per attribute
    _index.json
  standards/                    two pages, drafted by one recorded model call from the ISO graphs, reviewed by a person, hashed
    lcml-rules.md               one element = one concept; new stratum vs second element in a stratum; horizontal pattern vs
                                mixed class; class-level vs element-level characteristics; 2023 additions (density, spreading,
                                life-form specialisation)
    luml-activities.md          land-use activities that masquerade as cover classes and how to record them
  registry/                     GENERATED from the LCLR, hashed by fetch date
    INDEX.md                    every legend: alpha code, country, year, format, class count, files
    L16/SYSTEM.md               one folder per registered legend, same layout as systems/
    L16/classes/311.md          definition text + element rows parsed from the registry file
    L16/L16.lccs, L16.csv       verbatim copies
  candidates/<slug>.md          classification systems found by discover-systems but not yet ingested:
                                publisher, jurisdiction, url, format, why it matters, status
  systems/<slug>/
    SYSTEM.md                   publisher, version, scope statement, source documents, framing summary, run history
    framing/<instrument>.md     one node per law, policy, mandate or programme that shapes class names or thresholds
    classes/<code>.md           one node per class: frontmatter = its table rows; body = definition verbatim, rationale,
                                nearest registry examples, open questions
    elements.csv                the table projection
    <slug>.LChS, <slug>.lccs    the FAO projections
    package/                    registry submission package when built
  attention/<slug>.md           ranked list; each item links to the class and framing nodes it hinges on
  comparisons/<a>__<b>.md       equivalence matrix between two described systems
  agents/
    AGENTS.md                   how any agent platform runs this: entry point, skill order, tool contracts, write scope
    runner.py                   reference driver: plain Python, any model API, tools as subprocesses
    manifests/<skill>.json      inputs, outputs, tools it may call, nodes it must read
  skills/<skill>/SKILL.md       one per step, frontmatter + instructions
  tools/                        every deterministic step as a CLI with JSON in / JSON out
  _index.json                   id → path, kind, sha256
```

Node frontmatter, common fields: `id`, `kind`, `title`, `links: [{rel, id, path}]`, `sources`, `built_from` (sha of the input), `schema: okf/0.1`. Class nodes add `system`, `code`, `rows`, `confidence`, `status`, `open_questions`. Framing nodes add `institution`, `instrument_type`, `jurisdiction`, `effect_on_classes`.

Every node stays under a character cap so an agent reads whole nodes, never pages. `START.md` says: read `SYSTEM.md` for the system you are working on, open only the class nodes you need, open `vocab/` when you need an attribute's allowed values, open the registry classes that `nearest_examples` returns when decomposing.

## Skills and tools

Skills are what an agent does: read OKF nodes, reason, write nodes. Tools are what code does: deterministic, receipted, no model call. Each tool is a CLI with JSON in and JSON out so any runtime can call it.

| step | skill | tool |
|---|---|---|
| 0a vocabulary | – | `xsd_to_vocab`: parse the XSD, emit `vocab/lccs3/` (leaf types, parent chains, attributes, enums, ranges) |
| 0b registry | – | `fetch_registry`: pull the endpoint and every `.LChS` / `.lccs` / `.csv`, parse each with the matching reader, emit `registry/`, reconstruct `lchs_schema.json`, report schema gaps |
| 0c discover | `discover-systems`: given a region, agency, theme or list of names, search the registry index and the web; write one `candidates/<slug>.md` per find. Never ingests on its own. | `registry_search` over `registry/INDEX.md`; web search is the agent's own on its platform |
| 1 ingest | `ingest-classification`: turn a document into `SYSTEM.md` and one class node per class with verbatim definition, code, parent, language, source span. Titles-only classes get an empty definition and `status: titles_only`. If the input is already `.LChS` or `.lccs`, rows come from the file and the run is in **refine mode**: later steps critique and improve existing rows, and every change is a diff against the original. | `readers/` for JSON, CSV, XLSX, PDF, DOCX, HTML, plain text, `.lccs`, `.LChS` |
| 2 framing | `extract-framing`: from scope statement, preface, legal references and class definitions, write `framing/` nodes and link each class to the instruments that motivate its name or thresholds. Asks explicitly: which classes exist because of a rule rather than a physical difference? | `framing_lint`: every class links to a framing node or to `framing/none-stated.md`; every instrument has a jurisdiction |
| 3 decompose | `decompose-class`: for one class, propose the element graph down to the smallest unit using only vocabulary types; cite evidence per row; leave unknown ranges empty; read the nearest registry classes and state how this class differs from each; list siblings and name the discriminating attribute. Titles-only: propose from the name, mark rows `inferred_from_name`, confidence ≤ 0.4. | `nearest_examples`: deterministic lexical match over `registry/*/classes/*.md`, returns node paths. `table_validate`: type in vocabulary, attribute allowed on that type, enum legal, ranges in bounds, covers within a stratum ≤ 100, at least one Mandatory element per non-null class |
| 4 critique | `critique-system`: read all class and framing nodes for a system, add ambiguities the rules miss, phrase each as a decision with options, estimate blast radius across siblings and other systems | `rule_critics`: underspecified, sibling_overlap, hierarchy_conflict, land_use_masquerade, mixed_class_without_proportion, catch_all, threshold_drift, cross_system_collision, framing_only_split (identical element rows differing only by framing, e.g. Primary vs Secondary forest) |
| 5 emit | – | `table_to_lchs` / `lchs_to_table`, `table_to_lccs` / `lccs_to_table`; `okf_build` regenerates `_index.json`, `attention/`, `elements.csv`, checks links, relations and caps |
| 6 compare | `compare-systems`: for two systems (uploaded or registered), propose `same_physical_as` / `overlaps` / `disjoint_from` edges with the attribute that decides each, and note where framing differs though physics match | `equivalence`: mechanical first pass from element sets and range intersection; the skill reviews only uncertain cells |
| 7 package | `prepare-submission`: assemble what the LCLR expects (`.LChS`, `.lccs`, class `.csv`, reference record, dataset record if a map exists) plus a cover note listing unresolved attention items | `submission_check`: schema-valid, csv and XML agree on the class set, no placeholder names ("New Legend", "Describe the ...") |
| 8 submit | `submit-to-registry`, only with `--submit`: draft the message to the LCLR contact with the package attached, then stop for a human to send. Nothing is sent by an agent. Record date and status in `SYSTEM.md`. | – |

### Orchestration

Platform-independent by construction. `agents/AGENTS.md` describes the run for any agent platform: read `START.md`, run the skills in order, call tools by their CLI contract, write only under `systems/<slug>/`, `attention/` and `comparisons/`. `agents/runner.py` is the reference driver: a Python loop that calls a model API per skill and tools as subprocesses. Claude Code runs the same skills through `SKILL.md`; another framework reads the same manifests. The OKF folder is the shared memory between agents.

```
rocky run <input> --system <slug> [--mode propose|refine] [--compare <slug|L#>] [--submit]
rocky discover --region "Alaska" | --agency "USGS" | --names nlcd,avc
rocky registry refresh
```

`--mode` defaults from the input type: documents and tables → propose, `.LChS`/`.lccs` → refine.

## Framing as data

The attention list ranks classes by `severity × blast radius`. Framing nodes change both:

- A class whose only justification is an instrument, with no physical discriminator, is a `framing_only_split` and is routed to the stakeholder who owns that instrument, not to a botanist.
- Two systems that agree on elements but differ in names are a translation problem, ranked low. Two that share a name and differ in elements are a collision, ranked high. The framing node says which.
- Blast radius counts the classes and systems linked to the same instrument, so a threshold set by a national forest law surfaces once with all its dependents.

Each attention item carries: the class, its provisional rows, the ambiguity kind, the concrete options, what depends on it, the evidence spans, and the framing node to consult. The same text is written into the class description in the FAO files so a reviewer using FAO's tools sees the flag.

## Outputs of a run

1. `systems/<slug>/<slug>.LChS` and `<slug>.lccs`: the FAO legend files, every class present, unresolved rows carried as notes in the class description.
2. `attention/<slug>.md`: the ranked list of classes stakeholders should look at.
3. `systems/<slug>/package/`: the registry-ready submission package, and with `--submit` a drafted, unsent message.

Supporting: `elements.csv`, the class and framing nodes, and `comparisons/` when `--compare` is given.

## Validation

- **Round trip:** every registry `.lccs` and `.LChS` and the sample legend go file → table → file and back with every class, stratum, element, presence type and range preserved; `.lccs` output validates against the XSD, `.LChS` output passes the structural check. Cross-format: an LCHS legend → table → `.lccs` validates.
- **Schema coverage:** every type and attribute used anywhere in the registry exists in `vocab/`; gaps are listed in the fetch report, never silently tolerated.
- **Leave-one-out on the registry (primary quality number):** for each held-out registered legend, feed only its definition text to `decompose-class`; score element-type recall, presence-type agreement and range overlap against the registry rows. Report per legend so short-definition legends and prose-rich ones (Bangladesh L8, Nigeria L49) are visible separately.
- **Refine mode:** re-running on a registry legend with no edits produces an empty diff; injecting one wrong cover range produces exactly one attention item pointing at it.
- **MapBiomas regression:** the ten titles-only systems in `legends.json` yield an attention list whose top entries include code 4 (six systems), code 50, code 63, Peru 32, Uruguay 3, and Pasture / Mining / Aquaculture / Silviculture as land-use masquerades. Chile 59/60 surfaces as `framing_only_split`.
- **Document answer key:** the CORINE nomenclature guide, ingested as a PDF, produces rows for 111, 244 and 311 matching the registry's L16 decomposition on element types, phenology and cover ranges.
- **Cross-system check:** MapBiomas Uruguay (titles only) compared with registered Uruguay L20; `compare-systems` finds the forest and grassland equivalences and flags the plantation-species split.
- **OKF hygiene:** `okf_build --check` twice changes no bytes; every link resolves; every relation is in `ONTOLOGY.md`; no node exceeds the cap; every class node links to a framing node.
- **Portability:** `python okf/agents/runner.py --system mapbiomas_brazil` completes outside Claude Code with only a model API key and produces the same `elements.csv` (up to model nondeterminism) as the skill run.

## Build order

1. `xsd_to_vocab` and `vocab/lccs3/`.
2. `ONTOLOGY.md`, `START.md`, frontmatter parser, `okf_build --check`.
3. `fetch_registry`; `lchs_to_table` / `table_to_lchs` from the `.LChS` files, reconstructing `lchs_schema.json`; `lccs_to_table` / `table_to_lccs`; round trips over every registry file and the sample legend.
4. `agents/AGENTS.md`, manifests and `runner.py` skeleton, so every skill is written against the portable contract from the start.
5. `standards/` two pages: one recorded model call from the graphify graphs, then human review.
6. `ingest-classification` with JSON/CSV readers, run on `legends.json`; `.LChS`/`.lccs` readers give refine mode for free from step 3.
7. `decompose-class` with `nearest_examples` and `table_validate`, run on MapBiomas Brazil and on one held-out registry legend; inspect by hand.
8. `extract-framing` and `framing_lint`; MapBiomas framing nodes (Brazilian Forest Code and Cerrado, Argentine Ley 26.331, Chilean Ley 20.283) as the first hand-checked examples.
9. `rule_critics` and `critique-system`; MapBiomas regression and refine-mode tests.
10. Document readers (PDF, DOCX, HTML) on the CORINE guide; document answer-key test.
11. `compare-systems` and `equivalence`; Uruguay cross-check.
12. `prepare-submission`, `submission_check`, `submit-to-registry`; `discover-systems` and `registry_search`.
13. Leave-one-out run over the whole registry; publish the per-legend scores in `registry/EVAL.md`.

## Open item

The LCHS schema is reconstructed from four registry files. If FAO can share the LCHS tool's own schema or export specification, it replaces the reconstruction. Worth one email at the start of the build.
