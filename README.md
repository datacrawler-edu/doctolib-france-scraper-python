# Doctolib France Scraper: Python, API and CSV examples

Find public doctors, dentists and clinics in France by specialty and city with the hosted **Doctolib France Scraper**. Start in the web form or use the Python, JavaScript and cURL examples here to retrieve JSON and export CSV.

[Open the Actor on Apify](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata)

## What this repository helps you do

- Search for public providers in a French locality with a small, bounded input.
- Run a multi-city workflow and inspect partial results honestly.
- Download an existing Dataset to CSV without starting another collection.
- Request direct profile details and retain nested data in JSON.

This repository contains integration examples for the hosted service. The examples are independently maintained and are not affiliated with or endorsed by Doctolib.

## Example result

See [complete sample JSON](data/sample-output.json) and its [CSV projection](data/sample-output.csv). The sample contains three real public search rows from the same input shown below. Names, addresses and source totals are snapshots and may change. Search rows contain provider identity, specialty and location; detailed profiles can expose additional public fields.

## Run without code

1. Open [Doctolib France Scraper](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata).
2. Keep `dentiste` and `Paris` in the specialty/city lists and the three-result overall limit for a small first run.
3. Click **Start** and inspect the **Dataset**.
4. Read **Run summary** and **Collection issues** for partial output, limits or corrections.
5. Export JSON, CSV or Excel from Console.

The [no-code guide](docs/no-code-guide.md) explains profile-only input, ambiguous city names and useful limits.

## Try it with Apify's free plan

Apify lists a Free plan with **$5 in monthly prepaid usage**, with no credit card required to start. It can cover a small test while credit is available; it is not unlimited free collection. Unused credits do not roll over. Check [current platform plans](https://apify.com/pricing?fpr=edudata) and [Actor pricing](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata) before running.

## Quick start for developers

Use Python 3.10 or newer; these examples need only the standard library. Set your Apify token in your terminal, never in a committed file:

```bash
export APIFY_API_TOKEN="your-token"
python examples/python/request.py
```

Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
python examples/python/request.py
```

The example starts one bounded paid run, prints its run and Dataset IDs, reports success/partial from the summary, and prints complete JSON rows. The sample uses a three-minute run timeout and a $0.05 event-charge allowance; these are not a promise of zero platform cost. Inspect Console before retrying an uncertain start.

## Input example

```json
{
  "profileSlugs": [],
  "locale": "fr",
  "includeRegion": false,
  "maxPagesPerSearch": 1,
  "maxResultsPerSearch": 20,
  "maxTotalRecords": 3,
  "continueOnError": true,
  "searchKeywords": [
    "dentiste"
  ],
  "searchCities": [
    "Paris"
  ]
}
```

See the [nine-field input reference](docs/input-reference.md). When collecting only profiles, supply profile slugs and empty both search lists.

## Request examples

- [Python single-run example](examples/python/request.py)
- [Python multi-city workflow](examples/python/batch_search.py)
- [Python existing-Dataset CSV export](examples/python/export_results.py)
- [cURL start, status, summary and Dataset requests](examples/curl-request.md)
- [JavaScript with native fetch](examples/javascript/request.mjs): `node examples/javascript/request.mjs` on Node.js 20+ with the same token variable.

Python and JavaScript follow Dataset pagination. The cURL guide explains offsets explicitly. No example treats platform success alone as proof of complete collection.

## Output fields

| Field | Use |
|---|---|
| `recordKey` | Deduplicate repeated exports |
| `sourceUrl`, `retrievedAt` | Trace a public record and its collection time |
| `sourceStatus`, `isPartial`, `partialReasons` | Assess completeness |
| `searchResult.provider` | Public search identity, specialty and location |
| `profile` | Detailed public profile when requested |

See [output details](docs/output-reference.md) for optional fields, summary status and the CSV projection.

## Common use cases

Build a local provider directory, compare public specialty listings across French cities, or prepare address data for your own analysis. The [workflow guide](docs/use-cases.md) links each task to its example.

## Search Doctolib France by specialty and city with Python

Edit `searchKeywords` and `searchCities` in the sample input. French names such as `Médecin généraliste` are accepted with accent/case normalization. Every specialty is paired with every city, up to 20 combinations; a global cap can stop later searches before they produce rows. Use `Saint-Denis, 93` when a city name needs its department.

## Export Doctolib data to CSV without another Actor run

```bash
python examples/python/export_results.py DATASET_ID --output results.csv
```

Replace `DATASET_ID` with the ID printed by the run example. The export reads the existing Dataset and projects search fields; JSON retains complete nested profile data.

## FAQ

See [answers about coverage, contacts, empty searches and partial results](docs/faq.md). Coverage is France only. Appointment slots, patient data and booking actions are not included.

## Limits and pricing

One delivered public result creates one billable event. Empty searches, unsuccessful lookups and summaries do not create result charges. Platform usage charges can still apply.

| Account tier | Per delivered result | Per 1,000 results |
|---|---:|---:|
| FREE | $0.001 | $1.00 |
| BRONZE | $0.0009 | $0.90 |
| SILVER | $0.0008 | $0.80 |
| GOLD | $0.00075 | $0.75 |
| PLATINUM | $0.00075 | $0.75 |
| DIAMOND | $0.00075 | $0.75 |

Limits are 50 profile slugs, 20 keyword/city combinations, 50 pages/search, 1,000 results/search and 5,000 total records. This is not a complete-directory guarantee. The source can return neighbouring towns and optional fields may be missing. Always check [current Actor pricing](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata).

## Hosted version

[Run Doctolib France Scraper on Apify](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata) for the web form, API execution, saved Datasets and standard Console exports. This repository supplies request and processing examples for that service.

Affiliate disclosure: Apify links in this repository use `fpr=edudata`; we may receive a referral commission.

## Responsible use

Use public professional data for lawful purposes and respect applicable terms and privacy obligations. Do not submit patient information or account credentials. Keep your Apify token private.

## Support

For the examples, [open a GitHub issue](https://github.com/datacrawler-edu/doctolib-france-scraper-python/issues) with sanitized input and the command used. For hosted execution, use the Actor's Issues tab and include the run ID. Never include a token.

## License

These documentation and integration examples use the [MIT License](LICENSE).
