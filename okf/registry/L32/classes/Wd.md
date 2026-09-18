---
id: registry:L32:Wd
kind: class
title: Wd Wetlands
system: registry:L32
code: Wd
name: Wetlands
status: registered
decomposed: true
file_class_id: '37'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Wd Wetlands

## Definition (verbatim, FAO LCLR)

Wetlands are areas where water covers the soil, or is present either at or near the surface of the soil all year or for varying periods of time during the year, including during the growing season. Wetlands may support both aquatic and terrestrial species.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 38 | 39 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  |  |
| 38 | 3B Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `37`.
