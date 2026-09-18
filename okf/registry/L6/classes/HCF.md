---
id: registry:L6:HCF
kind: class
title: HCF Herbaceous crops in flood plain
system: registry:L6
code: HCF
name: Herbaceous crops in flood plain
status: registered
decomposed: true
file_class_id: 6B
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# HCF Herbaceous crops in flood plain

## Definition (verbatim, FAO LCLR)

Herbaceous crop located only in proximity of the riverbed is termed as crop in floodplain. The water supply is provided either by irrigation or by the annual floods. Crop in floodplain includes her-baceous crop irrigated in flood plain and herba-ceous crop post-flooding

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6C | 6D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Postflooding]/description=Describe the postflooding, elements/LC_Characteristic[LC_Postflooding]/name=Postflooding) |

Full rows: `../elements.csv`, class_id `6B`.
