# Output reference

Each Dataset item represents one public profile or one provider search result. The [complete search sample](../data/sample-output.json) preserves the nested source values returned by the hosted Actor; it is a sample, not a guaranteed current directory.

| Field | Meaning |
|---|---|
| `recordType` | `profile` or `search_result` |
| `recordKey` | Stable identity for deduplicating repeated exports |
| `sourceInput`, `sourceUrl`, `retrievedAt` | Requested target, public source URL and collection time |
| `sourceStatus`, `isPartial`, `partialReasons` | Completeness and limitations of this record |
| `profile` | Direct-profile details when requested; otherwise null |
| `searchResult` | Search context, page and provider when searching; otherwise null |
| `searchResult.provider` | Public provider identity, specialty, location and booking indicators |

Direct profiles can include practitioners, practices and public contact details, agendas and visit motives. A search row is not automatically a fully enriched profile. Optional fields can be null or absent depending on the source. A booking indicator is not appointment availability.

The Key-Value Store exposes SUMMARY (`runStatus`, `recordsDelivered`, `sourceErrors`, `partialReasons`) and ERRORS for collection issues. Always inspect business status even when the platform run says SUCCEEDED. `partial` is valid and must not be described as complete; it may have zero rows.

The shipped CSV example projects search rows into identity/status/link, name, specialty, address, city and postcode. Direct profiles keep their identity/status/link but do not populate search-specific columns in this projection. Use JSON or customize the projection to retain nested profile details. CSV export prefixes spreadsheet formula-like strings as text.
