"""Export an existing Dataset; this does not start another Actor run."""
import argparse
from common import dataset_items, export_csv

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id", help="Dataset ID displayed by request.py")
    parser.add_argument("--output", default="doctolib-results.csv")
    args = parser.parse_args()
    export_csv(dataset_items(args.dataset_id), args.output)
    print(f"Saved {args.output}")

if __name__ == "__main__":
    main()
