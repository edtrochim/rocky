---
id: registry:L28:Bt
kind: class
title: Bt Bushland thicket
system: registry:L28
code: Bt
name: Bushland thicket
status: registered
decomposed: true
file_class_id: '39'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Bt Bushland thicket

## Definition (verbatim, FAO LCLR)

Land not defined as “Forest”, trees lower than 5 m and a canopy cover of 0.1-15%, or trees able to reach these thresholds with a combined cover of shrubs. It does not include land that is predominantly under agricultural or urban land use.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3A | 3B Mandatory | `LC_Shrub` | Mandatory |  | height 0.0–5.0 | LC_VegetationArtificialityCharacteristic |
| 3A | 3E Mandatory | `LC_Tree` | Mandatory | 0.0–15.0 | height 0.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `39`.
