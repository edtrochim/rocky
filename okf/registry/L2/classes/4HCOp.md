---
id: registry:L2:4HCOp
kind: class
title: 4HCOp Closed to open permanently flooded herbaceous
system: registry:L2
code: 4HCOp
name: Closed to open permanently flooded herbaceous
status: registered
decomposed: true
file_class_id: BB
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 4HCOp Closed to open permanently flooded herbaceous

## Definition (verbatim, FAO LCLR)

Closed to open (15-100%) herbaceous vegetation on flooded land (> 4 months)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BC | BD Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| BC | BF Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 4.0–12.0 | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `BB`.
