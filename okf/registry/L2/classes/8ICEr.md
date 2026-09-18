---
id: registry:L2:8ICEr
kind: class
title: 8ICEr Rocky glacier
system: registry:L2
code: 8ICEr
name: Rocky glacier
status: registered
decomposed: true
file_class_id: E5
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_Ice
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_Ice
  path: ../../../vocab/elements/LC_Ice.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 8ICEr Rocky glacier

## Definition (verbatim, FAO LCLR)

Glacier covered by rock debris

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E6 | 11B Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Gravel |  |
| E6 | E7 Mandatory | `LC_Ice` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 9.0–12.0 |  |

Full rows: `../elements.csv`, class_id `E5`.
