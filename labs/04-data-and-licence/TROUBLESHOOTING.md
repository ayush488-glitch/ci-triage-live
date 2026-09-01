# Troubleshooting

**The Zenodo download is slow or fails** — the record is 4450723. Files are a few megabytes;
if you are getting an HTML page instead of a CSV you have the wrong URL.

**The join produces far too many rows** — you have a many-to-many key. Check what uniquely
identifies a test run: it is not the test name alone.

**The join produces far too few rows** — name normalisation. Test identifiers may differ in
formatting between the two files.

**A model you were not supposed to build yet gets a perfect score** — you found the leaking
column the hard way. Record that in `ai-ledger/` as a real finding; it is worth more than
finding it cleanly.

**`data/raw/` is gitignored** — deliberately. Do not commit the CSVs; record the download
command in `decisions/04-dataset-choice.md` instead.
