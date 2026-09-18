---
id: registry:L25:Stb
kind: class
title: Stb Dwarf shrub steppe
system: registry:L25
code: Stb
name: Dwarf shrub steppe
status: registered
decomposed: true
file_class_id: FE
n_rows: 32
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Stb Dwarf shrub steppe

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of dwarf shrub steppe. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element herbaceous growth forms.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| FF | 100 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–50.0 | height 10.0–80.0 | LC_VegetationArtificialityCharacteristic |
| FF | 103 Mandatory | `LC_Shrub` | Mandatory | 4.0–10.0 | height 0.02–1.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `FE`.
