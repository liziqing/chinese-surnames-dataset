# Mehrsprachiger Datensatz chinesischer Familiennamen

Ein offener, strukturierter und mehrsprachiger Datensatz mit mehr als 1.000 chinesischen Familiennamen für Natural Language Processing, Digital Humanities, Bildung, Lokalisierung, Schreibwerkzeuge und interkulturelle Anwendungen.

[English](README.md) | [Français](README-fr.md) | [简体中文](README-zh.md) | [繁體中文](README-zh-TW.md)

[![Datensatzsprachen](https://img.shields.io/badge/Sprachen-EN%20%7C%20FR%20%7C%20DE-blue)](#)
[![Datenformat](https://img.shields.io/badge/Format-JSON-green)](#)
[![Datenlizenz](https://img.shields.io/badge/Daten-CC%20BY%204.0-lightgrey)](#lizenz)
[![Codelizenz](https://img.shields.io/badge/Code-MIT-lightgrey)](LICENSE)

## Überblick

Die meisten maschinenlesbaren Datensätze zu chinesischen Familiennamen enthalten lediglich ein chinesisches Schriftzeichen und dessen Pinyin-Umschrift. Dieses Projekt erweitert diese Grundstruktur um mehrsprachige, historische, sprachwissenschaftliche und kulturelle Zusammenhänge.

Der Datensatz soll Informationen über chinesische Familiennamen für Software, Forschung, Bildung und mehrsprachige KI-Systeme leichter nutzbar machen. Er dokumentiert vereinfachte und traditionelle Zeichenformen, Aussprachehilfen, kulturelle Bedeutungen, häufig überlieferte Ursprungstraditionen, regionale Romanisierungen, Diaspora-Varianten, repräsentative Persönlichkeiten und traditionelle Klassifikationen.

Das Projekt stellt weder eine einzelne Ursprungserzählung noch eine kulturelle Klassifikation als allgemeingültige Wahrheit dar. Ziel ist es, relevanten Kontext zu bewahren, Unterschiede sichtbar zu machen und die Informationen strukturiert zugänglich zu machen.

## Warum dieses Projekt existiert

Chinesische Familiennamen sind mehr als bloße Bezeichnungen. In ihnen spiegeln sich Sprachgeschichte, Migration, regionale Aussprache, Familienerinnerung und kulturelle Traditionen.

Werden die Informationen auf Hanzi und Pinyin reduziert, geht ein großer Teil dieses Kontexts verloren. Derselbe Familienname kann in kantonesischen, Hokkien-, Hakka-, Teochew-, koreanischen, vietnamesischen und überseechinesischen Gemeinschaften unterschiedlich geschrieben werden. Historische Quellen können außerdem mehrere anerkannte Ursprungstraditionen für denselben Namen überliefern.

Das Projekt verfolgt folgende Ziele:

- kulturell bedeutsame Informationen in einem wiederverwendbaren Format zu bewahren;
- genauere mehrsprachige und interkulturelle Interpretation zu unterstützen;
- übermäßige Vereinfachungen in Übersetzungen und KI-generierten Inhalten zu reduzieren;
- Entwicklern bessere Werkzeuge für Namenssysteme, Bildung, Suche und Lokalisierung zu ermöglichen;
- eine offene Grundlage für gemeinschaftliche Prüfung, Korrektur und weitere Forschung bereitzustellen.

## Inhalt des Datensatzes

Je nach Eintrag kann der Datensatz folgende Felder enthalten:

- **Hanzi**: der Familienname in vereinfachtem Chinesisch;
- **Traditionelle Form**: das entsprechende traditionelle Zeichen, sofern abweichend;
- **Pinyin**: standardisierte Romanisierung des Mandarin;
- **Aussprachehilfe**: eine englisch orientierte Annäherung für Lernende;
- **Mehrsprachige Bedeutungen**: Beschreibungen auf Englisch, Französisch und Deutsch;
- **Historische Ursprungstraditionen**: häufig dokumentierte Erzählungen zur Entwicklung des Namens;
- **Verweise auf alte Abstammungslinien**: traditionelle Clan- oder Herkunftsbezeichnungen, sofern verfügbar;
- **Ursprungszeitraum**: eine häufig mit dem Namen verbundene Dynastie oder Epoche;
- **Regionale und diasporische Varianten**: alternative Schreibweisen und Transliterationen;
- **Repräsentative Persönlichkeiten**: ausgewählte historische oder kulturelle Namensträger;
- **Traditionelle Wu-Xing-Klassifikation**: Elementzuordnungen aus bestimmten Namenstraditionen, erfasst als Kulturdaten und nicht als standardisiertes wissenschaftliches System.

## Datenstruktur

Beispielhafter Eintrag:

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

Das Beispiel dient der Veranschaulichung. Verfügbarkeit und Formulierung einzelner Felder können sich während der Prüfung und Normalisierung noch unterscheiden.

## Mögliche Anwendungen

Der Datensatz kann unter anderem für folgende Zwecke verwendet werden:

1. **Natural Language Processing**  
   Entitätsnormalisierung, mehrsprachige Suche, Abgleich von Transliterationen und namensbezogene Suchfunktionen.

2. **Übersetzung und Lokalisierung**  
   Bessere Verarbeitung chinesischer Familiennamen, regionaler Schreibweisen und kulturell angemessener Erklärungen.

3. **KI- und Retrieval-Systeme**  
   Wissensbasen, Retrieval-Augmented Generation, Evaluationsdatensätze und strukturierter kultureller Kontext.

4. **Bildung und Digital Humanities**  
   Sprachlernen, Namensgeschichte, Migrationsforschung und vergleichende Kulturwissenschaft.

5. **Literatur, Spiele und World-Building**  
   Fundiertere Namenswahl für Romane, Drehbücher, Rollenspiele und interaktive Medien.

6. **Diaspora- und Familiengeschichtsforschung**  
   Auffinden möglicher Beziehungen zwischen regionalen und sprachlichen Schreibweisen. Der Datensatz ersetzt keine genealogischen Primärquellen.

## Verwendung in KI- und NLP-Systemen

Bei der Verwendung des Datensatzes in KI- oder NLP-Systemen sollte Folgendes beachtet werden:

- sprachliche Fakten sind von historischen Traditionen und kulturellen Klassifikationen zu unterscheiden;
- Unsicherheit sollte erhalten bleiben, wenn Quellen mehrere Ursprungstraditionen nennen;
- traditionelle Wu-Xing-Zuordnungen dürfen nicht als standardisierte wissenschaftliche Tatsachen dargestellt werden;
- aus einem Familiennamen allein dürfen keine Rückschlüsse auf Abstammung, Ethnie, Nationalität oder konkrete Familienbeziehungen gezogen werden;
- Quellen- und Versionsinformationen sollten in abgeleiteten Datensätzen erhalten bleiben;
- für historische, rechtliche, identitätsbezogene oder genealogische Schlussfolgerungen mit hoher Tragweite sind zusätzliche verlässliche Quellen heranzuziehen.

Der Datensatz soll Kontext verbessern und kulturelle Fehler reduzieren. Er ist nicht als alleinige Autorität für jede Aussage über Familiennamen gedacht.

## Kulturelle Bedeutung und interkultureller Austausch

Die chinesische Familiennamenkultur verbindet Schrift, Verwandtschaftstraditionen, Lokalgeschichte, Migration und kollektives Gedächtnis. Ein mehrsprachiges, maschinenlesbares Format hilft dabei, Informationen zu bewahren, die außerhalb chinesischsprachiger Quellen sonst nur schwer zugänglich wären.

Für internationale Nutzer können Familiennamen einen Einstieg in chinesische Geschichte und Sprache bieten. Für chinesische und diasporische Gemeinschaften zeigen regionale Varianten, wie sich Namen bei Wanderungen zwischen Dialekträumen und Staatsgrenzen verändert haben.

Indem das Projekt diese Zusammenhänge dokumentiert, ohne sie auf wörtliche Übersetzungen zu reduzieren, unterstützt es eine präzisere Verständigung zwischen chinesischsprachigen und nicht chinesischsprachigen Gemeinschaften.

## Datenqualität und Einschränkungen

Die Ursprünge chinesischer Familiennamen werden häufig in mehreren historischen, regionalen, clanbezogenen und genealogischen Traditionen beschrieben. Verschiedene Quellen können daher unterschiedliche Erklärungen für denselben Namen liefern.

Zu beachten ist:

- eine Ursprungserzählung ist kein Beweis für die Abstammung einer konkreten Familie;
- regionale Romanisierungen können mehrdeutig sein und mehreren chinesischen Zeichen entsprechen;
- Aussprachehilfen sind Näherungen und ersetzen keine standardisierte phonetische Anleitung;
- Wu-Xing-Zuordnungen unterscheiden sich je nach Namenstradition und sind nicht allgemein standardisiert;
- genannte Persönlichkeiten dienen als Beispiele und bilden keine vollständige Liste;
- einzelne Einträge können unvollständige, widersprüchliche oder vorläufige Angaben enthalten;
- die mehrsprachigen Beschreibungen werden schrittweise auf Genauigkeit und Konsistenz geprüft.

Korrekturen, die durch verlässliche Quellen belegt sind, sind willkommen.

## Projektstatus

Dieses Repository ist eine frühe öffentliche Version und wird aktiv weiterentwickelt.

Zu den aktuellen Prioritäten gehören:

- Quellenangaben und Provenienzinformationen;
- Prüfung von Pflichtfeldern und JSON-Konsistenz;
- Erkennung von Dubletten und widersprüchlichen Datensätzen;
- redaktionelle Prüfung der englischen, französischen und deutschen Beschreibungen;
- bessere Abdeckung regionaler und diasporischer Varianten;
- Dokumentation redaktioneller Entscheidungen und Unsicherheiten;
- automatisierte Validierung und versionierte Veröffentlichungen.

## Roadmap

Geplante Verbesserungen umfassen:

- ein dokumentiertes JSON-Schema;
- Validierungsskripte und GitHub Actions;
- Quellen- und Provenienzfelder auf Eintragsebene;
- klarere Kennzeichnungen für Vertrauens- und Prüfstatus;
- zusätzliche regionale Romanisierungen und Diaspora-Varianten;
- mehrsprachige redaktionelle Prüfung;
- Integrationsbeispiele für Entwickler und Forscher;
- getaggte Datensatzversionen und Änderungsprotokolle.

Die Roadmap beschreibt beabsichtigte Arbeiten und kann sich mit der Weiterentwicklung des Projekts ändern.

## Mitwirken

Beiträge sind insbesondere in folgenden Bereichen willkommen:

- sachliche Korrekturen mit verlässlichen Quellen;
- Belege für historische Ursprungstraditionen;
- Prüfung englischer, französischer und deutscher Übersetzungen;
- kantonesische, Hokkien-, Teochew-, Hakka- und weitere regionale Romanisierungen;
- Varianten aus überseechinesischen und diasporischen Gemeinschaften;
- JSON-Validierung und Werkzeuge zur Datenqualität;
- Dokumentation, Beispiele und Testfälle.

Bei größeren strukturellen Änderungen sollte vor einem Pull Request zunächst ein Issue eröffnet werden.

Sachliche Korrekturen sollten die verwendete Quelle nennen und erläutern, welches Feld geändert werden soll. Wenn Quellen voneinander abweichen, sollten die konkurrierenden Deutungen dokumentiert werden, anstatt eine davon stillschweigend zu ersetzen.

Beiträge dürfen keine privaten personenbezogenen Daten oder unbelegten Behauptungen über lebende Personen enthalten.

## Empfohlene Zitierweise

```text
Chinese Surnames Dataset.
Gepflegt von liziqing und Mitwirkenden.
https://github.com/liziqing/chinese-surnames-dataset
```

Bei der Weitergabe einer veränderten Fassung sollte die verwendete Version angegeben und die vorgenommenen Änderungen klar gekennzeichnet werden.

## Lizenz

Code und Validierungsskripte dieses Repositorys stehen unter der [MIT-Lizenz](LICENSE).

Die Datendatei `surnames.json` wird unter der **Creative Commons Attribution 4.0 International License (CC BY 4.0)** bereitgestellt.

Empfohlene Namensnennung:

```text
Chinese Surnames Dataset, gepflegt von liziqing und Mitwirkenden,
https://github.com/liziqing/chinese-surnames-dataset,
lizenziert unter CC BY 4.0.
```

Die Namensnennung kann in der Dokumentation, in Credits, in den Metadaten des Datensatzes oder an einer anderen angemessenen Stelle erfolgen.

## Pflege

Gepflegt von **liziqing** und Mitwirkenden aus der Community.

Das Projekt entstand aus fortlaufender Forschung zur chinesischen Namenskultur und zur interkulturellen Interpretation von Namen, darunter Arbeiten im Rahmen der FindChineseName-Initiative. Es wird als offene Ressource für öffentliche Weiterverwendung, Forschung, Bildung und Softwareentwicklung veröffentlicht. Die Nutzung des Datensatzes setzt keinen kommerziellen Dienst voraus.
