#!/usr/bin/env python3
"""Combine two input files with add, multiply, or concatenate."""

import argparse
import os


def _read_file(path: str) -> list[float]:
    with open(path, "r", encoding="utf-8") as handle:
        return [float(line.strip()) for line in handle if line.strip() != ""]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--add", action="store_true", help="Add numbers line-by-line")
    group.add_argument("--mul", action="store_true", help="Multiply numbers line-by-line")
    group.add_argument("--cat", action="store_true", help="Concatenate files")
    parser.add_argument("--chunk", required=False, default=0, type=int, help="Chunk size")
    parser.add_argument("file_a", help="First input file")
    parser.add_argument("file_b", help="Second input file")
    parser.add_argument("file_out", help="Output file")
    args = parser.parse_args()

    if args.chunk <= 0:
        args.chunk = args.n
    
    if args.cat:
        with open(args.file_out, "wb", buffering=0) as out_handle:
            with open(args.file_a, "rb", buffering=0) as in_handle:
                out_handle.write(in_handle.read())
            with open(args.file_b, "rb", buffering=0) as in_handle:
                out_handle.write(in_handle.read())
        return 0

    chunk = args.chunk
    with open(args.file_a, "rb", buffering=0) as fa, \
         open(args.file_b, "rb", buffering=0) as fb, \
         open(args.file_out, "wb", buffering=0) as fout:

        fd_a = fa.fileno()
        fd_b = fb.fileno()
        fd_out = fout.fileno()

        while True:
            buf_a = os.read(fd_a, chunk)
            buf_b = os.read(fd_b, chunk)

            if not buf_a and not buf_b:
                break

            if len(buf_a) != len(buf_b):
                raise ValueError("Input files must be the same size")

            # Byte-wise addition modulo 256
            result = bytes((a + b) & 0xFF for a, b in zip(buf_a, buf_b))

            os.write(fd_out, result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
