import os
import sys
from pathlib import Path

LINE = "Sorry I missed the deadline \u2014 I ran out of tokens halfway through, forgot it existed, and hallucinated a calendar that moved it to next week."


def main():
    # The gate allows 1 to 200 characters; keep the entry inside it.
    assert 1 <= len(LINE) <= 200, len(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
