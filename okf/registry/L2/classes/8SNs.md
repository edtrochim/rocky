---
id: registry:L2:8SNs
kind: class
title: 8SNs Seasonal snow
system: registry:L2
code: 8SNs
name: Seasonal snow
status: registered
decomposed: true
file_class_id: F1
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_Snow
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 8SNs Seasonal snow

## Definition (verbatim, FAO LCLR)

Seasonal snow (< 9 months)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F2 | F3 Mandatory | `LC_Snow` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 1.0–9.0 | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `F1`.
