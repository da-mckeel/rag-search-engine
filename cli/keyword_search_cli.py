import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent/"data"/"movies.json"
with open(DATA_FILE) as f:
    movies = json.load(f)

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = []
            for m in movies["movies"]:
                if args.query in m["title"]:
                    results.append(m["title"])
                    if len(results) == 5:
                        break
            for i, title in enumerate(results, start=1):
                print(f"{i}. {title}")
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()