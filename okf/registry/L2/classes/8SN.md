---
id: registry:L2:8SN
kind: class
title: 8SN Perennial snow
system: registry:L2
code: 8SN
name: Perennial snow
status: registered
decomposed: true
file_class_id: EB
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

# 8SN Perennial snow

## Definition (verbatim, FAO LCLR)

Perennial snow (> 9 months)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| EC | ED Mandatory | `LC_Snow` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 9.0–12.0 | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `EB`.
