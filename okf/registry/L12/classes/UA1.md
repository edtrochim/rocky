---
id: registry:L12:UA1
kind: class
title: UA1 Urban area
system: registry:L12
code: UA1
name: Urban area
status: registered
decomposed: true
file_class_id: '2'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# UA1 Urban area

## Definition (verbatim, FAO LCLR)

Relatively larger urban built-up areas, commonly with presence of trees, occasionally with small cultivated fields; scattered open areas observed in some areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Building` | Mandatory | 20.0–60.0 |  | LC_ConstructionUse (type=Residential) |
| 3 | 4 Mandatory | `LC_Tree` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
