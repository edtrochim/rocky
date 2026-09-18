---
id: registry:L28:Fhm
kind: class
title: Fhm Forest humid montane
system: registry:L28
code: Fhm
name: Forest humid montane
status: registered
decomposed: true
file_class_id: '2'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Fhm Forest humid montane

## Definition (verbatim, FAO LCLR)

Land spanning more than 0.5 ha with trees that have heights of between 20-50m with combined cover of natural herbaceous growth form. Geographical aspect is catchment forest, ≥ 800 m asl

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5 | 6 Mandatory | `LC_Tree` | Mandatory |  | height 20.0–50.0 | LC_VegetationArtificialityCharacteristic |
| 5 | 9 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
