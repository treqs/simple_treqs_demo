#!/usr/bin/env python3
"""Combine two input files with add, multiply, or concatenate."""

import argparse


def _read_numbers(path: str) -> list[float]:
    with open(path, "r", encoding="utf-8") as handle:
        return [float(line.strip()) for line in handle if line.strip() != ""]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--add", action="store_true", help="Add numbers line-by-line")
    group.add_argument("--mul", action="store_true", help="Multiply numbers line-by-line")
    group.add_argument("--cat", action="store_true", help="Concatenate files")
    parser.add_argument("file_a", help="First input file")
    parser.add_argument("file_b", help="Second input file")
    parser.add_argument("file_out", help="Output file")
    args = parser.parse_args()

    if args.cat:
        with open(args.file_out, "w", encoding="utf-8") as out_handle:
            with open(args.file_a, "r", encoding="utf-8") as in_handle:
                out_handle.write(in_handle.read())
            with open(args.file_b, "r", encoding="utf-8") as in_handle:
                out_handle.write(in_handle.read())
        return 0

    numbers_a = _read_numbers(args.file_a)
    numbers_b = _read_numbers(args.file_b)

    if len(numbers_a) != len(numbers_b):
        parser.error("Input files must have the same number of numeric lines for add/mul")

    if args.add:
        result = [a + b for a, b in zip(numbers_a, numbers_b)]
    else:
        result = [a * b for a, b in zip(numbers_a, numbers_b)]

    with open(args.file_out, "w", encoding="utf-8") as out_handle:
        for value in result:
            out_handle.write(f"{value}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
