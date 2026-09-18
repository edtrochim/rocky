---
id: registry:L49:Vnar
kind: class
title: Vnar Mangroves
system: registry:L49
code: Vnar
name: Mangroves
status: registered
decomposed: true
file_class_id: '4'
n_rows: 77
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Vnar Mangroves

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by marine vegetation found in close proximity to the ocean, creeks and estuaries. They can be pure stands or mixed with other vegetation such as Nypa palm, Raphia and others. The canopy closure is usually between 30 percent and 70 percent depending on the nature of logging activities taking place in the creeks. It is composed of two stratum that defines the overall structure of the class, characterized as: •Element of trees where the vegetation artificiality is defined as natural and seminatural. •Element of water body where the vegetation artificiality is defined as natural and seminatural. •Periodic type is tidal. •Water salinity is brackish.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 4 Fixed | `LC_Tree` | Fixed | 30–70 | depth -100–0; density 0–100000; lengthOfTemporalRelationship 1–100 |  |
| 4 | 5 Fixed | `LC_WaterBody` | Fixed | 0–100 | depth -100–0; periodVariationType=Tidal; persistencePeriod 0–365; density 0–999; lengthOfTemporalRelationship 1–100 | LC_WaterSalinityCharacteristic (waterSalinity=Brackish); LC_ArtificialityCharacteristic (artificiality=Natural) |

Full rows: `../elements.csv`, class_id `4`.
