---
id: registry:L2:8ICE
kind: class
title: 8ICE Glacier
system: registry:L2
code: 8ICE
name: Glacier
status: registered
decomposed: true
file_class_id: DF
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_Ice
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Ice
  path: ../../../vocab/elements/LC_Ice.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 8ICE Glacier

## Definition (verbatim, FAO LCLR)

Glacier

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E0 | E1 Mandatory | `LC_Ice` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 9.0–12.0 | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `DF`.
