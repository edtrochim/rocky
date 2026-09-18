---
id: registry:L42:Ft
kind: class
title: Ft Fruit trees orchard
system: registry:L42
code: Ft
name: Fruit trees orchard
status: registered
decomposed: true
file_class_id: 8A
n_rows: 25
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

# Ft Fruit trees orchard

## Definition (verbatim, FAO LCLR)

Fruit trees include deciduous or evergreen trees, irrigated or rain-fed, as well as shrubs that produce either stone or pome fruits, along with exotic fruits such as avocados and mangoes. Satellite images are used to identify these orchards. Nurseries and planted pastures are not included in this category.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8B | 8C Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Fruits and Nuts) |

Full rows: `../elements.csv`, class_id `8A`.
