---
id: registry:L25:Cabs
kind: class
title: Cabs Single layer shrub crop
system: registry:L25
code: Cabs
name: Single layer shrub crop
status: registered
decomposed: true
file_class_id: 1D3
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Cabs Single layer shrub crop

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. It is rainfed plantation area with single shrub crop layer.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1D4 | 1D5 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `1D3`.
