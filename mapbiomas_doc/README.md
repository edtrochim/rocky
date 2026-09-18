# MapBiomas Annual Land Cover and Land Use, South America (2019-2024)

![mapbiomas](https://img.shields.io/badge/mapbiomas-blue) ![land cover](https://img.shields.io/badge/land_cover-blue) ![land use](https://img.shields.io/badge/land_use-blue) ![south america](https://img.shields.io/badge/south_america-blue) ![cloud-optimized geotiff](https://img.shields.io/badge/cloud--optimized_geotiff-blue) ![landsat](https://img.shields.io/badge/landsat-blue) ![agriculture](https://img.shields.io/badge/agriculture-blue) ![deforestation](https://img.shields.io/badge/deforestation-blue) ![annual land cover](https://img.shields.io/badge/annual_land_cover-blue) ![30m](https://img.shields.io/badge/30m-blue)

Annual land cover and land use maps from the MapBiomas Project for ten South American countries, 2019-2024, as Cloud-Optimized GeoTIFFs at 30 m. One collection per country, one item per year. Pixel values are the raw national MapBiomas class codes - nothing was reclassified. Because each MapBiomas national initiative maintains its own legend, codes are not comparable across borders as published; the README documents a three-tier harmonisation (exact level-1 collapse, a pan-MapBiomas legend, and a corrected crosswalk onto MapBiomas Brazil Collection 10) and ships it as a machine-readable harmonization.csv.

## Collections

### [MapBiomas Argentina — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-argentina/)

MapBiomas annual land cover and land use for Argentina, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Argentina MapBiomas class codes with no recla...

### [MapBiomas Bolivia — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-bolivia/)

MapBiomas annual land cover and land use for Bolivia, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Bolivia MapBiomas class codes with no reclassif...

### [MapBiomas Brazil — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-brazil/)

MapBiomas annual land cover and land use for Brazil, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Brazil MapBiomas class codes with no reclassific...

### [MapBiomas Chile — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-chile/)

MapBiomas annual land cover and land use for Chile, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Chile MapBiomas class codes with no reclassificat...

### [MapBiomas Colombia — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-colombia/)

MapBiomas annual land cover and land use for Colombia, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Colombia MapBiomas class codes with no reclass...

### [MapBiomas Ecuador — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-ecuador/)

MapBiomas annual land cover and land use for Ecuador, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Ecuador MapBiomas class codes with no reclassif...

### [MapBiomas Paraguay — annual land cover and land use, 2019-2023](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-paraguay/)

MapBiomas annual land cover and land use for Paraguay, 2019-2023, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Paraguay MapBiomas class codes with no reclass...

### [MapBiomas Peru — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-peru/)

MapBiomas annual land cover and land use for Peru, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Peru MapBiomas class codes with no reclassificatio...

### [MapBiomas Uruguay — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-uruguay/)

MapBiomas annual land cover and land use for Uruguay, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Uruguay MapBiomas class codes with no reclassif...

### [MapBiomas Venezuela — annual land cover and land use, 2019-2024](https://source.coop/tristangruppwri/mapbiomas/mapbiomas-venezuela/)

MapBiomas annual land cover and land use for Venezuela, 2019-2024, at 30 m in EPSG:4326, one Cloud-Optimized GeoTIFF per year. Pixel values are the raw Venezuela MapBiomas class codes with no recla...

### [Provenance — legends, harmonisation tables and build scripts](https://source.coop/tristangruppwri/mapbiomas/provenance/)

The machine-readable tables the catalog README refers to, and the scripts that build this catalog from the raw MapBiomas country exports. `legends.json` holds the official legend for each of the te...

## Coverage

**Spatial Extent**

- West: -92.0947, South: -57.2646, East: -32.3922, North: 14.0148

**Temporal Extent**

- 2019-01-01 to 2024-12-31

## Source

[https://mapbiomas.org](https://mapbiomas.org)

## Processing Notes

## What was done to the data

Source GeoTIFFs were exported per country and year from the MapBiomas platform
and converted to Cloud-Optimized GeoTIFFs. **Pixel values were not changed. No
reclassification was applied to any raster.** The harmonisation described below
is documentation - apply it yourself, at analysis time, to the tier you need.

The conversion uses the Portolan CLI's shipped COG defaults with one deliberate
deviation and three additions:

| setting | value | |
|---|---|---|
| compression | DEFLATE, predictor 2 | Portolan default |
| internal tiles | 512 x 512 | Portolan default |
| overview resampling | `mode` | **deviation** - Portolan defaults to `nearest`; these are categorical maps, where the modal class is the meaningful downsample |
| data type | uint8 | **addition** - every observed class code is below 256; the full-resolution maximum was verified on each non-uint8 source before casting, so the cast is lossless |
| nodata | 0 | **addition** - 0 is background/outside-country in every source raster |
| colour table | official MapBiomas palette for the country | **addition** - files render correctly on open in QGIS and ArcGIS |
| class names | TIFF tags `CLASS_<code>` | **addition** - the legend travels with the file |

Provenance tags written into every COG: `MAPBIOMAS_COUNTRY`, `MAPBIOMAS_YEAR`,
`MAPBIOMAS_COLLECTION`, `MAPBIOMAS_LEGEND_SOURCE`, `SOURCE_FILE`,
`OVERVIEW_RESAMPLING`, and one `CLASS_<code>` tag per legend entry.

## Which MapBiomas collection is each country?

MapBiomas is not one map. It is a federation of national initiatives, each
publishing its own collection on its own schedule with its own legend. The
collection version was not assumed - it was established for each country by
testing which published legend contains the class codes that actually occur in
the pixels.

| country | years | MapBiomas collection | how it was established |
|---|---|---|---|
| Argentina | 2019-2024 | **Collection 2** | codes 63, 66, 73 and 77 are Collection 2 legend entries |
| Bolivia | 2019-2023 | **Collection 2** | carries 4, 23, 29, 66 and 68, none of which exist in the Collection 1 legend, and none of 39, 72, 81, 82, which are Collection 3 additions |
| Bolivia | 2024 | **Collection 3** | carries 39, 72, 81 and 82; agriculture code 18 is gone, split into 39 and 72 |
| Brazil | 2019-2024 | **Collection 10** | carries 6 Floodable Forest, introduced in Collection 10, plus 62 Cotton and 75 Photovoltaic; code 13 is absent, as Collection 10 retired it |
| Chile | 2019-2021 | **Collection 1** | none of 59, 60, 63, 67 are present, and 21 Mosaic of uses is, which the Collection 2 legend does not define |
| Chile | 2022 | **Collection 1, with mosaic artefacts** | as 2019-2021, plus a few hundred stray pixels - see known issues |
| Chile | 2023-2024 | **Collection 2** | carries 59, 60, 63 and 67 |
| Colombia | 2019-2024 | **Collection 3** | carries 74 Banana, 75 Solar panel farm, 81 and 82, all Collection 3 additions |
| Ecuador | 2019-2024 | **Collection 3** | carries 74, 81 and 82, none of which are in the Collection 2 legend |
| Paraguay | 2019-2023 | **Collection 2** | stated in the source filenames; every observed code is in the Collection 2 legend |
| Peru | 2019-2024 | **Collection 3** | stated in the source filenames; 70 Fog oasis and 72 Other crops confirm it |
| Uruguay | 2019-2024 | **Collection 3** | carries the 79/80/83 plantation species split introduced in Collection 3 |
| Venezuela | 2019-2024 | **Collection 3** | carries 81 and 82, absent from the Collection 2 legend |

Two countries change collection mid-series, so their own years are not directly
comparable to each other without harmonising first.

## Why harmonisation is needed

The same integer means different things in different countries, and some
integers exist in only one country:

- `4` is *Savanna Formation* in Brazil, *Open forests* in Argentina and Bolivia,
  *Dry forest* in Peru, *Wooded savanna* in Venezuela, *Open Natural Woodlands*
  in Paraguay.
- `50` is *Herbaceous Sandbank Vegetation* in Brazil and Colombia but
  *Xerophytic grassland/shrubland* in Venezuela - the same code for two
  unrelated cover types.
- `63` is *Shrub and herbaceous mosaic* in Argentina but *Steppe* in Chile.
- Andean classes `81`/`82`, shrubland `66`, fog oasis `70`, peatland `73`,
  steppe `63`, salt flat `61`, glacier `34` and the Uruguayan plantation split
  `79`/`80`/`83` have no equivalent at all in the Brazilian legend.
- Uruguay's legend documents agriculture as `19`, but every Uruguayan raster
  encodes it as `18`.

## Three tiers of harmonisation

How much comparability you can get depends on how much detail you are willing
to give up. Rather than one crosswalk, this catalog documents three, and every
class code in every raster has an entry in all three.

### Tier A - MapBiomas level 1 (exact)

Every national legend is a strict hierarchy under the same six parents. Collapsing
to level 1 loses detail but never correctness, and needs no judgement calls. Use
this for any statistic that has to be defensible across all ten countries.

| level-1 code | class |
|---|---|
| 1 | Forest formation |
| 10 | Non-forest natural formation |
| 14 | Farming |
| 22 | Non-vegetated area |
| 26 | Water body |
| 27 | Not observed |

Three caveats, each of which follows the country's own published hierarchy
rather than being silently forced:

- Peru files code 32 (Coastal salt flat) under level-1 22 Non-vegetated area, while Brazil, Colombia and Venezuela file the same code (Hypersaline tidal flat) under level-1 10 Non-forest natural formation. Tier A follows each country's own published hierarchy rather than forcing one of the two.
- Uruguay's code 3 is 'Closed forest and closed shrubland', so Uruguayan level-1 Forest includes shrubland that other countries would place under level-1 10 Non-forest natural formation.
- Code 4 is Savanna Formation in Brazil, Open forest in Argentina, Bolivia and Ecuador, Dry forest in Peru, Wooded savanna in Venezuela and Open Natural Woodlands in Paraguay. All six sit under level-1 1 Forest formation, so Tier A is unaffected; Tier B keeps the code with this caveat attached.

### Tier B - pan-MapBiomas legend (~50 classes)

Most non-Brazilian codes already mean the same thing in every country that
publishes them: `13`, `29`, `61`, `66`, `68`, `81`, `82`, `34` are consistent
across the Andean and Southern Cone legends. Tier B keeps those codes as
published and only resolves genuine collisions:

- Venezuela `50` (xerophytic shrubland) → `66` Shrubland, so it stops colliding
  with Brazil's and Colombia's `50` herbaceous sandbank vegetation.
- Argentina `77` (open shrubland) → `66`, merging Argentina's closed/open
  shrubland split into the single shrubland class the other legends use.
- Argentina `63` (shrub-herbaceous mosaic) → `66`, leaving `63` to mean Chile's
  Steppe unambiguously.
- Uruguay `19` → `18`, matching what the Uruguayan rasters actually encode.
- Chile `7` and `16` → `27` Not observed; they are mosaic artefacts, not classes.

Tier B is the right target for continental work that needs real thematic
resolution. Its cost is that no single country emits the full legend: Brazil
never emits Andean classes, the Andean countries never emit Brazil's crop split.

### Tier C - MapBiomas Brazil Collection 10 (corrected)

This is the target the Trazo Fields extraction pipeline
(`extract_hansen_mapbiomas_v16.Rmd`) uses. The version of the crosswalk in that
script drops 30 class codes into `27 Not Observed` without saying so, and treats
Colombia and Venezuela as Brazil-compatible passthroughs when seven of their
codes have no Brazilian meaning. The table below is the corrected version.

Two rules were applied. **No code falls through to 27** - `27` means "MapBiomas
could not observe this pixel" and nothing else. **No fold may change a pixel's
Tier A class** - that is what forces shrubland to `12` Grassland rather than `4`
Savanna Formation (`4` sits under level-1 Forest, so the other choice would
reclassify shrubland as forest and inflate forest area across five countries),
and glacier to `33` rather than `25`.

Lossy folds, applied identically in every country:

| Tier B code | class | → | Brazil C10 | why, and what is lost |
|---|---|---|---|---|
| 13 | Other non-forest natural formation | → | 12 Grassland | Brazil Collection 10 dropped 'Other non-forest natural formation'. Folded into 12 Grassland, which shares its level-1 parent (10). |
| 34 | Glacier, ice and permanent snow | → | 33 River, Lake and Ocean | Brazil Collection 10 has no glacier class. Folded into 33 River, Lake and Ocean because every national legend files glacier under level-1 26 Water body; folding to 25 instead would move the pixels to level-1 22 Non-vegetated. |
| 59 | ? | → | 3 Forest Formation | Brazil Collection 10 does not separate primary from secondary forest. Folded into 3 Forest Formation; level-1 parent (1) is preserved. |
| 60 | ? | → | 3 Forest Formation | As for 59. |
| 61 | Salt flat (salar) | → | 25 Other non Vegetated Areas | No salt flat class in Brazil. Folded into 25 Other non Vegetated Areas; level-1 parent (22) is preserved. |
| 63 | Steppe | → | 12 Grassland | No steppe class in Brazil. Folded into 12 Grassland; level-1 parent (10) is preserved. |
| 66 | Shrubland | → | 12 Grassland | Argentina's 63 is a shrub-and-herbaceous mosaic; Chile's 63 is Steppe. Merged into 66 Shrubland for Argentina to avoid the collision, and 63 is reserved for Chile's Steppe. No shrubland class in Brazil. Folded into 12 Grassland rather than 4 Savanna Formation: 4 sits under level-1 1 Forest, so mapping shrubland there would reclassify it as forest and inflate forest area across Chile, Argentina, Peru, Bolivia and Venezuela. |
| 67 | ? | → | 4 Savanna Formation | No dwarf/krummholz forest class in Brazil. Folded into 4 Savanna Formation, the Brazilian open-canopy woody class; level-1 parent (1 Forest) is preserved. |
| 68 | Other natural non-vegetated area | → | 25 Other non Vegetated Areas | No 'other natural non-vegetated area' class in Brazil. Folded into 25; level-1 parent (22) is preserved. |
| 70 | Fog oasis (loma) | → | 12 Grassland | No fog oasis (loma) class in Brazil. Folded into 12 Grassland; level-1 parent (10) is preserved. |
| 72 | Other crops | → | 41 Other Temporary Crops | 'Other crops' in Bolivia and Peru is not resolved to a crop cycle. Folded into 41 Other Temporary Crops, the Brazilian catch-all; level-1 parent (14) is preserved. |
| 73 | Peatland | → | 11 Wetland | No peatland class in Brazil. Folded into 11 Wetland; level-1 parent (10) is preserved. |
| 74 | Banana | → | 48 Other Perennial Crops | No banana class in Brazil. Banana is a perennial crop, so it folds into 48 Other Perennial Crops; level-1 parent (14) is preserved. The Rmd previously sent it to 41 Other Temporary Crops, which is the wrong crop cycle. |
| 79 | Forest plantation - pine | → | 9 Forest Plantation | Brazil does not split forest plantation by species. Folded into 9 Forest Plantation, its own parent class - detail is lost but no class boundary is crossed. |
| 80 | Forest plantation - eucalyptus | → | 9 Forest Plantation | As for 79. |
| 81 | Andean grassland and shrubland | → | 12 Grassland | No Andean grassland/shrubland class in Brazil. Folded into 12 Grassland; level-1 parent (10) is preserved. This is a large share of the Bolivian, Peruvian, Ecuadorian and Colombian highlands - flag it in any highland analysis. |
| 82 | Flooded Andean grassland and shrubland | → | 11 Wetland | No flooded Andean grassland/shrubland class in Brazil. Folded into 11 Wetland; level-1 parent (10) is preserved. |
| 83 | Forest plantation - other species | → | 9 Forest Plantation | As for 79. |

### Per-country tables

#### Argentina

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Closed forests | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Open forests | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 6 | Flooded forests | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Forest plantations | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Flooded grasslands | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grasslands | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 15 | Pastures | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 19 | Temporary crops | 14 Farming | 19 Temporary crop | 19 Temporary Crop | exact |
| 21 | Agriculture and pasture mosaic | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 24 | Urban areas | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non-vegetated areas | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 27 | Not observed | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 33 | Rivers, lakes or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Ice and permanent snow | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 36 | Perennial crops | 14 Farming | 36 Perennial crop | 36 Perennial Crop | exact |
| 63 | Shrubs and herbaceous mosaic | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 66 | Closed shrublands | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 73 | Peatlands | 10 Non-forest natural formation | 73 Peatland | 11 Wetland | **lossy** |
| 77 | Open shrublands | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |

#### Bolivia

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Open forest | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 6 | Flooded forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 11 | Flooded grassland/shrubland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland/shrubland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non-forest natural formation | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 18 | Agriculture | 14 Farming | 18 Agriculture | 18 Agriculture | exact |
| 21 | Mosaic of uses | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach, dune and sand spot | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Urban infrastructure | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non-vegetated anthropic area | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 27 | Not observed | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 29 | Rocky outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 33 | River, lake | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Glacier | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 39 | Soybean (beta) | 14 Farming | 39 Soybean | 39 Soybean | exact |
| 61 | Salt flat | 22 Non-vegetated area | 61 Salt flat (salar) | 25 Other non Vegetated Areas | **lossy** |
| 66 | Scrublands | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 68 | Other non-vegetated natural area | 22 Non-vegetated area | 68 Other natural non-vegetated area | 25 Other non Vegetated Areas | **lossy** |
| 72 | Other crops | 14 Farming | 72 Other crops | 41 Other Temporary Crops | **lossy** |
| 81 | Andean grassland and shrubland | 10 Non-forest natural formation | 81 Andean grassland and shrubland | 12 Grassland | **lossy** |
| 82 | Flooded Andean grassland and shrubland | 10 Non-forest natural formation | 82 Flooded Andean grassland and shrubland | 11 Wetland | **lossy** |

#### Brazil

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest Formation | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Savanna Formation | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 5 | Mangrove | 1 Forest formation | 5 Mangrove | 5 Mangrove | exact |
| 6 | Floodable Forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Forest Plantation | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Wetland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 20 | Sugar cane | 14 Farming | 20 Sugar cane | 20 Sugar cane | exact |
| 21 | Mosaic of Uses | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach, Dune and Sand Spot | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Urban Area | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non Vegetated Areas | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 29 | Rocky Outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 32 | Hypersaline Tidal Flat | 10 Non-forest natural formation | 32 Hypersaline tidal flat / coastal salt flat | 32 Hypersaline Tidal Flat | exact |
| 33 | River, Lake and Ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 35 | Palm Oil | 14 Farming | 35 Palm oil | 35 Palm Oil | exact |
| 39 | Soybean | 14 Farming | 39 Soybean | 39 Soybean | exact |
| 40 | Rice | 14 Farming | 40 Rice | 40 Rice | exact |
| 41 | Other Temporary Crops | 14 Farming | 41 Other temporary crops | 41 Other Temporary Crops | exact |
| 46 | Coffee | 14 Farming | 46 Coffee | 46 Coffee | exact |
| 47 | Citrus | 14 Farming | 47 Citrus | 47 Citrus | exact |
| 48 | Other Perennial Crops | 14 Farming | 48 Other perennial crops | 48 Other Perennial Crops | exact |
| 49 | Wooded Sandbank Vegetation | 1 Forest formation | 49 Wooded sandbank vegetation | 49 Wooded Sandbank Vegetation | exact |
| 50 | Herbaceous Sandbank Vegetation | 10 Non-forest natural formation | 50 Herbaceous sandbank vegetation | 50 Herbaceous Sandbank Vegetation | exact |
| 62 | Cotton (beta) | 14 Farming | 62 Cotton | 62 Cotton (beta) | exact |
| 75 | Photovoltaic Power Plant (beta) | 22 Non-vegetated area | 75 Photovoltaic power plant | 75 Photovoltaic Power Plant (beta) | exact |

#### Chile

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Open forest (pan-MapBiomas standard code; not in the Chile Collection 2 legend) | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 6 | Flooded forest (pan-MapBiomas standard code; not in the Chile Collection 2 legend) | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 7 | (not in the published national legend) | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 9 | Silviculture | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Wetland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non-forest natural formation (pan-MapBiomas standard code; not in the Chile Collection 2 legend) | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 16 | (not in the published national legend) | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 18 | Agriculture | 14 Farming | 18 Agriculture | 18 Agriculture | exact |
| 21 | Mosaic of uses (pan-MapBiomas standard code; not in the Chile Collection 2 legend) | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach, Dune and Sand Spot | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Infrastructure | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non-vegetated area | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 29 | Rocky Outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 32 | Hypersaline tidal flat (pan-MapBiomas standard code; not in the Chile Collection 2 legend) | 10 Non-forest natural formation | 32 Hypersaline tidal flat / coastal salt flat | 32 Hypersaline Tidal Flat | exact |
| 33 | River, lake or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Ice and snow | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 59 | Primary Forest | 1 Forest formation | 59 ? | 3 Forest Formation | **lossy** |
| 60 | Secondary Forest | 1 Forest formation | 60 ? | 3 Forest Formation | **lossy** |
| 61 | Salt Flat | 22 Non-vegetated area | 61 Salt flat (salar) | 25 Other non Vegetated Areas | **lossy** |
| 63 | Steppe | 10 Non-forest natural formation | 63 Steppe | 12 Grassland | **lossy** |
| 66 | Shrubland | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 67 | Dwarf forest | 1 Forest formation | 67 ? | 4 Savanna Formation | **lossy** |

#### Colombia

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 5 | Mangrove | 1 Forest formation | 5 Mangrove | 5 Mangrove | exact |
| 6 | Flooded forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Forest plantation | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Wetland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grasslands / herbaceous | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non forest formation | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 21 | Mosaic of agriculture and pasture | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach, dune and sand spot | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Infrastructure | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non-vegetated area | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 27 | Not observed | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 29 | Rocky outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 32 | Hypersaline tidal flat | 10 Non-forest natural formation | 32 Hypersaline tidal flat / coastal salt flat | 32 Hypersaline Tidal Flat | exact |
| 33 | River, lake or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Glacier | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 35 | Palm oil | 14 Farming | 35 Palm oil | 35 Palm Oil | exact |
| 49 | Wooded sand vegetation | 1 Forest formation | 49 Wooded sandbank vegetation | 49 Wooded Sandbank Vegetation | exact |
| 50 | Herbaceous sand vegetation | 10 Non-forest natural formation | 50 Herbaceous sandbank vegetation | 50 Herbaceous Sandbank Vegetation | exact |
| 68 | Other natural non-vegetated area | 22 Non-vegetated area | 68 Other natural non-vegetated area | 25 Other non Vegetated Areas | **lossy** |
| 74 | Banana (beta) | 14 Farming | 74 Banana | 48 Other Perennial Crops | **lossy** |
| 75 | Solar panel farm | 22 Non-vegetated area | 75 Photovoltaic power plant | 75 Photovoltaic Power Plant (beta) | exact |
| 81 | Andean Herbaceous and Shrubby Vegetation | 10 Non-forest natural formation | 81 Andean grassland and shrubland | 12 Grassland | **lossy** |
| 82 | Flooded Andean Herbaceous and Shrubby Vegetation | 10 Non-forest natural formation | 82 Flooded Andean grassland and shrubland | 11 Wetland | **lossy** |

#### Ecuador

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Open Forest | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 5 | Mangrove | 1 Forest formation | 5 Mangrove | 5 Mangrove | exact |
| 6 | Floodable forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Silviculture | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Non forest wetland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non-forest natural formation | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 21 | Mosaic of uses | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach, dune and sand spot | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Urban infrastructure | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other anthropic non-vegetated area | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 27 | Not observed | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 29 | Rocky Outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 33 | River, Lake or Ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Glacier | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 68 | Other natural non-vegetated area | 22 Non-vegetated area | 68 Other natural non-vegetated area | 25 Other non Vegetated Areas | **lossy** |
| 74 | Banana (beta) | 14 Farming | 74 Banana | 48 Other Perennial Crops | **lossy** |
| 81 | Andean Herbaceous and Shrubby Vegetation | 10 Non-forest natural formation | 81 Andean grassland and shrubland | 12 Grassland | **lossy** |
| 82 | Flooded Andean Herbaceous | 10 Non-forest natural formation | 82 Flooded Andean grassland and shrubland | 11 Wetland | **lossy** |

#### Paraguay

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Closed Natural Woodlands | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Open Natural Woodlands | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 6 | Flooded Natural Woodlands | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Forest Plantation | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Flooded grasslands | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 18 | Agriculture | 14 Farming | 18 Agriculture | 18 Agriculture | exact |
| 22 | Non-vegetated area | 22 Non-vegetated area | 22 Non-vegetated area (aggregate) | 22 Non vegetated area | exact |
| 26 | Water body | 26 Water body | 26 Water body (aggregate) | 26 Water | exact |

#### Peru

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Dry forest | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 5 | Mangrove | 1 Forest formation | 5 Mangrove | 5 Mangrove | exact |
| 6 | Flooded forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Planted forest | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Swamp or Flooded Grassland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grasslands / herbaceous | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non-forest formations | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 21 | Mosaic of agriculture and pasture | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Infrastructure | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non vegetated area | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 27 | Not observed | 27 Not observed | 27 Not observed | 27 Not Observed | exact |
| 29 | Rocky Outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 32 | Coastal Salt flat | 22 Non-vegetated area | 32 Hypersaline tidal flat / coastal salt flat | 32 Hypersaline Tidal Flat | exact |
| 33 | River, lake or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 34 | Glacier | 26 Water body | 34 Glacier, ice and permanent snow | 33 River, Lake and Ocean | **lossy** |
| 35 | Oil palm | 14 Farming | 35 Palm oil | 35 Palm Oil | exact |
| 40 | Rice | 14 Farming | 40 Rice | 40 Rice | exact |
| 61 | Salt flat | 22 Non-vegetated area | 61 Salt flat (salar) | 25 Other non Vegetated Areas | **lossy** |
| 66 | Scrubland | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 68 | Other natural non vegetated area | 22 Non-vegetated area | 68 Other natural non-vegetated area | 25 Other non Vegetated Areas | **lossy** |
| 70 | Fog oasis | 10 Non-forest natural formation | 70 Fog oasis (loma) | 12 Grassland | **lossy** |
| 72 | Other crops | 14 Farming | 72 Other crops | 41 Other Temporary Crops | **lossy** |

#### Uruguay

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Closed forest and closed shrubland | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 11 | Wetland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 15 | Pasture | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 18 | Agriculture (code used by the rasters in place of the legend's code 19; color from the pan-MapBiomas standard palette) | 14 Farming | 18 Agriculture | 18 Agriculture | exact |
| 22 | Non-vegetated area | 22 Non-vegetated area | 22 Non-vegetated area (aggregate) | 22 Non vegetated area | exact |
| 33 | River, lake or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 79 | Pinus plantation | 14 Farming | 79 Forest plantation - pine | 9 Forest Plantation | **lossy** |
| 80 | Eucaliptus plantation | 14 Farming | 80 Forest plantation - eucalyptus | 9 Forest Plantation | **lossy** |
| 83 | Other types of forest plantation | 14 Farming | 83 Forest plantation - other species | 9 Forest Plantation | **lossy** |

#### Venezuela

| code | national class | Tier A | Tier B | Tier C (Brazil C10) | Tier C loss |
|---|---|---|---|---|---|
| 3 | Forest | 1 Forest formation | 3 Forest | 3 Forest Formation | exact |
| 4 | Wooded savanna | 1 Forest formation | 4 Open / dry forest or savanna formation | 4 Savanna Formation | exact |
| 5 | Mangrove | 1 Forest formation | 5 Mangrove | 5 Mangrove | exact |
| 6 | Flooded forest | 1 Forest formation | 6 Flooded forest | 6 Floodable Forest | exact |
| 9 | Forest plantation | 14 Farming | 9 Forest plantation | 9 Forest Plantation | exact |
| 11 | Flooded grassland/shrubland | 10 Non-forest natural formation | 11 Wetland / flooded herbaceous | 11 Wetland | exact |
| 12 | Grassland | 10 Non-forest natural formation | 12 Grassland / herbaceous | 12 Grassland | exact |
| 13 | Other non-forest natural formations | 10 Non-forest natural formation | 13 Other non-forest natural formation | 12 Grassland | **lossy** |
| 15 | Pasture/Fallow lands | 14 Farming | 15 Pasture | 15 Pasture | exact |
| 18 | Agriculture/Fallow lands | 14 Farming | 18 Agriculture | 18 Agriculture | exact |
| 21 | Cropland/Pasture/Fallow lands | 14 Farming | 21 Mosaic of uses | 21 Mosaic of Uses | exact |
| 23 | Beach or dune | 22 Non-vegetated area | 23 Beach, dune and sand spot | 23 Beach, Dune and Sand Spot | exact |
| 24 | Urban | 22 Non-vegetated area | 24 Urban / infrastructure | 24 Urban Area | exact |
| 25 | Other non-vegetated anthropic areas | 22 Non-vegetated area | 25 Other non-vegetated area | 25 Other non Vegetated Areas | exact |
| 29 | Rocky outcrop | 10 Non-forest natural formation | 29 Rocky outcrop | 29 Rocky Outcrop | exact |
| 30 | Mining | 22 Non-vegetated area | 30 Mining | 30 Mining | exact |
| 31 | Aquaculture | 26 Water body | 31 Aquaculture | 31 Aquaculture | exact |
| 32 | Hypersaline tidal flat | 10 Non-forest natural formation | 32 Hypersaline tidal flat / coastal salt flat | 32 Hypersaline Tidal Flat | exact |
| 33 | River, lake or ocean | 26 Water body | 33 River, lake or ocean | 33 River, Lake and Ocean | exact |
| 50 | Xerophytic grassland/shrubland | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 66 | Shrubland | 10 Non-forest natural formation | 66 Shrubland | 12 Grassland | **lossy** |
| 68 | Other non-vegetated natural areas | 22 Non-vegetated area | 68 Other natural non-vegetated area | 25 Other non Vegetated Areas | **lossy** |
| 81 | Andean herbaceous/shrubby vegetation | 10 Non-forest natural formation | 81 Andean grassland and shrubland | 12 Grassland | **lossy** |
| 82 | Flooded andean herbaceous/shrubby vegetation | 10 Non-forest natural formation | 82 Flooded Andean grassland and shrubland | 11 Wetland | **lossy** |


## Applying it

The full table is published as a machine-readable asset,
`provenance/harmonization.csv`, with columns `country, code, national_class,
tier_a_code, tier_a_class, tier_b_code, tier_b_class, tier_b_note, tier_c_code,
tier_c_class, tier_c_lossy, tier_c_note`.

```python
import csv
import numpy as np
import rasterio

TIER = "tier_c_code"          # or tier_a_code / tier_b_code
COUNTRY = "uruguay"

lut = np.zeros(256, dtype="uint8")        # 0 stays 0 (nodata)
for row in csv.DictReader(open("provenance/harmonization.csv", encoding="utf-8")):
    if row["country"] == COUNTRY:
        lut[int(row["code"])] = int(row[TIER])

path = ("https://data.source.coop/tristangruppwri/mapbiomas/"
        "mapbiomas-uruguay/mapbiomas_uruguay_2024/mapbiomas_uruguay_2024.tif")
with rasterio.open(path) as src:
    harmonised = lut[src.read(1)]
```

Anything not listed for a country stays 0, which is nodata - so an unexpected
code shows up as a hole rather than as a silently wrong class.

## Known issues and caveats

- **Legends differ between countries, and for Bolivia and Chile between years
  within the same country.** Never compare raw codes across collections. See the
  collection table and the three harmonisation tiers above.
- **Chile 2022 contains mosaic artefacts.** Codes `4`, `6`, `7`, `13`, `16` and
  `32` occur at 1-3 pixels each in a 1-in-16 sample, against hundreds of
  thousands of pixels for every real class. Their values fall between adjacent
  real codes (`7` between `6` and `9`, `16` between `15` and `18`, `32` between
  `29` and `34`), which is the signature of a non-nearest resampling during the
  mosaic step upstream of this catalog. Codes `7` and `16` exist in no MapBiomas
  legend at all. Treat all six as no-data for that year.
- **Uruguay encodes agriculture as `18`**, while the published Uruguay
  Collection 3 legend lists agriculture as `19`. No Uruguayan raster contains any
  pixel with value `19`.
- **The Paraguay Collection 2 legend PDF assigns `#ffefc3` to class `9` (Forest
  Plantation)** - the same colour it assigns to the class `14` farming
  aggregate. Every other national legend uses `#7a5900`. The published value is
  reproduced verbatim in the colour tables rather than corrected.
- **Paraguay coverage ends at 2023.** MapBiomas Paraguay had not released a 2024
  collection when these rasters were exported.
- **Codes `4`, `6`, `13`, `21` and `32` occur in Chilean rasters** but are absent
  from the published Chile legends. Names and colours come from the
  pan-MapBiomas standard palette shared by the other national legends.
- **`0` is background, not a class.** It is set as nodata in every COG.
- **Tier C is lossy by construction for the Andes and Patagonia.** Andean
  grassland `81` alone is a large share of the Bolivian, Peruvian, Ecuadorian and
  Colombian highlands, and Tier C folds it into `12` Grassland. Highland analyses
  should use Tier A or Tier B.
- **These rasters are a mirror, not the authoritative source.** MapBiomas
  releases new collections regularly; check mapbiomas.org before assuming these
  are current.


## Availability

**41 of 59 Cloud-Optimized GeoTIFFs are declared here but are not in the bucket.** They return HTTP 404. The upload in July 2026 stopped part way through and the STAC metadata was written for the complete set.

| collection | years served | years missing |
|---|---|---|
| mapbiomas-argentina | 2019, 2020, 2021, 2022, 2023, 2024 | none |
| mapbiomas-bolivia | 2019 | 2020, 2021, 2022, 2023, 2024 |
| mapbiomas-brazil | none | 2019, 2020, 2021, 2022, 2023, 2024 |
| mapbiomas-chile | none | 2019, 2020, 2021, 2022, 2023, 2024 |
| mapbiomas-colombia | none | 2019, 2020, 2021, 2022, 2023, 2024 |
| mapbiomas-ecuador | 2019, 2020, 2021, 2022, 2023 | 2024 |
| mapbiomas-paraguay | none | 2019, 2020, 2021, 2022, 2023 |
| mapbiomas-peru | none | 2019, 2020, 2021, 2022, 2023, 2024 |
| mapbiomas-uruguay | 2019, 2020, 2021, 2022, 2023, 2024 | none |
| mapbiomas-venezuela | none | 2019, 2020, 2021, 2022, 2023, 2024 |

That is 10.80 GiB of raster that a reader cannot fetch yet. The metadata is correct and describes the intended set, so the fix is to upload the remaining files, not to change the metadata.

Re-measure this table at any time:

```bash
python3 tools/availability.py --refresh
```

## Citation

MapBiomas Project — annual land cover and land use collections for Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Paraguay, Peru, Uruguay and Venezuela. Accessed through https://mapbiomas.org. Republished as Cloud-Optimized GeoTIFFs with the raw national legends preserved.

## Attribution

MapBiomas Project (mapbiomas.org), CC-BY-SA 4.0. Each country map is produced by the corresponding MapBiomas national initiative.

## License

[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

*Generated by [Portolan](https://github.com/portolan-sdi/portolan-cli) from STAC metadata and .portolan/metadata.yaml*
