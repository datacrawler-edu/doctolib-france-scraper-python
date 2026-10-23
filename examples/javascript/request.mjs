// Node.js 20+. Starts one paid Actor run; preserve the printed run ID.
import { readFile } from 'node:fs/promises';
const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN before running this example.');
const base = 'https://api.apify.com/v2';
async function request(path, body) {
  const response = await fetch(base + path, {
    method: body === undefined ? 'GET' : 'POST',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(40000),
  });
  if (!response.ok) throw new Error(`Apify request failed (HTTP ${response.status}); inspect Console before retrying.`);
  return response.json();
}
const input = JSON.parse(await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));
let run = (await request('/acts/datascraperes~doctolib-france-scraper/runs?build=latest&memory=256&timeout=180&maxTotalChargeUsd=0.05', input)).data;
console.error(`Run ID: ${run.id}`);
const deadline = Date.now() + 300000;
while (['READY', 'RUNNING', 'TIMING-OUT', 'ABORTING'].includes(run.status)) {
  if (Date.now() >= deadline) throw new Error(`Stopped waiting; inspect run ${run.id} in Console. It may still be active.`);
  run = (await request(`/actor-runs/${run.id}?waitForFinish=10`)).data;
  if (['READY', 'RUNNING'].includes(run.status)) await new Promise(resolve => setTimeout(resolve, 1000));
}
if (run.status !== 'SUCCEEDED') throw new Error(`Run ${run.id} ended with ${run.status}; inspect saved data and log.`);
const summary = await request(`/key-value-stores/${run.defaultKeyValueStoreId}/records/SUMMARY`);
if (!['success', 'partial'].includes(summary.runStatus)) throw new Error('Unexpected business result; inspect Run summary.');
console.error(`Result: ${summary.runStatus}; reasons: ${JSON.stringify(summary.partialReasons || [])}`);
console.error(`Dataset ID: ${run.defaultDatasetId}`);
const items = [];
for (let offset = 0; ; ) {
  const page = await request(`/datasets/${run.defaultDatasetId}/items?offset=${offset}&limit=1000`);
  if (!Array.isArray(page)) throw new Error('Unexpected Dataset response.');
  items.push(...page);
  if (page.length < 1000) break;
  offset += page.length;
}
console.log(JSON.stringify(items, null, 2));
