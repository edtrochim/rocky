---
id: skill:compare-systems
kind: guide
title: "Skill: compare-systems"
schema: okf/0.1
name: compare-systems
description: Review the uncertain cells of a mechanical comparison between two systems and explain the differences.
inputs: [system, compare]
tools: [equivalence]
---

# compare-systems

Run `python okf/tools/equivalence.py --a <system> --b <other>` first. It writes
`comparisons/<a>__<b>.md` with the best match per class from element sets and cover ranges, and a
`.json` with every cell. Cells marked `same_physical_as` and `disjoint_from` need no review. Review the
`overlaps` and `undecided` cells.

## For each reviewed cell decide

- `same_physical_as`: the rows differ only in wording, a stated versus unstated range, or a characteristic
  that the other system does not record. Say which.
- `overlaps`: the classes share elements but one is broader (say which, and the attribute that widens
  it), or the thresholds differ (give both numbers), or one has an extra stratum.
- `disjoint_from`: the shared elements are incidental (an optional element on one side).
- `undecided` stays undecided when one side has no decomposition; propose what it would take to decide.

Then look at framing: if the two classes are physically the same but named differently, note the
instrument behind each name (translation problem, low severity). If they share a name and differ
physically, that is a collision (high severity); write it as an attention item for both systems.

## Output

Append your review under a "## Review" heading in the comparison node, one line per reviewed cell:
`A code | B code | relation | reason`, followed by a short list of attention items to add. Keep the
mechanical table above intact.
