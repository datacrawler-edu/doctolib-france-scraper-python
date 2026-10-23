"""Search dentists in two cities in one bounded Actor run."""
import json
from common import run_actor, sample_input

def main():
    value = sample_input()
    value.update(searchCities=["Paris", "Lyon"], maxResultsPerSearch=3, maxTotalRecords=6)
    print(json.dumps(run_actor(value), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
