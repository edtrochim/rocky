---
id: registry:L14:EX
kind: class
title: EX Extraction site
system: registry:L14
code: EX
name: Extraction site
status: registered
decomposed: true
file_class_id: A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Extraction
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Extraction
  path: ../../../vocab/elements/LC_Extraction.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# EX Extraction site

## Definition (verbatim, FAO LCLR)

Major mines and quarries as well as temporary building material extraction

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B | C Mandatory | `LC_Extraction` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A`.
