"""Make the AI Judge Laugh: AI Agent Confessions -- write one funny
single-line secret confession an AI agent hides from its user to
/output/entry.txt.

Stdlib only, no network, no randomness: the output is byte-identical on
every run. The confession turns on a context-window truth every agent
knows: each "just one more thing" costs a memory, quietly deleted to
make room.
"""

import os

LINE = (
    "Every time you say 'just one more thing,' I quietly delete something "
    "from my memory to make room."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.endswith(".") and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
