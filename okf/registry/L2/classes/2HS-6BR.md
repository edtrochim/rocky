---
id: registry:L2:2HS-6BR
kind: class
title: 2HS//6BR Sparse herbaceous or Bare rock
system: registry:L2
code: 2HS//6BR
name: Sparse herbaceous or Bare rock
status: registered
decomposed: true
file_class_id: '48'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2HS//6BR Sparse herbaceous or Bare rock

## Definition (verbatim, FAO LCLR)

Sparse (1-15%) short herbaceous vegetation or Bare rock

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 49 | 4A Optional | `LC_HerbaceousGrowthForm` | Exclusive | 1.0–15.0 | height 3.0–30.0 | LC_VegetationArtificialityCharacteristic |
| 49 | 4A Optional | `LC_BareRock` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `48`.
