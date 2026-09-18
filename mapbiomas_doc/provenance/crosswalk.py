"""Reproduce the MapBiomas harmonisation crosswalk used in
`extract_hansen_mapbiomas_v16.Rmd` and audit it against the class codes that
actually occur in the rasters.

The crosswalk maps each national MapBiomas legend onto the MapBiomas Brazil
Collection 10 legend, which the Rmd pipeline uses as the common reference so
pixel pools from neighbouring countries can be merged for continental analysis.

Outputs:
  crosswalk.csv   country, source_code, source_class, target_code, target_class
  gaps.json       codes observed in the rasters that the crosswalk does not map
"""

from __future__ import annotations

import csv
import json
import os

BUILD = os.path.dirname(os.path.abspath(__file__))
LEGENDS = json.load(open(os.path.join(BUILD, "legends.json"), encoding="utf-8"))
OBSERVED = json.load(open(os.path.join(BUILD, "observed_classes.json"), encoding="utf-8"))

# --- crosswalk tables, transcribed from extract_hansen_mapbiomas_v16.Rmd ------
# Brazil is the reference legend, so it and the two countries the Rmd treats as
# natively Brazil-compatible have no reclassification table.

RCL = {
    "brazil": None,
    "colombia": None,   # Rmd: "Colombia uses Brazil-compatible codes natively"
    "venezuela": None,  # Rmd: "Venezuela uses Brazil-compatible codes natively"
    "peru": dict(zip(
        [1, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 18, 21, 23, 24, 25, 26, 29, 30, 31, 32, 33,
         34, 35, 40, 61, 66, 68, 70, 72, 27],
        [3, 3, 4, 5, 6, 12, 11, 12, 12, 14, 15, 18, 21, 23, 24, 25, 33, 29, 30, 31, 32, 33,
         34, 35, 40, 25, 12, 25, 12, 41, 27])),
    "bolivia": dict(zip(
        [1, 3, 4, 5, 6, 10, 11, 12, 13, 15, 18, 19, 20, 21, 24, 25, 27, 29, 30, 31, 32, 33,
         34, 35, 36, 39, 40, 9, 61, 66, 68, 72, 81, 82],
        [3, 3, 4, 5, 6, 12, 11, 12, 3, 15, 18, 41, 20, 21, 24, 25, 27, 29, 30, 31, 32, 33,
         34, 35, 48, 39, 40, 9, 25, 12, 25, 41, 12, 11])),
    "paraguay": dict(zip(
        [3, 4, 5, 9, 11, 12, 15, 18, 19, 21, 24, 27, 33, 39],
        [3, 4, 5, 9, 11, 12, 15, 18, 41, 21, 24, 27, 33, 39])),
    "argentina": dict(zip(
        [3, 4, 5, 9, 11, 12, 15, 18, 19, 20, 21, 24, 25, 27, 29, 30, 32, 33, 34, 36, 39, 41,
         48, 49, 50, 63, 66, 73, 77],
        [3, 4, 5, 9, 11, 12, 15, 18, 41, 20, 21, 24, 25, 27, 29, 30, 32, 33, 34, 48, 39, 41,
         48, 49, 50, 12, 4, 11, 4])),
    "ecuador": dict(zip(
        [3, 4, 5, 6, 9, 11, 12, 13, 15, 18, 19, 21, 24, 27, 29, 30, 32, 33, 34, 35, 36, 39,
         40, 41, 68, 74, 81, 82],
        [3, 4, 5, 6, 9, 11, 12, 12, 15, 18, 41, 21, 24, 27, 29, 30, 32, 33, 34, 35, 48, 39,
         40, 41, 25, 41, 12, 11])),
    "uruguay": dict(zip(
        [3, 9, 11, 12, 15, 21, 24, 27, 33, 39, 41],
        [3, 9, 11, 12, 15, 21, 24, 27, 33, 39, 41])),
    "chile": dict(zip(
        [3, 4, 5, 9, 11, 12, 15, 18, 21, 23, 24, 27, 29, 30, 32, 33, 34, 41, 48,
         59, 60, 61, 63, 66, 67],
        [3, 4, 5, 9, 11, 12, 15, 18, 21, 23, 24, 27, 29, 30, 32, 33, 34, 41, 48,
         3, 3, 25, 12, 4, 4])),
}

# Everything the Rmd's `terra::classify(..., others = 27)` does not list falls
# through to 27 = Not Observed.
FALLBACK = 27

BRAZIL = LEGENDS["brazil"]["classes"]


def target_name(code: int) -> str:
    entry = BRAZIL.get(str(code))
    return entry[0] if entry else f"(code {code} is not in the Brazil Collection 10 legend)"


def source_name(country: str, code: int) -> str:
    entry = LEGENDS[country]["classes"].get(str(code))
    return entry[0] if entry else "(not in the published national legend)"


def main() -> None:
    rows = []
    gaps = {}

    for country in sorted(LEGENDS):
        if country.startswith("_"):
            continue
        table = RCL[country]
        observed = sorted({c for f, hist in OBSERVED.items()
                           if f.startswith(country) or country in f
                           for c in map(int, hist)} - {0})

        unmapped = []
        for code in observed:
            if table is None:
                tgt = code
                note = "passthrough (Rmd treats this legend as Brazil-compatible)"
                if str(code) not in BRAZIL:
                    unmapped.append({"code": code, "reason":
                                     "passthrough, but this code has no meaning in the "
                                     "Brazil Collection 10 legend",
                                     "national_class": source_name(country, code)})
            elif code in table:
                tgt = table[code]
                note = ""
            else:
                tgt = FALLBACK
                note = "NOT in the Rmd crosswalk - falls through to 27 Not Observed"
                unmapped.append({"code": code, "reason":
                                 "absent from the crosswalk, silently recoded to 27",
                                 "national_class": source_name(country, code)})
            rows.append({
                "country": country,
                "source_code": code,
                "source_class": source_name(country, code),
                "target_code": tgt,
                "target_class": target_name(tgt),
                "note": note,
            })

        # codes the crosswalk maps but that never occur in the data
        if table:
            never = sorted(set(table) - set(observed))
        else:
            never = []
        gaps[country] = {
            "observed_codes": observed,
            "unmapped_or_mismatched": unmapped,
            "crosswalk_entries_never_observed": never,
        }

    with open(os.path.join(BUILD, "crosswalk.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["country", "source_code", "source_class",
                                          "target_code", "target_class", "note"])
        w.writeheader()
        w.writerows(rows)

    with open(os.path.join(BUILD, "gaps.json"), "w", encoding="utf-8") as f:
        json.dump(gaps, f, indent=1)

    for country, g in gaps.items():
        bad = g["unmapped_or_mismatched"]
        print(f"{country:10s} observed={len(g['observed_codes']):2d} problems={len(bad)}")
        for b in bad:
            print(f"    {b['code']:>3} {b['national_class'][:60]:60s} {b['reason']}")


if __name__ == "__main__":
    main()
