---
id: registry:L25:Sd
kind: class
title: Sd Dump sites - extraction sites
system: registry:L25
code: Sd
name: Dump sites - extraction sites
status: registered
decomposed: true
file_class_id: '326'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonBuiltUpSurface
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonBuiltUpSurface
  path: ../../../vocab/elements/LC_NonBuiltUpSurface.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sd Dump sites - extraction sites

## Definition (verbatim, FAO LCLR)

Land used for disposal of waste materials is known as dump sites. Extraction sites are defined by the absence of the original land cover which is removed by human activity or machinery for extraction of sand, stone, mineral or coal.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 327 | 328 Mandatory | `LC_NonBuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `326`.
