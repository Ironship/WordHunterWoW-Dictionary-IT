# Italian dictionary audit — instructions

You are improving an Italian→English dictionary used by a World of Warcraft addon.
Players read Italian quest text and click a word to see its English meaning plus a
short note. Your job is to fix machine-translation errors and write notes that
teach the reader something worth knowing.

## Input

`Data/cache/audit_work/in/batch_NN.jsonl` — one JSON object per line:

- `key` — lowercase lookup key. **Copy it through byte for byte.** It is already
  casefolded the way the addon looks words up, and accents are part of the key:
  `è`, `perché`, `città`, `più` keep theirs. Do not ASCII-fold `à è é ì ò ù`, do
  not re-case, and above all do not add an accent the key does not have — `e`
  and `è` are different words with different keys, and "correcting" one into the
  other silently overwrites the wrong entry. Copy the key and the word exactly as
  given: a changed key breaks the lookup, and a changed word breaks the repair
  path that would otherwise recover it.
- `word` — the Italian word as it appears in game. **Copy through verbatim.**
- `current` — the existing Google Translate output. Often right, sometimes wrong.
- `count` — how often the word occurs across all quests.
- `context` — a real quest sentence containing the word.

## Output

`Data/cache/audit_work/out/batch_NN.jsonl` — one JSON object per input line,
**same order, same count, same keys**, with exactly these four fields:

```json
{"key":"roccavento","word":"Roccavento","translation":"Stormwind","note":"rocca (fortress) + vento (wind); the human capital"}
```

Write the file with the Write tool, in one single write. Do not use apply_patch:
a file of 150 dense JSON lines is not a patchable target and the attempt fails.
UTF-8, no BOM, no trailing commas, no markdown fences, one compact JSON object
per line.

## Do both jobs in one pass

The two halves of this task are the translation and the note, and they carry
equal weight. Agents on this task reliably do one and skip the other: a pass
told to care about notes stops touching translations, and a pass told to care
about translations writes four notes in a hundred and fifty rows.

A healthy pass revises a good share of the translations and leaves a note on
nearly every row that is owed one. A bare proper name is not owed a note, and an
empty one is correct there — you must not invent lore.

**Do not append a synonym to a translation that is already correct.** Repeating
the existing answer unchanged is the right outcome when it is right; padding it
out to look busy is not a correction and is easy to spot.

## Errors to look for before you accept `current`

Google is right often enough that skimming feels safe. These are the mistakes it
actually makes on Italian quest text:

- an accent dropped or added, which changes the word entirely: `e` is "and",
  `è` is "is"; `la` is "the", `là` is "there"; `da` is "from", `dà` is "gives";
  `si` is the reflexive pronoun, `sì` is "yes"; `ne` is "of it", `né` is "nor"
- the congiuntivo read as an indicative (`abbia` is "may have", not "has")
- the passato remoto flattened to a present (`portò` is "carried", not "carries")
- an imperative read as a third person (`raccogli` as a command is "collect",
  as a statement "he collects" — quest objectives are commands)
- a false friend taken at face value: `attualmente` is currently not actually,
  `eventualmente` is possibly not eventually, `morbido` is soft not morbid,
  `fattoria` is a farm not a factory, `libreria` is a bookshop not a library,
  `parenti` are relatives not parents, `camera` is a room not a camera,
  `sensibile` is sensitive not sensible
- a plural rendered as a singular, or the reverse — Italian plurals in -i and -e
  are easy to miss
- an elided or truncated form read as a different word: `un'anima` is "a soul",
  and `de'` `co'` `po'` are clipped forms, not typos
- an official English WoW name missed, or invented

## translation

- Give the meaning that fits **WoW quest text**, not a dictionary's first entry.
- Use the **official English WoW term** when the Italian is a game proper noun,
  and only when you are confident of it. If you are not, give a clean literal
  translation instead. **Do not invent lore, zone names, or NPC names.** This is
  the single most damaging mistake available here: in the Spanish pack a coined
  place name had been glossed "Ironforge" and was in fact Razor Hill.
- Separate genuinely distinct senses with `; ` — at most three, most common first.
- Keep the grammatical category of the Italian word (noun → noun, verb → verb).
  Nouns: no article. Verbs: bare infinitive without "to" unless it disambiguates.
- Capitalise by English convention, not the source's. Italian lowercases things
  English capitalises — `italiano` → Italian, `martedì` → Tuesday, `gennaio` →
  January — so the translation is capitalised even though the word is not.
- If `current` is already the best answer, repeat it unchanged. That is a normal
  and expected outcome.

## note

This is the part the reader actually reads for pleasure. Make it earn its place.

1. **Word breakdown**, when it illuminates the word:
   `oscurità` → "oscuro (dark) + -ità, the suffix that turns adjectives into nouns"
2. **False friend / trap**, when a learner would guess wrong:
   `attualmente` → "false friend: means currently, never actually"
3. **Official name differs from the literal sense**, when you are sure of it
4. **Idiom or fixed phrase** the word usually appears in:
   `fare` → "fare a meno di = to do without"
5. **Etymology or a genuinely interesting fact**:
   `ciao` → "from Venetian s-ciavo, 'your servant'"

Rules:

- English, lowercase start, **no trailing period**, at most ~120 characters.
- Never merely restate the translation ("means darkness") — that is wasted space.
- Never write filler like "common verb" or "common Italian word" on its own.
- If nothing worth saying comes to mind, use `""`. An empty note is much better
  than a boring one, and it is the right answer for a bare proper name.
- No newlines, no quotes-inside-quotes problems — keep it plain.

## Accuracy

Getting a translation wrong is worse than leaving it as it was. When torn between
a confident literal reading and a half-remembered WoW term, choose the literal
one and say in the note what you could not confirm. Do not guess at lore.
