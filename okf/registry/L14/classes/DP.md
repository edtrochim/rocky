---
id: registry:L14:DP
kind: class
title: DP Date palm plantation
system: registry:L14
code: DP
name: Date palm plantation
status: registered
decomposed: true
file_class_id: '67'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# DP Date palm plantation

## Definition (verbatim, FAO LCLR)

Regular date palm plantation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 68 | 69 Mandatory | `LC_Tree` | Mandatory | 60.0–80.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Date Palm) |

Full rows: `../elements.csv`, class_id `67`.
