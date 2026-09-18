---
id: registry:L12:BLR
kind: class
title: BLR Boulder and loose rock
system: registry:L12
code: BLR
name: Boulder and loose rock
status: registered
decomposed: true
file_class_id: '50'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_GrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# BLR Boulder and loose rock

## Definition (verbatim, FAO LCLR)

Areas with large scattered boulders and/or unconsolidated loose rocks, commonly sloping and associated with rock outcrops, usually together with open - closed natural vegetation and/or shrubs and/or natural trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 51 | 52 Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Boulder |  |
| 51 | 52 Mandatory | `LC_GrowthForm` | Optional | 0.0–10.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `50`.
