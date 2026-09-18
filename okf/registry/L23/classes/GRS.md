---
id: registry:L23:GRS
kind: class
title: GRS Grassland
system: registry:L23
code: GRS
name: Grassland
status: registered
decomposed: true
file_class_id: A
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# GRS Grassland

## Definition (verbatim, FAO LCLR)

Natural herbaceous vegetation - close to very open.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B | C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A`.
