---
id: registry:L29:lcc8
kind: class
title: lcc8 Grassland
system: registry:L29
code: lcc8
name: Grassland
status: registered
decomposed: true
file_class_id: '57'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_Forbs
- LC_Graminoid
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Forbs
  path: ../../../vocab/elements/LC_Forbs.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc8 Grassland

## Definition (verbatim, FAO LCLR)

Areas covered by herbaceous vegetation with cover ranging from Closed to Open (15–100%). This category includes rangeland and pasture that is not considered cropland.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 58 | 59 Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 58 | 59 Mandatory | `LC_Forbs` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `57`.
