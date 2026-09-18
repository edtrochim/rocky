---
id: registry:L37:Cp
kind: class
title: Cp Permanent culture
system: registry:L37
code: Cp
name: Permanent culture
status: registered
decomposed: true
file_class_id: '98'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Cp Permanent culture

## Definition (verbatim, FAO LCLR)

These are crops that are grown all year round without interruption. Industrial crops and orchards are grouped together in this unit. Industrial crops in the case of Burkina Faso boil down to sugar cane, for example, cultivated over vast areas with sophisticated technical means for sprinkler irrigation. It is easily identifiable in the images by the shape of the plots and the extent of the crops.
There are also orchards which consist of plantations of fruit trees intended mainly for food products. These include, for example, mango orchards, cashew trees, guava trees, etc. their extent varies but they are difficult to identify from Landsat images. However, enormous field work supplemented by documentation makes it possible to recognize them.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 99 | 100 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (speciesName=Mango); LC_FloristicAspectsCharacteristic |

Full rows: `../elements.csv`, class_id `98`.
