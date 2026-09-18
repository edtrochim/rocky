---
id: registry:L12:HCIR
kind: class
title: HCIR Irrigated agriculture
system: registry:L12
code: HCIR
name: Irrigated agriculture
status: registered
decomposed: true
file_class_id: E7
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# HCIR Irrigated agriculture

## Definition (verbatim, FAO LCLR)

Small size irrigated herbaceous crops near water courses.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E8 | E9 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `E7`.
