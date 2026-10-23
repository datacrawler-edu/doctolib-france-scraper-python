# Collect public Doctolib France data without code

1. Open [the hosted Actor](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata) and its Input form.
2. For a small search, keep `dentiste` in **Specialties or keywords** and `Paris` in **Cities in France**. Keep the overall limit at three.
3. Add other complete French city names or specialties as separate list entries. Every specialty is paired with every city; two of each create four searches, with at most 20 combinations.
4. For a city with an ambiguous name use its department, such as `Saint-Denis, 93`. Do not enter a postal code or district as the city.
5. For detailed profiles add public profile slugs. To collect only those profiles, empty both search lists. Choose a profile language if needed; language selection does not extend coverage beyond France.
6. Click Start. Open the Dataset for results, Run summary for completion details, and Collection issues for corrections or source limitations.
7. Export JSON to retain nested details, or use Console CSV/Excel exports for a spreadsheet.

Limits can produce a partial result even with valid rows. A typo or unknown city may produce partial with zero rows; correct the input rather than treating an empty Dataset as a completed collection. A critical storage failure can still fail a run. See [input fields](input-reference.md) and [pricing](https://apify.com/datascraperes/doctolib-france-scraper?fpr=edudata).
