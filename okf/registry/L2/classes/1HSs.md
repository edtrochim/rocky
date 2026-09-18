---
id: registry:L2:1HSs
kind: class
title: 1HSs Small herbaceous crops in sloping land
system: registry:L2
code: 1HSs
name: Small herbaceous crops in sloping land
status: registered
decomposed: true
file_class_id: '20'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 1HSs Small herbaceous crops in sloping land

## Definition (verbatim, FAO LCLR)

Small (< 2 ha) herbaceous crops in sloping land

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 22 | 23 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `20`.
