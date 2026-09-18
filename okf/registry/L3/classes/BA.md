---
id: registry:L3:BA
kind: class
title: BA Bare Area
system: registry:L3
code: BA
name: Bare Area
status: registered
decomposed: true
file_class_id: '43'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# BA Bare Area

## Definition (verbatim, FAO LCLR)

Rock or Soil sometimes with very sparse natural vegetation (0-15%)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 44 | 45 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |
| 44 | 143 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 0.1–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `43`.
