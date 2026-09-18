---
id: start
kind: start
title: Start here
schema: okf/0.1
links:
- rel: see
  id: ontology
  path: ONTOLOGY.md
- rel: see
  id: agents
  path: agents/AGENTS.md
- rel: see
  id: vocab
  path: vocab/INDEX.md
- rel: see
  id: registry
  path: registry/INDEX.md
---

# Start here

This folder is a knowledge base about **land cover classification systems** and how to express each class in
the ISO 19144-2 Land Cover Meta Language (LCML): a class as one or more horizontal patterns, each a stack of
strata, each stratum holding atomic elements (trees, shrubs, graminoids, built-up surface, bare soil, water
body ...) with properties (presence, cover, height ...) and characteristics (artificiality, salinity, crop
parameters ...). The output of the work is FAO's file formats, LChS (2023 edition) and LCCS3, and a ranked
list of classes stakeholders must decide on.

Every file here is a node: Markdown with YAML frontmatter and typed links. Read one node, follow only the
links you need, stop. There is no search index; the links are the retrieval.

## Where to go

- [Ontology](ONTOLOGY.md): the node kinds and relations this folder allows.
- [How agents run this](agents/AGENTS.md): the skill order, the tool contracts, what an agent may write.
- [LCML vocabulary](vocab/INDEX.md): every element type, characteristic type, record type and enumeration,
  generated from FAO's LChS schema with LCCS3 names cross-walked. Open an element page when you need to know
  which properties it allows and which values are legal.
- [FAO Land Cover Legend Registry](registry/INDEX.md): 47 registered legends with their classes, each pairing
  a prose definition with FAO's own element decomposition. These are the worked examples and the answer key.
- `systems/<slug>/`: classification systems ingested by this workflow. Each has `SYSTEM.md`, `framing/`,
  `classes/`, `elements.csv` and the FAO files.
- `attention/<slug>.md`: what stakeholders should look at for a system, ranked.
- `comparisons/`: equivalence matrices between two described systems.
- `standards/`: two reviewed pages on the LCML rules and the land-use activities that masquerade as cover.

## Rules that hold everywhere

- Never invent a threshold. A property with no evidence stays empty and the class is flagged.
- Never reclassify silently. Every change to a class is a row diff with a note.
- The registry and the schemas are provenance, not opinion: do not edit `vocab/` or `registry/` by hand.
- Nothing here sends anything anywhere. Submission to FAO is a package plus a drafted message a person sends.
