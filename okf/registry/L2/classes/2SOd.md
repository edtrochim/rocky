---
id: registry:L2:2SOd
kind: class
title: 2SOd Open dwarf shrubs with sparse herbaceous
system: registry:L2
code: 2SOd
name: Open dwarf shrubs with sparse herbaceous
status: registered
decomposed: true
file_class_id: 6F
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2SOd Open dwarf shrubs with sparse herbaceous

## Definition (verbatim, FAO LCLR)

Open (15-65 %) dwarf shrubs with open (15-100%) herbaceous

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 70 | 71 Mandatory | `LC_Shrub` | Mandatory | 15.0–40.0 | height 0.03–5.0 | LC_VegetationArtificialityCharacteristic |
| 70 | 71 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–10.0 | height 3.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6F`.
