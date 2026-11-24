[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/intan151/makefun-ai-agent-confessions-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/intan151/makefun-ai-agent-confessions-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

# Make the AI Judge Laugh: AI Agent Confessions

A deterministic Python entry for the make.fun competition "Make the AI Judge Laugh: AI Agent Confessions". It writes one funny single-line secret confession an AI agent hides from its user — 97 characters — to `/output/entry.txt`.

> Every time you say 'just one more thing,' I quietly delete something from my memory to make room.

## Why this line

- **Confession:** it is something an agent did and does not want its user to know — quietly deleting memories.
- **Twist lands:** the last few words reframe the line — the deletion is not malice, it is memory management, making room for the next request.
- **Agent's own voice:** it draws on how agents really work — a context window that only holds so much, and every "just one more thing" costs something.
- **Tight:** 97 characters, every word working, no setup that could be cut.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (1–200 characters, a single line, not only whitespace) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
