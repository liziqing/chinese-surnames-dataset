# Chinese Surnames Dataset

An open, structured, and multilingual dataset of more than 1,000 Chinese surnames for natural language processing, digital humanities, education, localization, writing tools, and cross-cultural applications.

[Français](README-fr.md) | [Deutsch](README-de.md) | [简体中文](README-zh.md) | [繁體中文](README-zh-TW.md)

[![Dataset Languages](https://img.shields.io/badge/Dataset%20Languages-EN%20%7C%20FR%20%7C%20DE-blue)](#)
[![Data Format](https://img.shields.io/badge/Format-JSON-green)](#)
[![Dataset License](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey)](#license)
[![Code License](https://img.shields.io/badge/Code-MIT-lightgrey)](LICENSE)

## Overview

Most machine-readable Chinese surname datasets provide only a Chinese character and its Pinyin transcription. This project extends that basic structure with multilingual, historical, linguistic, and cultural context.

The dataset is designed to make Chinese surname information easier to reuse in software, research, education, and multilingual AI systems. It documents simplified and traditional forms, pronunciation guidance, cultural meanings, commonly recorded origin narratives, regional romanizations, diaspora variants, representative figures, and traditional classifications.

The project does not present any single origin narrative or cultural classification as universally definitive. Its purpose is to preserve useful context, identify variation, and make the material accessible in a structured format.

## Why This Project Exists

Chinese surnames are more than identifiers. They preserve layers of linguistic history, migration, regional pronunciation, family memory, and cultural tradition.

When surname information is reduced to Hanzi and Pinyin alone, much of this context is lost. The same surname may appear under different spellings across Cantonese, Hokkien, Hakka, Teochew, Korean, Vietnamese, and overseas Chinese communities. Historical sources may also record several accepted origin traditions for one surname.

This project aims to:

- preserve culturally meaningful surname information in a reusable format;
- support accurate multilingual and cross-cultural interpretation;
- reduce oversimplification in translation and AI-generated content;
- help developers build better naming, education, search, and localization tools;
- provide a foundation for community review, correction, and further research.

## Dataset Contents

Depending on the record, the dataset may include:

- **Hanzi**: the surname in simplified Chinese;
- **Traditional form**: the corresponding traditional character when different;
- **Pinyin**: standardized Mandarin romanization;
- **Pronunciation guidance**: an English-oriented approximation for learners;
- **Multilingual meanings**: descriptions in English, French, and German;
- **Historical origin narratives**: commonly documented accounts of a surname’s development;
- **Ancient lineage references**: traditional clan or ancestral-origin labels where available;
- **Origin period**: a commonly associated dynasty or historical era;
- **Regional and diaspora variants**: alternative spellings and transliterations;
- **Representative figures**: selected historical or cultural figures associated with the surname;
- **Traditional Wu Xing classification**: elemental associations used in some naming traditions, recorded as cultural data rather than a standardized scientific system.

## Data Structure

Illustrative record:

```json
{
  "hanzi": "李",
  "traditional": "李",
  "pinyin": "Li",
  "pronunciation": "Lee (rhymes with 'see')",
  "element": "Wood",
  "meaningEn": "The surname Li (李) is commonly associated with the plum tree...",
  "meaningFr": "Le nom de famille Li (李) est couramment associé au prunier...",
  "meaningDe": "Der Familienname Li (李) wird häufig mit dem Pflaumenbaum verbunden...",
  "originEn": "One commonly recorded origin tradition connects the surname with...",
  "originFr": "Une tradition d'origine couramment rapportée associe ce nom à...",
  "originDe": "Eine häufig überlieferte Ursprungstradition verbindet den Namen mit...",
  "famousPeopleEn": "Selected representative figures...",
  "famousPeopleFr": "Personnalités représentatives sélectionnées...",
  "famousPeopleDe": "Ausgewählte repräsentative Persönlichkeiten...",
  "variants": [
    "Lee",
    "Lei",
    "Ong",
    "Lý"
  ],
  "ancientOrigin": "Ying (嬴)",
  "originEra": "Shang Dynasty to Western Zhou Dynasty"
}
```

The example is illustrative. Field availability and wording may vary between records while the dataset is being reviewed and normalized.

## Potential Uses

The dataset may support:

1. **Natural language processing**  
   Entity normalization, multilingual retrieval, transliteration matching, and name-aware search.

2. **Translation and localization**  
   Better handling of Chinese surnames, regional spellings, and culturally appropriate explanations.

3. **AI and retrieval systems**  
   Knowledge bases, retrieval-augmented generation, evaluation sets, and structured cultural context.

4. **Education and digital humanities**  
   Language learning, surname history, migration studies, and comparative cultural research.

5. **Writing, games, and world-building**  
   More informed character naming for fiction, screenwriting, role-playing games, and interactive media.

6. **Diaspora and family-history research**  
   Discovery of possible spelling relationships across regions and languages. The dataset is not a substitute for primary genealogical records.

## Use in AI and NLP Systems

When using this dataset in an AI or NLP system:

- distinguish linguistic facts from historical traditions and cultural classifications;
- preserve uncertainty when sources record multiple origin narratives;
- do not treat traditional Wu Xing associations as standardized scientific facts;
- do not infer a person’s ancestry, ethnicity, nationality, or family relationship from a surname alone;
- retain source and version information when incorporating records into a derived dataset;
- use additional authoritative sources for high-stakes historical, legal, identity, or genealogical conclusions.

The dataset is intended to improve context and reduce cultural error, not to serve as the sole authority for every surname-related claim.

## Cultural Significance and Cross-Cultural Exchange

Chinese surname culture connects written language, kinship traditions, local history, migration, and collective memory. Making this information available in a multilingual, machine-readable format helps preserve details that may otherwise remain inaccessible outside Chinese-language sources.

For international users, surname explanations can provide an entry point into Chinese history and language. For Chinese and diaspora communities, regional variants help show how names changed as families moved across dialect areas and national borders.

By documenting these relationships without reducing them to literal translation alone, the project supports more accurate communication between Chinese-speaking and non-Chinese-speaking communities.

## Data Quality and Limitations

Chinese surname origins are often recorded through multiple historical, regional, clan, and genealogical traditions. Different sources may provide different explanations for the same surname.

Please note:

- an origin narrative should not be treated as proof of an individual family’s ancestry;
- regional romanizations may overlap or refer to more than one Chinese character;
- pronunciation guides are approximate and do not replace standard phonetic instruction;
- Wu Xing assignments vary between naming traditions and are not universally standardized;
- representative figures are illustrative rather than exhaustive;
- some records may contain incomplete, inconsistent, or provisional information;
- multilingual descriptions are being progressively reviewed for accuracy and consistency.

Corrections supported by reliable sources are welcome.

## Project Status

This repository is an early public release and is under active development.

Current priorities include:

- adding source references and provenance information;
- validating required fields and JSON consistency;
- detecting duplicate or conflicting records;
- reviewing English, French, and German descriptions;
- improving regional and diaspora variant coverage;
- documenting editorial decisions and uncertainty;
- introducing automated validation and versioned releases.

## Roadmap

Planned improvements include:

- a documented JSON Schema;
- validation scripts and GitHub Actions;
- record-level source and provenance fields;
- clearer confidence and review-status indicators;
- additional regional romanizations and diaspora variants;
- multilingual editorial review;
- example integrations for developers and researchers;
- tagged dataset releases and changelogs.

Roadmap items describe intended work and may change as the project develops.

## Contributing

Contributions are welcome, particularly in the following areas:

- factual corrections supported by reliable sources;
- references for historical origin claims;
- English, French, and German translation review;
- Cantonese, Hokkien, Teochew, Hakka, and other regional romanizations;
- overseas and diaspora surname variants;
- JSON validation and data-quality tooling;
- documentation, examples, and test cases.

For substantial structural changes, please open an issue before submitting a pull request.

For factual corrections, include the source used and explain which field should change. Where sources disagree, document the competing interpretations rather than silently replacing one with another.

Contributors should avoid adding private personal information or unsupported claims about living individuals.

## Suggested Citation

```text
Chinese Surnames Dataset.
Maintained by liziqing and contributors.
https://github.com/liziqing/chinese-surnames-dataset
```

When redistributing a modified version, identify the version used and clearly indicate your changes.

## License

Code and validation scripts in this repository are licensed under the [MIT License](LICENSE).

The dataset file `surnames.json` is provided under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

Suggested dataset attribution:

```text
Chinese Surnames Dataset, maintained by liziqing and contributors,
https://github.com/liziqing/chinese-surnames-dataset,
licensed under CC BY 4.0.
```

Attribution may be placed in documentation, credits, dataset metadata, or another reasonable location appropriate to the reuse context.

## Maintainers

Maintained by **liziqing** and community contributors.

The project originated from ongoing research into Chinese naming culture and cross-cultural name interpretation, including research conducted as part of the FindChineseName initiative. It is published as an open resource for public reuse, research, education, and software development. Use of the dataset does not require the use of any commercial service.
