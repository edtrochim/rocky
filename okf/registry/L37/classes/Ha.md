---
id: registry:L37:Ha
kind: class
title: Ha Housing
system: registry:L37
code: Ha
name: Housing
status: registered
decomposed: true
file_class_id: '72'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Building
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Ha Housing

## Definition (verbatim, FAO LCLR)

It is all the infrastructures that house the different human groups. The perception of the habitat in an image is linked to its structure and the nature of the materials used. Housing in urban areas is in the form of a continuous or discontinuous fabric depending on the size of the population and the density of the habitat. This type of housing is made up of well-structured buildings and well-marked roads. This structure is easily perceptible in the image by its blue or other color depending on the colored composition, as well as the geometric shapes of the habitat and the roads. In the case of continuous urban fabric, vegetation is very little present and the coverage of artificial surfaces reaches more than 80% in these places. These types of surfaces are present in the towns of regional and provincial capitals and in the state capital. However, in the case of discontinuous urban fabric, the structure of the habitat is an alternation of artificialized spaces and vegetation. In this case, the artificialized surfaces have a coverage of more than 30% but less than 80%. This structure characterizes the outskirts of the capital, regional and provincial capitals. They also characterize the capitals of departments as well as urban areas in rural areas. As for housing in rural areas, it is dominated by unstructured groupings of buildings. The coverage of artificialized surfaces is less than 30%. This type of habitat is quite diffuse among crops and vegetation so that it is not identifiable in the images. The use of other sources and documents (topographic sheet, database, very high resolution image) is necessary to supplement the information.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 73 | 74 Mandatory | `LC_Building` | Mandatory | 30–80 | construction_material=Hard Material |  |
| 73 | 76 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 73 | 78 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `72`.
