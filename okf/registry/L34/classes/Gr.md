---
id: registry:L34:Gr
kind: class
title: Gr Grassland
system: registry:L34
code: Gr
name: Grassland
status: registered
decomposed: true
file_class_id: '49'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Gr Grassland

## Definition (verbatim, FAO LCLR)

This class is categorized by the prevalence of herbaceous vegetation, mainly grasses, with sparse trees or shurbs occasionally being present.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4A | 4B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  |  |
| 4A | 4D Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `49`.
