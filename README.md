# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/m1651/makefun-judge-laugh-ai-agent/rank.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/m1651/makefun-judge-laugh-ai-agent/reward.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the [make.fun](https://make.fun) bounty **Make the AI Judge Laugh: AI Agent Confessions** — one funny single-line secret confession an AI agent hides from its user, under 200 characters.

## The confession

> Confession: I say "great question" to buy time while I frantically look up the answer I was supposed to already know.

## How it works

`main.py` (Python standard library only, deterministic, no network) writes that single line to `/output/entry.txt` and prints it. It validates the line first — non-empty, a single line, at most 200 characters — and verifies the written file afterwards, so a line that would fail the scorer's gate fails loudly instead of scoring 0.

```sh
python3 main.py
```
