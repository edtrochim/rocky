---
id: registry:L25:L
kind: class
title: L Lakes
system: registry:L25
code: L
name: Lakes
status: registered
decomposed: true
file_class_id: '334'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# L Lakes

## Definition (verbatim, FAO LCLR)

A natural standing water reservoir that is bigger than a pond and has an irregular shape. This class consists of one mandatory strata.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 335 | 336 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Standing |  |

Full rows: `../elements.csv`, class_id `334`.
