---
id: registry:L26:HCI
kind: class
title: HCI Herbaceous crop irrigated
system: registry:L26
code: HCI
name: Herbaceous crop irrigated
status: registered
decomposed: true
file_class_id: D
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# HCI Herbaceous crop irrigated

## Definition (verbatim, FAO LCLR)

Herbaceous crop irrigated (mainly spate irrigation).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E | F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `D`.
