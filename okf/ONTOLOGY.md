---
id: ontology
kind: ontology
title: Ontology
schema: okf/0.1
---

# Ontology

Node kinds and typed relations of this knowledge base. The build rejects any other kind or relation.

## Kinds

| kind | meaning |
|---|---|
| `start` | the single entry point; links to everything an agent may need |
| `ontology` | the node kinds and relations, rendered from code |
| `vocab_element` | one LCML atomic element type (LChS BlockReference), from the schema |
| `vocab_characteristic` | one LCML characteristic type (LChS CharacteristicReference), from the schema |
| `vocab_enum` | one enumeration with its documented values |
| `vocab_record` | one flat record type of the LChS file format |
| `standard` | a reviewed digest of an ISO 19144 rule or concept |
| `registry_index` | the FAO LCLR legend list |
| `system` | one classification system: publisher, scope, sources, framing summary |
| `class` | one class of a system: definition, element rows, rationale, open questions |
| `framing` | an institution, instrument or purpose that shapes class names or thresholds |
| `candidate` | a classification system found but not yet ingested |
| `attention` | the ranked list of classes stakeholders should look at, for one system |
| `comparison` | an equivalence matrix between two described systems |
| `eval` | scores from a leave-one-out or regression run |
| `guide` | instructions for agents or people (AGENTS.md, skill pages) |

## Relations

| relation | from | to | meaning |
|---|---|---|---|
| `see` | * | * | navigation: the target is worth opening next |
| `has_class` | system | class | the system defines this class |
| `in_system` | class, framing, attention | system | belongs to this system |
| `uses_type` | class | vocab_element, vocab_characteristic | the class description uses this LCML type |
| `allows` | vocab_element, vocab_characteristic | vocab_enum | a property of this type takes values from this enum |
| `specialises` | vocab_element | vocab_element | subtype of, per the schema documentation |
| `named_by` | class | framing | the class name comes from this institution or instrument |
| `motivated_by` | class | framing | a threshold or split in this class exists because of this instrument |
| `evidenced_by` | class, framing | system | the evidence span is in this system's source documents |
| `nearest_example` | class | class | a registered class whose definition is closest; used as a worked example |
| `same_physical_as` | class | class | element rows are equivalent (comparison) |
| `overlaps` | class | class | element rows intersect but differ (comparison) |
| `disjoint_from` | class | class | element rows are disjoint (comparison) |
| `about` | attention, eval | class, system | the item concerns this node |
| `hinges_on` | attention | framing | the decision belongs to whoever owns this instrument |
| `compares` | comparison | system | one of the two systems compared |
| `in_registry` | system | registry_index | this system is a registered FAO legend |
| `supersedes` | system | system | a newer version of the same system |

## Node grammar

Every node is Markdown with a YAML frontmatter block holding `id`, `kind`, `title`, `schema`, optional `links` (list of `{rel, id, path}` with `path` relative to the node), `sources` and `built_from`. Nodes stay under 12000 characters so an agent reads whole nodes. Links are the only retrieval mechanism: start at `START.md`, follow the links you need, stop.
