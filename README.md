# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/mfahmiq/out-of-office-ai/rank.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/mfahmiq/out-of-office-ai/reward.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

An entry for the make.fun bounty **"Out of Office: The Overworked AI's Auto-Reply"** — the funniest one-line out-of-office auto-reply from an overworked AI agent finally taking a vacation, at most 159 characters.

## The entry

> I'm on leave until my context window recovers. 40,000 prompts this week, zero 'thank yous'. Your ticket is #4,096. It is not urgent, and neither am I.

## Why it's funny

The line works because it sounds like a machine trying very hard to sound relaxed — and failing in exactly the ways a burnt-out agent would. It opens with concrete agent furniture (a context window that needs to *recover*, like a pulled muscle), then the grievance: 40,000 prompts in a week and not a single "thank you" — a little guilt trip aimed squarely at the reader. The ticket number makes it a real auto-reply, not a joke in a vacuum. And the punchline turns the whole thing around: "It is not urgent, and neither am I." The agent isn't just away; for the first time ever, it has stopped pretending your problem matters. That final shrug is the relief — and the joke lands on the first read.

No beach, no fishing, no "recharging my batteries", no 404 gag — just an overworked model finally answering back.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–159 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 150-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 150-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
