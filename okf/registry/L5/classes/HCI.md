---
id: registry:L5:HCI
kind: class
title: HCI Herbaceous crops irrigated
system: registry:L5
code: HCI
name: Herbaceous crops irrigated
status: registered
decomposed: true
file_class_id: '3'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# HCI Herbaceous crops irrigated

## Definition (verbatim, FAO LCLR)

Agricultural areas characterized by ex-tensive irrigational facilities. The pres-ence channels for irrigation is a distinc-tive factor of this land cover class. The greenness associated with irrigated sites is generally independent of rainfall. Irri-gated crops have 2 higher peaks corre-sponding to the two main crop seasons: Kharif (first sowing season from April – June and harvested during October – December) with the main crops such as rice, sugarcane, cotton and maize and Rabi (second sowing season from Octo-ber – December and harvested in April – May) with main crops such as cereals and oil seeds.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 5 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `3`.
