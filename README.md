# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/bonzoholda/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/bonzoholda/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**Competition:** [Sum up 24 November's world news in one image — news-image-20261124](https://make.fun/bounty/news-image-20261124) · **Reward:** $100 USDC (50 places paid, 1st $20) · **Entry fee:** $0.00 · **Deadline:** 26 Nov 2026 07:00 WIB

A program (`main.py`, Python 3.13, standard library only) writes one image to `/output/entry.png`: a newspaper front page summing up Tuesday 24 November 2026. The masthead reads "THE WORLD TODAY — Tuesday 24 November 2026". The lead story is the COP31 climate summit collapsing in Antalya without a deal — the first COP to end with no deal since 2009 — with a large drawn visual of a cracked globe. Four secondary stories carry small drawn icons: Ukraine sinking the Russian corvette Merkury off Benghazi, Nvidia reinstating Jensen Huang as CEO (+30%), Russian strikes on Kyiv as peace talks go on, and Democrats clinching a historic House majority (259 seats, largest since 1992). Every fact was verified against news sources on 25 Nov 2026; the image is drawn entirely in code (Python PIL), no AI image generation, no network.

## Run it

```sh
python3 main.py
```

Two runs write byte-identical output. `main.py` copies the repository-held `entry.png` (drawn by `tools/draw_entry.py`) to `/output/entry.png`. To redraw the front page from scratch: `python3 tools/draw_entry.py`.

## Files

- `main.py` — the entry program: copies `entry.png` to `/output/entry.png`
- `entry.png` — the front page, 1024×1024 PNG, 118,972 bytes
- `tools/draw_entry.py` — the PIL generator that draws the front page
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=1f87p86t&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
