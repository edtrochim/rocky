---
id: registry:L42:Bo
kind: class
title: Bo Banana orchard
system: registry:L42
code: Bo
name: Banana orchard
status: registered
decomposed: true
file_class_id: 7D
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Bo Banana orchard

## Definition (verbatim, FAO LCLR)

Banana trees are located in coastal areas, especially in the South of the Lebanon.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7E | 7F Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Banana) |

Full rows: `../elements.csv`, class_id `7D`.
