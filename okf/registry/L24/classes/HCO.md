---
id: registry:L24:HCO
kind: class
title: HCO Herbaceous
system: registry:L24
code: HCO
name: Herbaceous
status: registered
decomposed: true
file_class_id: '31'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# HCO Herbaceous

## Definition (verbatim, FAO LCLR)

Herbaceous closed-to-sparse in terrestrial and aquatic/regularly flooded land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 32 | 33 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `31`.
