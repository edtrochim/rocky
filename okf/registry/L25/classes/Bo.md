---
id: registry:L25:Bo
kind: class
title: Bo Bomas
system: registry:L25
code: Bo
name: Bomas
status: registered
decomposed: true
file_class_id: '306'
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Building
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Bo Bomas

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of bomas. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by three basic elements built up, herbs and bare area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 307 | 308 Mandatory | `LC_Building` | Mandatory |  | construction_material=Light Material |  |
| 30A | 30B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |
| 30F | 310 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `306`.
