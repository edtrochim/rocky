---
id: registry:L6:SNW
kind: class
title: SNW Snow
system: registry:L6
code: SNW
name: Snow
status: registered
decomposed: true
file_class_id: '77'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_Snow
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# SNW Snow

## Definition (verbatim, FAO LCLR)

This class includes snow permanent, glaciers and glacier with debris. Snow permanent is the area characterized by year-long surface cover of ice and/or snow.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 78 | 79 Mandatory | `LC_Snow` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |

Full rows: `../elements.csv`, class_id `77`.
