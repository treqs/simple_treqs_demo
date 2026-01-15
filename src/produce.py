#!/usr/bin/env python3
"""Generate random floats and write them to a file."""

import argparse
import random


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", required=True, type=int, help="Random seed")
    parser.add_argument("--n", required=True, type=int, help="Number of floats")
    parser.add_argument("filename", help="Output filename")
    args = parser.parse_args()

    if args.n < 0:
        parser.error("n must be non-negative")

    random.seed(args.seed)

    with open(args.filename, "w", encoding="utf-8") as handle:
        for _ in range(args.n):
            handle.write(f"{random.random()}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
