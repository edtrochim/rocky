---
id: registry:L42:Co
kind: class
title: Co Citrus orchard
system: registry:L42
code: Co
name: Citrus orchard
status: registered
decomposed: true
file_class_id: '64'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Co Citrus orchard

## Definition (verbatim, FAO LCLR)

Citrus includes all types of lemons, oranges, clementines, etc., typically found near the coast.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 65 | 66 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Plantation]/name=Plantation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Citrus Fruits) |

Full rows: `../elements.csv`, class_id `64`.
