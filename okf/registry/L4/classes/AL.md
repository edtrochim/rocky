---
id: registry:L4:AL
kind: class
title: AL Arable land
system: registry:L4
code: AL
name: Arable land
status: registered
decomposed: true
file_class_id: 2B
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# AL Arable land

## Definition (verbatim, FAO LCLR)

Cultivated and managed land dominated by herbaceous growth forms.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C | 2D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_GrazedCharacteristic |

Full rows: `../elements.csv`, class_id `2B`.
