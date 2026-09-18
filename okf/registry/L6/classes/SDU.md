---
id: registry:L6:SDU
kind: class
title: SDU Sand dunes
system: registry:L6
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
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# SDU Sand dunes

## Definition (verbatim, FAO LCLR)

Bare area/undifferenti-ated area not used for cultivation and usually devoid of grass and shrub cover. Non-vege-tated areas are charac-terized by NDVI values close to zero.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 47 | 48 Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `46`.
