---
id: registry:L5:SDU
kind: class
title: SDU Sand dunes
system: registry:L5
code: SDU
name: Sand dunes
status: registered
decomposed: true
file_class_id: '46'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# SDU Sand dunes

## Definition (verbatim, FAO LCLR)

Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover. Non-vegetated areas are charac-terized by NDVI values close to zero.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 47 | 48 Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `46`.
