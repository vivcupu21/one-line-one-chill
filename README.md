# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)

Entry for the make.fun bounty **One Line, One Chill** ($5, sponsor Hanif / u-azazex).

## What it does

`main.py` (stdlib only, no network, no randomness) writes one original horror
sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`):

> The dentist held up the X-ray and said, 'You have thirty-three teeth,' and I counted the extra one moving.

106 characters, one sentence, one breath: a routine check-up, a count that
does not add up, and the last word doing the frightening.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
