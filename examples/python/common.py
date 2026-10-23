"""Small standard-library client for the hosted Actor and its Dataset."""
import csv
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
ACTOR = "datascraperes~doctolib-france-scraper"
BASE = "https://api.apify.com/v2"

def request(path, body=None):
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError("Set APIFY_API_TOKEN before calling Apify.")
    payload = None if body is None else json.dumps(body).encode("utf-8")
    req = Request(BASE + path, data=payload,
                  headers={"Authorization": "Bearer " + token,
                           "Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=40) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Apify request failed (HTTP {exc.code}). Check your account and run in Console.") from None
    except URLError:
        raise RuntimeError("Connection failed. Inspect Console for an existing run before starting again.") from None

def sample_input():
    return json.loads((ROOT / "data/sample-input.json").read_text(encoding="utf-8"))

def dataset_items(dataset_id):
    if not re.fullmatch(r"[A-Za-z0-9]+", dataset_id):
        raise ValueError("Provide the Dataset ID from the run, not a URL.")
    offset = 0
    while True:
        page = request(f"/datasets/{dataset_id}/items?offset={offset}&limit=1000")
        if not isinstance(page, list):
            raise RuntimeError("Unexpected Dataset response.")
        yield from page
        if len(page) < 1000:
            break
        offset += len(page)

def run_actor(run_input):
    # Starting a run can incur charges. Never automatically repeat this POST.
    run = request(f"/acts/{ACTOR}/runs?build=latest&memory=256&timeout=180&maxTotalChargeUsd=0.05", run_input)["data"]
    print(f"Run ID: {run['id']} — inspect this run before retrying a start.", file=sys.stderr)
    deadline = time.monotonic() + 300
    while run["status"] in ("READY", "RUNNING", "TIMING-OUT", "ABORTING"):
        if time.monotonic() >= deadline:
            raise RuntimeError(f"Stopped waiting; inspect run {run['id']} in Console. It may still be active.")
        run = request(f"/actor-runs/{run['id']}?waitForFinish=10")["data"]
        if run["status"] in ("READY", "RUNNING"):
            time.sleep(1)
    if run["status"] != "SUCCEEDED":
        raise RuntimeError(f"Run {run['id']} ended with {run['status']}; inspect its log and saved data.")
    summary = request(f"/key-value-stores/{run['defaultKeyValueStoreId']}/records/SUMMARY")
    state = summary.get("runStatus")
    if state not in ("success", "partial"):
        raise RuntimeError("Missing or unexpected business result; inspect Run summary.")
    print(f"Result: {state}; reasons: {summary.get('partialReasons', [])}", file=sys.stderr)
    print(f"Dataset ID: {run['defaultDatasetId']}", file=sys.stderr)
    return list(dataset_items(run["defaultDatasetId"]))

CSV_FIELDS = ["recordKey", "recordType", "sourceStatus", "isPartial", "sourceUrl",
              "name", "specialty", "address", "city", "zipcode"]

def csv_row(item):
    provider = (item.get("searchResult") or {}).get("provider") or {}
    location = provider.get("location") or {}
    row = {k: item.get(k) for k in CSV_FIELDS[:5]}
    row.update(name=" ".join(filter(None, [provider.get("firstName"), (provider.get("name") or "").strip()])),
               specialty=(provider.get("speciality") or {}).get("name"),
               **{k: location.get(k) for k in ("address", "city", "zipcode")})
    return row

def export_csv(items, path):
    with Path(path).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for item in items:
            row = csv_row(item)
            # Treat external strings as text when opened in spreadsheet software.
            writer.writerow({k: "'" + v if isinstance(v, str) and v.lstrip().startswith(("=", "+", "-", "@")) else v
                             for k, v in row.items()})
