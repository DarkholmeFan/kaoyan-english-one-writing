"""Count approximate English words for practice feedback."""

import json
import re
import sys


WORD = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
    r"|(?:[A-Za-z]\.){2,}"
    r"|[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ0-9]*"
    r"(?:[-'’][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*"
    r"|\d+(?:[.,]\d+)*"
)


def main():
    essay = sys.stdin.read().strip()
    paragraphs = re.split(r"\n(?:[ \t]*\n)+", essay) if essay else []
    counts = [len(WORD.findall(paragraph)) for paragraph in paragraphs]
    print(json.dumps({"total": sum(counts), "paragraphs": counts}))


if __name__ == "__main__":
    main()
