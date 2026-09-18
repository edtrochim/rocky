---
id: registry:L14:BS
kind: class
title: BS Bare soil
system: registry:L14
code: BS
name: Bare soil
status: registered
decomposed: true
file_class_id: DB
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# BS Bare soil

## Definition (verbatim, FAO LCLR)

Bare areas -undifferentiated areas not used for cultivation and usually devoid of grass or shrub cover, commonly associated with degraded land and erosion effects, sometimes within or adjacent to urban and rural areas

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DC | DD Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `DB`.
