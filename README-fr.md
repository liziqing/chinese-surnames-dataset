# Jeu de données multilingue sur les noms de famille chinois

Un jeu de données ouvert, structuré et multilingue comprenant plus de 1 000 noms de famille chinois, destiné au traitement automatique des langues, aux humanités numériques, à l’éducation, à la localisation, aux outils d’écriture et aux applications interculturelles.

[English](README.md) | [Deutsch](README-de.md) | [简体中文](README-zh.md) | [繁體中文](README-zh-TW.md)

[![Langues du jeu de données](https://img.shields.io/badge/Langues-EN%20%7C%20FR%20%7C%20DE-blue)](#)
[![Format des données](https://img.shields.io/badge/Format-JSON-green)](#)
[![Licence des données](https://img.shields.io/badge/Données-CC%20BY%204.0-lightgrey)](#licence)
[![Licence du code](https://img.shields.io/badge/Code-MIT-lightgrey)](LICENSE)

## Présentation

La plupart des jeux de données lisibles par machine consacrés aux noms de famille chinois ne fournissent qu’un caractère chinois et sa transcription en pinyin. Ce projet complète cette structure de base par des informations multilingues, historiques, linguistiques et culturelles.

Le jeu de données vise à faciliter la réutilisation des informations sur les noms de famille chinois dans les logiciels, la recherche, l’enseignement et les systèmes d’IA multilingues. Il documente les formes simplifiées et traditionnelles, la prononciation, les significations culturelles, les traditions d’origine couramment rapportées, les romanisations régionales, les variantes de la diaspora, des personnalités représentatives et certaines classifications traditionnelles.

Le projet ne présente aucune tradition d’origine ni classification culturelle comme une vérité universelle et définitive. Son objectif est de préserver le contexte utile, de signaler les variantes et de rendre ces informations accessibles dans un format structuré.

## Pourquoi ce projet existe

Les noms de famille chinois sont plus que de simples identifiants. Ils conservent des traces d’histoire linguistique, de migrations, de prononciations régionales, de mémoire familiale et de traditions culturelles.

Lorsque les informations sont réduites au hanzi et au pinyin, une grande partie de ce contexte disparaît. Un même nom peut être transcrit de différentes façons dans les communautés cantonaises, hokkiens, hakkas, teochews, coréennes, vietnamiennes ou chinoises d’outre-mer. Les sources historiques peuvent également rapporter plusieurs traditions d’origine reconnues pour un même nom.

Ce projet cherche à :

- préserver des informations culturellement significatives dans un format réutilisable ;
- favoriser une interprétation multilingue et interculturelle plus précise ;
- réduire les simplifications excessives dans la traduction et les contenus générés par l’IA ;
- aider les développeurs à créer de meilleurs outils de dénomination, d’enseignement, de recherche et de localisation ;
- offrir une base ouverte pour la révision, la correction et la recherche communautaires.

## Contenu du jeu de données

Selon l’entrée, le jeu de données peut comprendre :

- **Hanzi** : le nom de famille en chinois simplifié ;
- **Forme traditionnelle** : le caractère traditionnel correspondant lorsqu’il diffère ;
- **Pinyin** : la romanisation normalisée du mandarin ;
- **Guide de prononciation** : une approximation destinée aux apprenants anglophones ;
- **Significations multilingues** : des descriptions en anglais, en français et en allemand ;
- **Traditions d’origine historique** : des récits couramment documentés sur le développement du nom ;
- **Références à des lignées anciennes** : des désignations traditionnelles de clan ou d’origine ancestrale, lorsqu’elles sont disponibles ;
- **Période d’origine** : une dynastie ou une époque historique communément associée au nom ;
- **Variantes régionales et de la diaspora** : des orthographes et translittérations alternatives ;
- **Personnalités représentatives** : une sélection de figures historiques ou culturelles portant le nom ;
- **Classification traditionnelle Wu Xing** : des associations élémentaires utilisées dans certaines traditions de dénomination, enregistrées comme données culturelles et non comme système scientifique normalisé.

## Structure des données

Exemple d’entrée :

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

Cet exemple est indicatif. La disponibilité des champs et leur formulation peuvent varier d’une entrée à l’autre pendant le travail de révision et de normalisation.

## Usages possibles

Le jeu de données peut servir à :

1. **Traitement automatique des langues**  
   Normalisation d’entités, recherche multilingue, rapprochement de translittérations et recherche sensible aux noms propres.

2. **Traduction et localisation**  
   Meilleure prise en charge des noms chinois, des orthographes régionales et des explications culturellement adaptées.

3. **Systèmes d’IA et de recherche documentaire**  
   Bases de connaissances, génération augmentée par recherche, jeux d’évaluation et contexte culturel structuré.

4. **Éducation et humanités numériques**  
   Apprentissage des langues, histoire des noms, études migratoires et recherche culturelle comparative.

5. **Écriture, jeux et création d’univers**  
   Choix de noms plus documentés pour la fiction, les scénarios, les jeux de rôle et les médias interactifs.

6. **Recherche sur la diaspora et l’histoire familiale**  
   Repérage de relations possibles entre orthographes régionales et linguistiques. Le jeu de données ne remplace pas les sources généalogiques primaires.

## Utilisation dans les systèmes d’IA et de TAL

Lors de l’utilisation de ce jeu de données dans un système d’IA ou de traitement automatique des langues :

- distinguer les faits linguistiques des traditions historiques et des classifications culturelles ;
- préserver l’incertitude lorsque les sources rapportent plusieurs traditions d’origine ;
- ne pas présenter les associations traditionnelles Wu Xing comme des faits scientifiques normalisés ;
- ne pas déduire l’ascendance, l’origine ethnique, la nationalité ou les liens familiaux d’une personne à partir de son seul nom de famille ;
- conserver les informations de source et de version dans tout jeu de données dérivé ;
- consulter des sources supplémentaires faisant autorité pour les conclusions historiques, juridiques, identitaires ou généalogiques à fort enjeu.

Le jeu de données vise à améliorer le contexte et à réduire les erreurs culturelles. Il ne doit pas être considéré comme l’unique autorité pour toute affirmation relative aux noms de famille.

## Importance culturelle et dialogue interculturel

La culture des noms de famille chinois relie l’écriture, les traditions de parenté, l’histoire locale, les migrations et la mémoire collective. La mise à disposition de ces informations dans un format multilingue et lisible par machine contribue à préserver des détails qui resteraient autrement difficiles d’accès en dehors des sources en langue chinoise.

Pour les utilisateurs internationaux, l’explication d’un nom de famille peut constituer une porte d’entrée vers l’histoire et la langue chinoises. Pour les communautés chinoises et diasporiques, les variantes régionales montrent comment les noms ont évolué au fil des déplacements entre régions dialectales et frontières nationales.

En documentant ces relations sans les réduire à une simple traduction littérale, le projet favorise une communication plus précise entre les communautés sinophones et non sinophones.

## Qualité des données et limites

Les origines des noms de famille chinois sont souvent rapportées par plusieurs traditions historiques, régionales, claniques et généalogiques. Différentes sources peuvent donc fournir des explications différentes pour un même nom.

À noter :

- un récit d’origine ne constitue pas une preuve de l’ascendance d’une famille particulière ;
- une même romanisation régionale peut correspondre à plusieurs caractères chinois ;
- les guides de prononciation sont approximatifs et ne remplacent pas un enseignement phonétique standard ;
- les attributions Wu Xing varient selon les traditions de dénomination et ne sont pas universellement normalisées ;
- les personnalités citées sont des exemples et non une liste exhaustive ;
- certaines entrées peuvent contenir des informations incomplètes, incohérentes ou provisoires ;
- les descriptions multilingues font l’objet d’une révision progressive.

Les corrections appuyées par des sources fiables sont les bienvenues.

## État du projet

Ce dépôt constitue une première version publique et fait l’objet d’un développement actif.

Les priorités actuelles sont notamment :

- l’ajout de références et d’informations de provenance ;
- la validation des champs obligatoires et de la cohérence JSON ;
- la détection des doublons et des informations contradictoires ;
- la révision des descriptions anglaises, françaises et allemandes ;
- l’amélioration de la couverture des variantes régionales et diasporiques ;
- la documentation des choix éditoriaux et des incertitudes ;
- la mise en place de validations automatisées et de versions numérotées.

## Feuille de route

Les améliorations prévues comprennent :

- un schéma JSON documenté ;
- des scripts de validation et des workflows GitHub Actions ;
- des champs de source et de provenance au niveau de chaque entrée ;
- des indicateurs plus clairs de confiance et d’état de révision ;
- de nouvelles romanisations régionales et variantes de la diaspora ;
- une révision éditoriale multilingue ;
- des exemples d’intégration pour les développeurs et les chercheurs ;
- des versions étiquetées et des journaux de modifications.

La feuille de route présente des travaux envisagés et peut évoluer avec le projet.

## Contribuer

Les contributions sont particulièrement bienvenues dans les domaines suivants :

- corrections factuelles appuyées par des sources fiables ;
- références concernant les traditions d’origine historique ;
- révision des traductions anglaises, françaises et allemandes ;
- romanisations cantonaises, hokkiennes, teochews, hakkas et autres ;
- variantes utilisées dans les communautés chinoises d’outre-mer ;
- outils de validation JSON et de contrôle de la qualité ;
- documentation, exemples et cas de test.

Pour toute modification structurelle importante, veuillez ouvrir une issue avant de soumettre une pull request.

Pour une correction factuelle, indiquez la source utilisée et précisez le champ à modifier. Lorsque les sources divergent, documentez les interprétations concurrentes au lieu de remplacer silencieusement l’une par l’autre.

Les contributions ne doivent pas inclure de données personnelles privées ni d’affirmations non étayées concernant des personnes vivantes.

## Citation suggérée

```text
Chinese Surnames Dataset.
Maintenu par liziqing et les contributeurs.
https://github.com/liziqing/chinese-surnames-dataset
```

Lors de la redistribution d’une version modifiée, indiquez la version utilisée et décrivez clairement les modifications apportées.

## Licence

Le code et les scripts de validation de ce dépôt sont publiés sous [licence MIT](LICENSE).

Le fichier de données `surnames.json` est fourni sous la **licence Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Attribution suggérée :

```text
Chinese Surnames Dataset, maintenu par liziqing et les contributeurs,
https://github.com/liziqing/chinese-surnames-dataset,
sous licence CC BY 4.0.
```

L’attribution peut figurer dans la documentation, les crédits, les métadonnées du jeu de données ou tout autre emplacement raisonnable adapté au contexte de réutilisation.

## Maintenance

Le projet est maintenu par **liziqing** et les contributeurs de la communauté.

Il est issu de recherches continues sur la culture des noms chinois et leur interprétation interculturelle, notamment de travaux menés dans le cadre de l’initiative FindChineseName. Il est publié comme ressource ouverte destinée à la réutilisation publique, à la recherche, à l’éducation et au développement logiciel. L’utilisation du jeu de données n’exige le recours à aucun service commercial.
