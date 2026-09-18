---
id: registry:L3:MN
kind: class
title: MN Mines
system: registry:L3
code: MN
name: Mines
status: registered
decomposed: true
file_class_id: 15F
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Extraction
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Extraction
  path: ../../../vocab/elements/LC_Extraction.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# MN Mines

## Definition (verbatim, FAO LCLR)

Extractions sites

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 160 | 161 Mandatory | `LC_Extraction` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `15F`.
