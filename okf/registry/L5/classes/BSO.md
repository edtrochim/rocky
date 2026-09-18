---
id: registry:L5:BSO
kind: class
title: BSO Bare soil
system: registry:L5
code: BSO
name: Bare soil
status: registered
decomposed: true
file_class_id: 4A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# BSO Bare soil

## Definition (verbatim, FAO LCLR)

Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover. Non-vegetated ar-eas are characterized by NDVI values close to zero.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4B | 4C Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `4A`.
