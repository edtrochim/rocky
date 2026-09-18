---
id: skill:prepare-submission
kind: guide
title: "Skill: prepare-submission"
schema: okf/0.1
name: prepare-submission
description: Build and verify the registry-ready package for a system.
inputs: [system]
tools: [submission_check]
---

# prepare-submission

Run `python okf/tools/submission_check.py --system <slug> --build`. It writes
`systems/<slug>/package/` with the LChS and LCCS3 files, the class CSV (id, hex, code, name), a
reference record and a README listing unresolved attention items, then checks schema validity, that the
CSV and XML agree on the class set, and that no placeholder names remain.

Your part:

1. Read the check report. Fix what it reports through the proper skill (a placeholder name means the
   ingest was wrong; a schema error means a decomposition wrote a property the type does not allow; a
   missing class means a decomposition failed). Rerun until `ok` is true.
2. Edit `package/README.md` so a registrar can read it: what the system is, who publishes it, which
   classes are decomposed, which are titles-only, and the top attention items with the decision each one
   needs. Keep it under one page.
3. Record in `SYSTEM.md` run history that the package was built, with the date.

Nothing is sent. Submission is a separate skill that a person triggers with `--submit`.
