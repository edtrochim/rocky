---
id: registry:L37:Zh
kind: class
title: Zh Wetland
system: registry:L37
code: Zh
name: Wetland
status: registered
decomposed: true
file_class_id: '111'
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Zh Wetland

## Definition (verbatim, FAO LCLR)

These are low-lying lands generally flooded during the rainy season. Sparsely forested areas, partially, temporarily or permanently saturated with stagnant or running water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 112 | 113 Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `111`.
