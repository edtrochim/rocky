---
id: registry:L2:1HLMv
kind: class
title: 1HLMv Large to medium herbaceous crops in valley floor
system: registry:L2
code: 1HLMv
name: Large to medium herbaceous crops in valley floor
status: registered
decomposed: true
file_class_id: '27'
n_rows: 23
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

# 1HLMv Large to medium herbaceous crops in valley floor

## Definition (verbatim, FAO LCLR)

Large to medium (> 2 ha) herbaceous crops in valley floor

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 29 | 2A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `27`.
