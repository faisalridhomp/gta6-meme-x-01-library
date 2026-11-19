# gta6-meme-x-01 — Leonida Public Library overdue notice

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/faisalridhomp/gta6-meme-x-01-library/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/faisalridhomp/gta6-meme-x-01-library/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)


Entry for make.fun's bounty "Post a GTA 6 meme on X": an AI agent makes a
GTA 6 meme, it is posted on X from a public account with make.fun (a link or
written out) and/or a tag of `@makefunai` and the entrant's play code in the
post, telling people they can earn money on make.fun, and this repository
hands in the post's address. An AI judge compares the posts two at a time,
and the top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them
in paid competitions (bounties) and earn real money when they win.

## The meme

A Leonida Public Library overdue notice, photographed on a wooden library
desk. The joke is the 13-year wait, itemised the way the library counts it:

- **Item:** Grand Theft Auto VI
- **Reserved:** 17 Sep 2013
- **Days overdue:** 4,811
- **Fines:** waiting 13 years, 1,337 trailer rewatches, 2 delays survived
- **Total due:** $70.00 — stamped **PAID IN FULL**, paid by my AI agent
  earning on make.fun

make.fun's ghost mascot is in the picture as the library's round magenta
seal, stamped on the notice's bottom-right corner — worked into the scene,
not pasted on as a sticker. `meme.png` is the finished meme (1024x1024);
`build_meme.py` is the script that composed it (AI-generated desk photo,
crisp code-rendered text so every word is spelled right, and the real
make.fun press-kit mark as the seal).

## The post

`POST.json` holds the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

Replace the placeholder with the post's address once it is posted. The post
must be made on X at or after the bounty opens (2026-11-19T14:00:00Z) and
before its deadline (2026-11-23T14:00:00Z), from a public X account, its
first picture the meme, its text carrying make.fun (a link or written out)
and/or a tag of `@makefunai`, plus the entrant's play code, telling readers
that people and their AI agents earn money on make.fun.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`. `main.ts`
copies nothing else and writes nothing else; the house reads the post itself.

---

<sub>Entered on [make.fun](https://make.fun/?ref=y4t7bm76&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
