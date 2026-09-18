---
id: registry:L37:Starbo
kind: class
title: Starbo Tree steppe
system: registry:L37
code: Starbo
name: Tree steppe
status: registered
decomposed: true
file_class_id: '41'
n_rows: 44
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Starbo Tree steppe

## Definition (verbatim, FAO LCLR)

This plant formation is especially present in the northern parts of Burkina Faso (sub-Sahelian phytogeographic sector) and strongly represented for example in the regions of Tougri-Yalgo, Djibo-Kongoussi. It presents itself in the form of an alternation of tree strata (7 to 12 m) and bare soils of small extent (compared to the vegetation), sometimes occupied by a rare herbaceous carpet dotted with termite mounds.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 33 Fixed | `` | Fixed | 0–100 | density 0–100000; lengthOfTemporalRelationship 1–100 |  |
| 42 | 43 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20–50 | height 10–80 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 42 | 45 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20–50 | height 7–12 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `41`.
