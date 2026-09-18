---
id: registry:L25:Bi
kind: class
title: Bi Flooded woody
system: registry:L25
code: Bi
name: Flooded woody
status: registered
decomposed: true
file_class_id: 12D
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Bi Flooded woody

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by two mandatory stratum that defines the overall class structure. The strata are constituted by two basic elements i.e., woody and water body with fresh water salinity, and natural artificiality.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12E | 132 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |
| 12E | 12F Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `12D`.
