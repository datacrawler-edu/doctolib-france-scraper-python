# Frequently asked questions

### Do I need a Doctolib account?
No. The hosted Actor collects publicly visible France data. An Apify account/token is needed for API examples; the web form needs no code.

### Are Germany and Italy supported?
No. Profile language options do not change the France-only coverage.

### Does it return appointment slots?
No. It can return public booking indicators and visit motives; no appointment availability or booking actions are included.

### Why is a successful platform run marked partial?
A requested limit or collection issue can make the business result partial. Check Run summary and Collection issues, including when no rows are returned.

### Will every result include a phone number?
No. Search rows and detailed profiles differ; public contact fields depend on what is present in the requested profile.

### Is the complete country directory guaranteed?
No. Searches are bounded, source-dependent and may include nearby localities. Empty results do not prove that no providers exist.

### Is the repository free to run?
The examples are MIT-licensed. Running the hosted Actor can incur charges. Check [current Actor pricing](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata); downloading an existing Dataset does not start a new Actor run.

### What if the connection drops while starting a run?
Check your runs in Console before retrying. Repeating a start request can create a second paid run. The examples print the run ID as soon as it is available and do not automatically repeat the start.
