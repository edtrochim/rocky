---
id: registry:L26:SA
kind: class
title: SA Sand
system: registry:L26
code: SA
name: Sand
status: registered
decomposed: true
file_class_id: '41'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# SA Sand

## Definition (verbatim, FAO LCLR)

Loose and shifting sand. Optional layer of growth dorms (herbs, shrubs and trees) not exceeding 3% cover.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  |  |
| 42 | 45 Optional | `LC_GrowthForm` | Mandatory | 0.0–3.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `41`.
