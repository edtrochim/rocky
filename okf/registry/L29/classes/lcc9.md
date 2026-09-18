---
id: registry:L29:lcc9
kind: class
title: lcc9 Snow
system: registry:L29
code: lcc9
name: Snow
status: registered
decomposed: true
file_class_id: 5E
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Snow
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc9 Snow

## Definition (verbatim, FAO LCLR)

This class describes perennial snow (persistence > 9 months per year).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5F | 60 Mandatory | `LC_Snow` | Mandatory | 10.0–100.0 | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |

Full rows: `../elements.csv`, class_id `5E`.
