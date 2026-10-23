# Workflows

## Find dentists in a French city

Run `python examples/python/request.py` for the bounded dentists-in-Paris sample. Use the complete source URL to inspect an individual listing. Neighbouring towns may appear in source results.

## Compare public listings in two cities

Run `python examples/python/batch_search.py`. It searches Paris and Lyon, with up to three results per search and six total. Distinct records can refer to the same provider seen in different searches; choose a provider identity or recordKey according to your analysis.

## Export an existing Dataset

Run `python examples/python/export_results.py DATASET_ID --output results.csv`. This only reads an existing Dataset and does not start another paid Actor execution. It follows Dataset pagination. It does not fetch additional Doctolib details.

## Obtain detailed public profiles

Edit the sample input with profile slugs and empty both search lists. Optional region enrichment applies to valid French postal codes; profile localization may be incomplete. Prefer JSON for all nested data.
