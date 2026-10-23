# Input reference

The sample input includes all nine public fields. Defaults below apply when a value is omitted; the small example intentionally overrides several limits.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `profileSlugs` | array | null | Add one public Doctolib France profile identifier per item, for example laurent-martini-paris. Up to 50 profiles are supported; repeated identifiers are collected once. Leave this list empty to search by specialty and city. To collect only these profiles, clear both search lists. |
| `searchKeywords` | array | null | Add one French specialty or keyword per item, for example dentiste, Médecin généraliste, or Pédiatre. Accents, capitalization and extra spaces are accepted. Each term is searched in every city below: two terms and three cities create six searches. Enter both a specialty and a city, with at most 20 combinations. |
| `searchCities` | array | null | Add one complete French city name per item, for example Paris, Lyon, or Marseille. If several places share a name, include the department code, for example Saint-Denis, 93. Use city names rather than postal codes or districts. Results may include nearby providers. Each city is searched for every specialty above. |
| `locale` | string | "fr" | Choose the language for details collected from the optional profile list: French, English, German, or Italian. Some information may remain in its original language. This setting does not translate specialty searches. The default is French. |
| `includeRegion` | boolean | false | Add the administrative region, such as Ile De France, to provider locations with a valid French postal code. This is optional and does not add a separate result charge. If the region is unavailable, the main provider details are kept and the result is marked partial. |
| `maxPagesPerSearch` | integer | 5 | Set how many pages to check for each specialty and city combination, from 1 to 50. Increase this to look for more providers. A search stops sooner if it reaches its result limit or the overall limit. If more results may remain, the run summary is marked partial. |
| `maxResultsPerSearch` | integer | 100 | Set the maximum number of provider results for each specialty and city combination, from 1 to 1,000. The page limit and overall result limit also apply. Fewer providers may be returned when there are not enough matches. |
| `maxTotalRecords` | integer | 100 | Set the overall result limit, from 1 to 5,000. This includes all profiles and specialty searches together. The prefilled example collects up to 3 results; increase it for a larger collection. Failed lookups and run summaries do not count as results. |
| `continueOnError` | boolean | true | When enabled, continue with the remaining profiles and searches if one cannot be collected. When disabled, stop after the first lookup issue. Already collected results remain available in either case, and the run summary is marked partial with an explanation. |

Limits: 50 profile slugs, 20 specialty/city combinations, 50 pages per search, 1,000 results per search and 5,000 total rows. Each specialty is paired with every city. A global limit can stop later searches; it does not promise an equal number per city. Search terms should be supported French specialty names; capitalization, accents and spacing are normalized, but arbitrary text is not guaranteed to match.

Profiles use public slugs, not patient identifiers. `locale` affects direct profile presentation only. `continueOnError` allows subsequent targets after collection issues; run summaries still explain partial output.
