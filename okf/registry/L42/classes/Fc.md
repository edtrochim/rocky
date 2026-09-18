---
id: registry:L42:Fc
kind: class
title: Fc Field crops
system: registry:L42
code: Fc
name: Field crops
status: registered
decomposed: true
file_class_id: 5C
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_GrowthForm
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Fc Field crops

## Definition (verbatim, FAO LCLR)

Field crops include plowed land cultivated with annual, biennial, and triennial herbaceous crops. This category is subdivided into: (1) large open field crops, (2) small open field crops or terraces, (3) abandoned agricultural land, and (4) urban sprawl on open field crops.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5D | 62 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 5D | 5E Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `5C`.
