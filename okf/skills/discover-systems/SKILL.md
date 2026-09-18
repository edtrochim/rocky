---
id: skill:discover-systems
kind: guide
title: "Skill: discover-systems"
schema: okf/0.1
name: discover-systems
description: Find land cover classification systems for a region, agency or theme and record them as candidates.
inputs: [query]
tools: [registry_search]
---

# discover-systems

Given a region, an agency, a theme or a list of names, find classification systems worth ingesting and
write one `candidates/<slug>.md` per find. Never ingest from here.

## How to work

1. Search the registry first: `python okf/tools/registry_search.py --q <term>`. A registered legend is
   the best candidate because it already carries FAO's decomposition; note its id.
2. Search the web with the platform's own tool for the publisher's classification document: the
   nomenclature guide, the legend code sheet, the algorithm theoretical basis document, the national
   standard. Prefer the document that carries class *definitions*, not the map viewer.
3. For each find, record: publisher, jurisdiction, year and version, the URL of the defining document,
   its format (pdf, html, xlsx, LChS, lccs), whether it has prose definitions or titles only, how many
   classes, why it matters (which stakeholder uses it, what it is compared against), and `status: found`.
4. Do not record datasets without a classification document, and do not record secondary summaries when
   the primary document is available.

## Candidate node

Frontmatter: `id: candidate:<slug>`, `kind: candidate`, `title`, `publisher`, `jurisdiction`, `year`,
`url`, `format`, `definitions: prose | titles | lcml`, `n_classes`, `registry_id` (if registered),
`status: found`, `links` (`see` to the registry SYSTEM.md when registered). Body: three to six sentences
on what it is, why it matters and what ingesting it will need (a PDF reader, a table, a translation).
