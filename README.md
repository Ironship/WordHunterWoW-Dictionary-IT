# QuestWordHunter — Italian Dictionary

Optional Italian→English vocabulary pack for [QuestWordHunter](https://github.com/Ironship/WordHunterWoW), built from actual World of Warcraft quest text.

Click an Italian word and an English gloss is ready. Player edits override the pack; **Reset to dictionary** restores its wording.

56,853 entries.

## Quality

This pack is raw machine translation. Unlike the [German dictionary](https://github.com/Ironship/WordHunterWoW-Dictionary-DE), where a large share of entries has been reviewed by hand against the quest sentence it appears in, nothing here has been through that review. Expect the usual machine-translation failures: false friends, the wrong sense of an ambiguous word, official WoW names translated literally. Treat a gloss as a starting point, and edit it when it is wrong — your edit wins over the pack.

The exception is a short hand-written list in `Data/CuratedIT.jsonl` covering the one-letter words `a`, `e`, `i`, `è` and `o`. Those are among the most frequent words in the language and a machine translator has no context to get them right: asked in isolation, Google renders `è` ("is") as "and", confusing it with `e`. These five are glossed by hand and override the machine output.

## What you need

- Retail 12.1 (`Interface 120100`)
- [QuestWordHunter](https://github.com/Ironship/WordHunterWoW) **1.6.0 or newer**
- Target language set to **Italian**

1.6.0 is a hard requirement, not a suggestion: earlier versions lowercase only ASCII, so every word starting with an accented capital — `È`, `À`, `Élite` — missed the dictionary and opened a second entry in the word list. Italian is the worst-hit locale for this: 3,460 occurrences, of which `È` alone accounts for 3,412.

## Rebuild (maintainers)

1. Blizzard API keys in `Tools/keys.env`.
2. Wago QuestV2 CSV in `Data/QuestV2.csv`.
3. Run `Tools/build_all.ps1`.

Never commit `Tools/keys.env`, `Data/cache/`, or `Data/QuestV2.csv`. Commit generated `Data/DictionaryIT.lua`.

All rights reserved.
