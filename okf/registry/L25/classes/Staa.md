---
id: registry:L25:Staa
kind: class
title: Staa Trees and shrub steppe
system: registry:L25
code: Staa
name: Trees and shrub steppe
status: registered
decomposed: true
file_class_id: F6
n_rows: 32
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Staa Trees and shrub steppe

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of tree and shrub steppe. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element herbaceous growth forms.A strata of basic element woody growth forms emergent from the main strata is present.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F7 | F8 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–50.0 | height 10.0–80.0 | LC_VegetationArtificialityCharacteristic |
| F7 | FB Mandatory | `LC_WoodyGrowthForm` | Mandatory | 4.0–10.0 | height 2.0–7.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `F6`.
