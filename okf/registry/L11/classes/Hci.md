---
id: registry:L11:Hci
kind: class
title: Hci Herbaceous crop irrigated
system: registry:L11
code: Hci
name: Herbaceous crop irrigated
status: registered
decomposed: true
file_class_id: 10F
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# Hci Herbaceous crop irrigated

## Definition (verbatim, FAO LCLR)

Irrigated cultivation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 110 | 111 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `10F`.
