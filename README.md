# Münchner Open-Data-Monitor

**Welche Datensätze hat die Stadt München identifiziert – und welche davon sind heute tatsächlich als Open Data verfügbar?**

Dieses Projekt dokumentiert den Stand der Veröffentlichung kommunaler Daten in München. Ausgangspunkt ist eine Bestandsaufnahme der Landeshauptstadt aus dem Jahr 2022 mit **96 Datensätzen bzw. potenziellen Datenangeboten** verschiedener Referate und städtischer Unternehmen.

Die ursprüngliche Liste wird mit dem öffentlich verfügbaren Datenangebot im Oktober 2026 abgeglichen. Ziel ist es, Fortschritte, Lücken und Hindernisse bei der Bereitstellung offener Verwaltungsdaten nachvollziehbar zu machen.

## Ergebnisse

**Stand der Untersuchung: 25. Oktober 2026**

| Veröffentlichungsstatus                        | Anzahl |
| ---------------------------------------------- | -----: |
| ✅ Offen verfügbar                              |     59 |
| 🟡 Teilweise verfügbar                         |     16 |
| 📄 Öffentlich zugänglich, offene Lizenz unklar |     13 |
| ❌ Keine passende Quelle nachgewiesen           |      8 |
| **Gesamt**                                     | **96** |

Die Zahlen beruhen auf einer unabhängigen Recherche im Münchner Open-Data-Katalog, in den Geodiensten der Stadt und auf Fachseiten. Für jeden Eintrag mit Fundstelle ist die Datensatzseite oder der Dienst verlinkt. Lizenzen sind nach der Regel des Katalogs eingetragen (DL-DE-BY 2.0, für MVV- und MVG-Daten CC BY 4.0); wie belastbar die einzelne Angabe ist, hält eine Belegstufe je Zeile fest, Details in der [Methodik](METHODIK.md).

„Heute verfügbar“ bedeutet nicht „Datenstand 2026“: Manche Dateien enden 2023 oder 2024. Öffentliche Sichtbarkeit, technische Abrufbarkeit und offene Lizenz sind drei verschiedene Dinge. Gerade bei Familienangeboten, Jugendhilfe, Unterkünften und einigen Umweltkarten ist die technische Veröffentlichung weiter als die dokumentierte Freigabe zur Weiterverwendung.

Ein Datensatz gilt nicht bereits deshalb als offen, weil die entsprechenden Informationen auf einer Webseite oder in einem PDF öffentlich zugänglich sind.

Die 96 Einträge sind außerdem **keine 96 getrennten Dateien**: Mehrere Einträge der Liste von 2022 (etwa die fünf GEWOFAG-Positionen oder die vier Tierpark-Kennzahlen) werden heute in jeweils einem einzigen Datensatz veröffentlicht.

## Hintergrund

### 2022: Bestandsaufnahme kommunaler Datensätze

Im Mai 2022 dokumentierte die Landeshauptstadt München die Ergebnisse einer verwaltungsinternen Open-Data-Abfrage bei Referaten, Eigenbetrieben und städtischen Gesellschaften.

Die Liste umfasst unter anderem Daten aus den Bereichen Mobilität, Wohnen, Stadtplanung, Umwelt, Bildung, Kultur und Verwaltung.

**Quelle:** [Ergebnisse und Ableitungen der OpenData-Abfrage – Sitzungsvorlage V 05865](https://www.muenchen-transparent.de/dokumente/7132160)

### 2025: Hochwertige Datensätze identifizieren

Im Oktober 2025 beschloss München einen weiteren Ansatz zur Identifikation besonders relevanter Datensätze. Dabei wird ausdrücklich auf das Projekt „Berlins Kerndatensätze“ Bezug genommen.

**Quelle:** [Hochwertige Datensätze identifizieren – Sitzungsvorlage V 17861](https://www.muenchen-transparent.de/dokumente/9285003)

Die Bestandsaufnahme von 2022 ist allerdings nicht mit einer offiziellen Priorisierung hochwertiger Datensätze gleichzusetzen.

## Datensatzübersicht

Die Untersuchung erfasst für jeden der 96 Einträge:

- Ursprüngliche Bezeichnung und zuständige Stelle
- Veröffentlichungsstatus im Jahr 2026
- Fundstelle bzw. Download-Link
- Dateiformat und Lizenz, soweit ermittelbar
- Einschränkungen und Unterschiede zum ursprünglich genannten Datensatz
- Datum der letzten Überprüfung

Die Ergebnisse liegen als maschinenlesbare CSV-Dateien und als Markdown-Tabelle vor:

| Datei | Inhalt |
| --- | --- |
| [berichte/2026-10-25.md](berichte/2026-10-25.md) | Alle 96 Einträge mit Status und Rechercheanmerkung als Tabelle |
| [daten/bestandsaufnahme-2022.csv](daten/bestandsaufnahme-2022.csv) | Die ursprüngliche Liste aus der Sitzungsvorlage von 2022 (historische Basis, wird nicht überschrieben) |
| [daten/verfuegbarkeit-2026-10-25.csv](daten/verfuegbarkeit-2026-10-25.csv) | Bewertung der Verfügbarkeit zum 25. Oktober 2026 |
| [METHODIK.md](METHODIK.md) | Statusdefinitionen, Spaltenbeschreibung und Anforderungen an Belege |
| [QUELLEN.md](QUELLEN.md) | Offizielle Dokumente und Vergleichsprojekte |

Die Markdown-Tabelle wird mit `python3 skripte/bericht_erzeugen.py` aus den beiden CSV-Dateien erzeugt und sollte nicht von Hand bearbeitet werden.

## Ziel des Projekts

Der Monitor soll sichtbar machen, welche kommunalen Daten bereits offen bereitstehen und wo weiterhin Lücken bestehen.

Er dient als Grundlage für weitere Recherchen, datenjournalistische Auswertungen, zivilgesellschaftliche Projekte und die Diskussion über kommunale Datentransparenz.

Die Untersuchung versteht sich ausdrücklich **nicht als offizielle Bewertung der Landeshauptstadt München**, sondern als unabhängige, fortschreibbare Bestandsaufnahme.

## Mitmachen

Ergänzungen und Korrekturen sind willkommen. Wer einen bislang nicht erfassten Datensatz findet oder eine fehlerhafte Einstufung entdeckt, kann einen Issue oder Pull Request erstellen.

Bitte möglichst die Datenquelle (direkte URL der Datensatzseite oder Schnittstelle), die Lizenz und das Datum der Überprüfung angeben. Die Liste von 2022 bleibt als historische Basis unverändert; Änderungen am Status gehören in die datierte Verfügbarkeitsdatei oder in einen neuen, datierten Stand.

## Lizenz

Alle eigenen Inhalte dieses Repositories (Texte, CSV-Dateien, Skripte) stehen unter [CC0 1.0 Universal](LICENSE) und dürfen ohne Einschränkung weiterverwendet werden.

Nicht davon erfasst sind die verlinkten Sitzungsvorlagen der Landeshauptstadt München und die Datensätze der Stadt selbst. Für sie gelten die Nutzungsbedingungen der jeweiligen Stelle; die in den Tabellen genannten Lizenzen (etwa CC BY 4.0) beziehen sich auf diese Originaldaten.

## Verwandte Projekte

- [awesome-munich-data](https://github.com/tifa365/awesome-munich-data) – Sammlung offener Münchner Datenquellen, Schnittstellen und Projekte
- [Berlins Kerndatensätze](https://odis-berlin.de/projekte/2023-02-kerndatens%C3%A4tze/) – Projekt zur Identifikation und Priorisierung relevanter Verwaltungsdaten

---

*Unabhängiges, nichtkommerzielles Projekt. Keine offizielle Veröffentlichung der Landeshauptstadt München.*
