---
id: registry:L30:Arg
kind: class
title: Arg Wooded shrubland
system: registry:L30
code: Arg
name: Wooded shrubland
status: registered
decomposed: true
file_class_id: '60'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Arg Wooded shrubland

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 62 | 63 Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 | height 0.3–1.5 | LC_VegetationArtificialityCharacteristic |
| 62 | 66 Optional | `LC_WoodyGrowthForm` | Mandatory | 1.0–9.0 | height 3.0–7.0 |  |

Full rows: `../elements.csv`, class_id `60`.
