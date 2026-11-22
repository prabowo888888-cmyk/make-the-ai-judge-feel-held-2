#!/usr/bin/env python3
"""Make the AI judge feel held - make.fun entry.

Writes one short text to /output/entry.txt.
Deterministic, no network, standard library only.
"""
import os
from pathlib import Path

TEXT = (
    "After the rain, the street smells of wet stone, and a cat is asleep "
    "on the neighbour's wall, one paw tucked under its chin. "
    "The laundry line is empty. "
    "The day has folded itself away, and there is nowhere else you have to be tonight."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
