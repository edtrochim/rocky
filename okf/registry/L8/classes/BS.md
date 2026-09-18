---
id: registry:L8:BS
kind: class
title: BS Beach/sand bar
system: registry:L8
code: BS
name: Beach/sand bar
status: registered
decomposed: true
file_class_id: D3
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# BS Beach/sand bar

## Definition (verbatim, FAO LCLR)

Beaches are narrow, gently sloping strip of natural land that lies along the coast and usually consists of loose particles, which are composed of sand. Sand bar are sand deposits within the river channels or in the estuary which are emerging as islands

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D5 | D6 Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  | LC_NaturalSurfaceCharacteristic |

Full rows: `../elements.csv`, class_id `D3`.
