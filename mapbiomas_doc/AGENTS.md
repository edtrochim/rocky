# Agent Guide: MapBiomas Annual Land Cover and Land Use, South America

Read this before you query the catalog. Every number here is measured from the
STAC objects in this catalog or from a listing of the bucket. Nothing is
quoted from memory.

Machine entry point: <https://data.source.coop/tristangruppwri/mapbiomas/catalog.json>
Human entry point: <https://source.coop/tristangruppwri/mapbiomas>
Source repository: <https://github.com/wri/rural-land>

## What This Is

Annual land cover and land use maps from the MapBiomas Project for ten South American countries, 2019-2024, as Cloud-Optimized GeoTIFFs at 30 m. One collection per country, one item per year. Pixel values are the raw national MapBiomas class codes - nothing was reclassified. Because each MapBiomas national initiative maintains its own legend, codes are not comparable across borders as published; the README documents a three-tier harmonisation (exact level-1 collapse, a pan-MapBiomas legend, and a corrected crosswalk onto MapBiomas Brazil Collection 10) and ships it as a machine-readable harmonization.csv.

The catalog is a mirror. MapBiomas produces the maps and licenses them. Source
Cooperative serves the files. See `providers` on any collection.

## Shape

| collection | items | years | class codes in the legend |
|---|---|---|---|
| `mapbiomas-argentina` | 6 | 2019-2024 | 21 |
| `mapbiomas-bolivia` | 6 | 2019-2024 | 30 |
| `mapbiomas-brazil` | 6 | 2019-2024 | 38 |
| `mapbiomas-chile` | 6 | 2019-2024 | 29 |
| `mapbiomas-colombia` | 6 | 2019-2024 | 31 |
| `mapbiomas-ecuador` | 6 | 2019-2024 | 27 |
| `mapbiomas-paraguay` | 5 | 2019-2023 | 14 |
| `mapbiomas-peru` | 6 | 2019-2024 | 33 |
| `mapbiomas-uruguay` | 6 | 2019-2024 | 17 |
| `mapbiomas-venezuela` | 6 | 2019-2024 | 31 |
| `provenance` | 0 | - | 0 |

11 collections, 59 items. One item per country-year.
One Cloud-Optimized GeoTIFF per item, at 30 m in EPSG:4326, `uint8`, nodata 0.

## The One Thing That Breaks Analyses

**The same integer means different things in different countries.** Code `4` is
Savanna Formation in Brazil and Open forests in Argentina. Code `50` is
Herbaceous Sandbank Vegetation in Brazil and Xerophytic grassland in Venezuela.
Code `63` is Shrub and herbaceous mosaic in Argentina and Steppe in Chile.

Never compare raw codes across collections. Bolivia and Chile also change
MapBiomas collection part way through their own year range, so their years are
not comparable to each other either.

Three crosswalks are published, one exact and two lossy, in
<https://data.source.coop/tristangruppwri/mapbiomas/provenance/harmonization.csv>. The catalog README explains which
tier to use. Apply one before any cross-country statistic.

## Reading a Pixel

Every COG embeds the official MapBiomas colour table for its country, and one
`CLASS_<code>` TIFF tag per legend entry, so the file is self-describing. The
same legend is in the STAC as `classification:classes` on the data asset's
band, with `color_hint` carrying the official colour. Use that rather than a
palette of your own.

```python
import rasterio

url = ("https://data.source.coop/tristangruppwri/mapbiomas/"
       "mapbiomas-uruguay/mapbiomas_uruguay_2024/mapbiomas_uruguay_2024.tif")
with rasterio.open(url) as src:
    window = rasterio.windows.Window(0, 0, 512, 512)
    block = src.read(1, window=window)
    names = {k: v for k, v in src.tags().items() if k.startswith("CLASS_")}
```

The bucket answers range requests, so a windowed read fetches only the tiles it
needs. It does not need credentials.

## Before You Query

Check `tools/availability.py` in the source repository, or the Availability
section of the catalog README. Some declared rasters are not in the bucket yet
and return HTTP 404.

## Conformance

Portolan profile https://schemas.portolan-sdi.org/portolan/v0.1.2/schema.json. Validated with rashid 0.1.7. Known
deviations are listed in `docs/conformance.md` in the source repository, each
with the reason it stands.
