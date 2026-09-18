---
id: registry:L11:MQ
kind: class
title: MQ Mines and quarries
system: registry:L11
code: MQ
name: Mines and quarries
status: registered
decomposed: true
file_class_id: A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Extraction
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Extraction
  path: ../../../vocab/elements/LC_Extraction.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# MQ Mines and quarries

## Definition (verbatim, FAO LCLR)

Major mines and quarries as well as temporary building material extraction.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B | C Mandatory | `LC_Extraction` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A`.
