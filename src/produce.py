#!/usr/bin/env python3
"""Generate random floats and write them to a file."""

import argparse
import random
import os

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", required=True, type=int, help="Random seed")
    parser.add_argument("--chunk", required=True, type=int, help="Chunk size")
    parser.add_argument("--n", required=True, type=int, help="Number of floats")
    parser.add_argument("filename", help="Output filename")
    args = parser.parse_args()

    if args.n < 0:
        parser.error("n must be non-negative")

    random.seed(args.seed)

    chunk = args.chunk

    # Open in binary mode; buffering=0 disables Python's user-space buffering
    with open(args.filename, "wb", buffering=0) as handle:
        fd = handle.fileno()

        remaining = args.n
        buf = bytearray()

        while remaining > 0:
            # Fill a buffer up to exactly `chunk` bytes
            while len(buf) < chunk and remaining > 0:
                # Example payload: 8 random bytes per sample (change as you like)
                l = min(remaining,chunk)
                buf += random.randbytes(l)
                remaining -= l

            # Write exactly `chunk` bytes if possible; last write may be smaller
            to_write = bytes(buf[:chunk])
            os.write(fd, to_write)          # direct fd write => syscall
            buf = buf[chunk:]

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
