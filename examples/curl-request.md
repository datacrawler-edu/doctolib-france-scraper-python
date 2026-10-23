# Call Doctolib France with cURL

Run these commands from the repository root in Bash, with `APIFY_API_TOKEN` set. Starting an Actor can incur charges. Use the saved run ID if a connection fails; do not blindly repeat the start request.

```bash
curl --fail-with-body --max-time 60 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample-input.json \
  'https://api.apify.com/v2/acts/datascraperes~doctolib-france-scraper/runs?build=latest&memory=256&timeout=180&maxTotalChargeUsd=0.05' \
  --output run.json
```

Read `data.id` in `run.json`, set `RUN_ID` to it and check its status:

```bash
curl --fail-with-body --max-time 40 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/actor-runs/$RUN_ID?waitForFinish=10"
```

Repeat only the status GET while the run is active. Continue after `data.status` is `SUCCEEDED`; inspect logs and saved results for any other terminal status. From that response set `STORE_ID` to `defaultKeyValueStoreId` and `DATASET_ID` to `defaultDatasetId`.

```bash
curl --fail-with-body --max-time 40 -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/key-value-stores/$STORE_ID/records/SUMMARY"
curl --fail-with-body --max-time 40 -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/datasets/$DATASET_ID/items?format=json&offset=0&limit=1000" \
  --output results.json
```

Check `SUMMARY.runStatus` and `partialReasons`: technical success can contain partial results or no results. The Dataset request above retrieves the first 1,000 rows; increase offset by the page size for subsequent pages. The Python and JavaScript examples handle Dataset pagination automatically. `maxTotalChargeUsd` limits billable events; platform/resource charges and final accounting can differ, so monitor the run in Console.
