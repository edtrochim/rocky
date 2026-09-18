---
id: registry:L20:Aa_l
kind: class
title: Aa_l Lakes, reservoirs and barrages
system: registry:L20
code: Aa_l
name: Lakes, reservoirs and barrages
status: registered
decomposed: true
file_class_id: BE
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Aa_l Lakes, reservoirs and barrages

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BF | C0 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Atmospheric | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterChemistryCharacteristic (nutrient_level=TDS <1000ppm); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `BE`.
