---
id: registry:L12:RH2
kind: class
title: RH2 Rural settlements (sloping and mountaneous area)
system: registry:L12
code: RH2
name: Rural settlements (sloping and mountaneous area)
status: registered
decomposed: true
file_class_id: 1D
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# RH2 Rural settlements (sloping and mountaneous area)

## Definition (verbatim, FAO LCLR)

Rural houses in sloping and mountaneous areas (slope greater than 5 degrees) + herbaceous natural vegetation, ocassionally with small fields and sometimes with shrubs emplyed for demarcation, usually treeless.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E | 1F Mandatory | `LC_Building` | Mandatory | 5.0–20.0 |  |  |
| 1E | 1F Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1D`.
