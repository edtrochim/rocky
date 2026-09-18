---
id: registry:L7:Pw
kind: class
title: Pw Permanent Wadi
system: registry:L7
code: Pw
name: Permanent Wadi
status: registered
decomposed: true
file_class_id: C9
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Pw Permanent Wadi

## Definition (verbatim, FAO LCLR)

Streams of with permanent flowing fresh water with weekly periodic variation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| CB | CC Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Weeks; dynamics=Flowing | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `C9`.
