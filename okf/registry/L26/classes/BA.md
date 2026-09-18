---
id: registry:L26:BA
kind: class
title: BA Bare Area
system: registry:L26
code: BA
name: Bare Area
status: registered
decomposed: true
file_class_id: '19'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_NaturalSurfaceElement
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# BA Bare Area

## Definition (verbatim, FAO LCLR)

Optional layer of Growth forms (Herbs, Shrubs ans Trees) not exceeding 3% cover.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1A | 1B Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |
| 1A | 1D Optional | `LC_GrowthForm` | Mandatory | 0.0–3.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `19`.
