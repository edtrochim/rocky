---
id: registry:L25:Saa
kind: class
title: Saa Tree and shrub savanna
system: registry:L25
code: Saa
name: Tree and shrub savanna
status: registered
decomposed: true
file_class_id: CE
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

# Saa Tree and shrub savanna

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of tree and shrub savanna. It is constituted by two mandatory stratum that defines the overall class structure. First strata is constituted by one basic element herbaceous growth forms. Second strata of basic element woody growth forms is present

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| CF | D0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 | height 80.0–300.0 | LC_VegetationArtificialityCharacteristic |
| CF | D3 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 4.0–20.0 | height 1.0–10.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `CE`.
