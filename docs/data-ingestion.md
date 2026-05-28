# Data Ingestion Sources

## Current Location

Raw source files live under:

```text
_docs/_to_be_converted_to_fixtures/
```

These files are intended for a future ingestion process that will create
database fixtures or import-ready data. The target format is not defined yet.

## Inventory

Current source categories include:

- KML and KMZ railway paths and location data.
- XLS, XLSX, and ODS spreadsheets with stations, rolling stock, SIGO codes,
  network declarations, and related reference data.
- PDF and DOCX documents with source material for manual or automated
  extraction.
- MP4 media files that may later map to media records or storage ingestion.
- `files_to_download.txt`, a source list for future acquisition work.

## Handling Rules

- Treat raw files as immutable. Do not edit source files in place.
- Preserve original filenames when possible because they carry source context.
- Store generated fixtures outside `_docs/_to_be_converted_to_fixtures/`.
- Document extraction assumptions before committing derived data.
- Prefer structured parsers for spreadsheets, KML/KMZ, and document metadata.
- Keep one ingestion step accountable for one source family at a time.

## Future Pipeline

A future ingestion workflow should define:

1. Source file category and parser.
2. Target API table or fixture model.
3. Normalization rules, including names, coordinates, dates, and codes.
4. Validation checks against `infotrem-api` migrations and fixture allowlists.
5. Repeatable command and expected output location.

For API fixtures, align model names and load order with `infotrem-api` fixture
loading rules before generating committed YAML.
