"""Start the three-result example and print complete JSON records."""
import json
from common import run_actor, sample_input

def main():
    print(json.dumps(run_actor(sample_input()), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
