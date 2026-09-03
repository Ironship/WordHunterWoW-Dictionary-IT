PACK_NAME = "WordHunterWoW-Dictionary-IT"

LOCALES = {
    "itIT": {
        "api": "it_IT",
        "source": "it",
        "variable": "WordHunterWoW_Dictionary_IT",
        "output": "DictionaryIT.lua",
        "curated": "CuratedIT.jsonl",
        "single_char_words": "aeièo",
        # Function words. A quest field that is thick with the English ones and
        # thin on these is an untranslated row sitting in the locale file, and
        # its words are not Italian words.
        "stopwords": ("il", "lo", "la", "gli", "le", "un", "una", "di", "del",
                      "della", "che", "per", "con", "non", "sono", "questo",
                      "questa", "nel", "nella", "dei", "delle", "al", "alla"),
    },
}

ENGLISH_STOPWORDS = ("the", "and", "you", "your", "with", "from", "that",
                     "this", "have", "will", "they", "them", "been", "must",
                     "into", "there", "their", "what", "when", "would")
