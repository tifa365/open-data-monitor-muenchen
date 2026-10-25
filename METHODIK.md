# Methodik und Nachvollziehbarkeit

## Grundlage der Liste

Ausgangspunkt ist die Sitzungsvorlage 20-26 / V 05865 des Münchner Stadtrats aus dem Mai 2022 („Ergebnisse und Ableitungen der OpenData-Abfrage bei Referaten, Eigenbetrieben und Gesellschaften der LH München“). Die 96 Einträge werden mit ihrer laufenden Nummer (1–96), der meldenden Stelle und dem ursprünglichen Vermerk der Verwaltung übernommen. Diese Liste ist die **historische Basis** und wird nicht überschrieben. Korrekturen (etwa Übertragungsfehler) sind im Versionsverlauf zu begründen.

## Stand der Recherche

**Prüfdatum: 25. Oktober 2026.** Die 96 Einträge wurden mit dem Münchner Open-Data-Katalog (opendata.muenchen.de) abgeglichen; passende Downloads und Geodienste wurden aufgerufen, ergänzend wurde auf den Fachseiten der Stadt recherchiert. Für jede Zeile mit Fundstelle ist die Datensatzseite oder der Dienst verlinkt.

„Heute verfügbar“ heißt nicht „Datenstand 2026“: Manche Dateien enden 2023 oder 2024. Solche Einschränkungen stehen in der Rechercheanmerkung.

### Lizenzangaben

Für die verlinkten Datensätze des Münchner Open-Data-Katalogs gilt grundsätzlich die Datenlizenz Deutschland – Namensnennung – Version 2.0 (DL-DE-BY 2.0). MVV- und MVG-Daten stehen unter CC BY 4.0. Die Lizenzspalte ist nach dieser Regel befüllt; die Belegstufe (siehe unten) hält fest, ob die Lizenz in der Recherche ausdrücklich genannt wurde oder aus der allgemeinen Katalogregel folgt. Bei Einträgen mit Status `public_only` oder `not_found` bleibt die Lizenzspalte leer, weil gerade keine offene Lizenz belegt ist.

## Statusdefinitionen

| Wert in der CSV | Anzeige | Bedeutung |
| --- | --- | --- |
| `open` | ✅ Offen verfügbar | Ein direkt entsprechender oder im Wesentlichen übereinstimmender Datensatz steht nach der Recherche maschinenlesbar zum Download oder als offen nutzbarer Dienst bereit, mit einer erkennbaren offenen Lizenz. |
| `partial` | 🟡 Teilweise verfügbar | Nur ein Teil des ursprünglich genannten Datensatzes, eine historische Fassung oder ein verwandter, aber nicht identischer Datensatz wurde gefunden. |
| `public_only` | 📄 Öffentlich zugänglich, offene Lizenz unklar | Eine Webseite, ein PDF oder ein öffentlich abrufbarer Dienst existiert, aber offene Nutzungsrechte oder Maschinenlesbarkeit konnten nicht festgestellt werden. |
| `not_found` | ❌ Keine passende Quelle nachgewiesen | Keine passende, offen lizenzierte Quelle gefunden. **Kein Beleg dafür, dass der Datensatz nicht existiert.** |

Ein Datensatz gilt nicht bereits deshalb als offen, weil seine Inhalte öffentlich einsehbar sind. Ein funktionierender WMS-Kartendienst ist nicht gleichbedeutend mit einem Vektordaten-Download, und ein erreichbarer Endpunkt ist kein Beleg für eine offene Lizenz.

## Spalten der CSV-Dateien

Die Spaltennamen sind bewusst englisch und ohne Umlaute gehalten, damit die Dateien ohne Anpassung in gängigen Werkzeugen verarbeitet werden können.

### `daten/bestandsaufnahme-2022.csv`

| Spalte | Inhalt |
| --- | --- |
| `id` | Laufende Nummer 1–96 aus der Sitzungsvorlage |
| `provider_2022` | Meldende Stelle (Referat, Eigenbetrieb, Gesellschaft) |
| `dataset_title_2022` | Bezeichnung des Datensatzes bzw. Datenangebots im Original |
| `administrative_note_2022` | Vermerk der Verwaltung 2022 (z. B. „Datensatz liegt vor“, „Bisher nur Nennung“, „GeoDaten“, „PDF“) |
| `source_document_url` | Link zur Sitzungsvorlage |

### `daten/verfuegbarkeit-2026-10-25.csv`

| Spalte | Inhalt |
| --- | --- |
| `id` | Verweis auf die Nummer in der Bestandsaufnahme 2022 |
| `status` | Einer der vier Werte `open`, `partial`, `public_only`, `not_found` |
| `status_detail` | Einstufung im Detail: Symbol und Kurzbezeichnung wie in `status`, ergänzt um Zusätze wie „als Kartendienst“ oder „historischer Bestand“ |
| `assessment_notes` | Rechercheanmerkung: gefundener Datensatz, Format, Abdeckung, Abweichungen |
| `dataset_url` | Direkte URL der Datensatzseite, des Dienstes oder der Fachseite |
| `additional_urls` | Weitere Fundstellen, durch Leerzeichen getrennt (z. B. zweiter Datensatz, Metadaten, Direktdownload) |
| `license` | Lizenzbezeichnung, z. B. `DL-DE-BY 2.0` oder `CC BY 4.0`; leer, wenn keine offene Lizenz belegt ist |
| `license_url` | Link zum Lizenztext |
| `evidence_checked_at` | Prüfdatum im Format `JJJJ-MM-TT` |
| `evidence_level` | Belegstufe, siehe unten |

### Belegstufen (`evidence_level`)

| Wert | Bedeutung |
| --- | --- |
| `url_license_stated` | Fundstelle verlinkt, Lizenz in der Recherche ausdrücklich festgestellt (MVV/MVG, Geothermie-Layer) |
| `url_license_catalog_rule` | Fundstelle im Open-Data-Katalog verlinkt; Lizenz nach der allgemeinen Katalogregel DL-DE-BY 2.0 eingetragen, nicht auf jeder Datensatzseite einzeln nachgelesen |
| `url_only` | Fundstelle verlinkt, keine offene Lizenz belegt (alle `public_only` sowie `not_found` mit verwandtem Angebot) |
| `no_url` | Keine Fundstelle (nur bei `not_found`) |

## Anforderungen an künftige Prüfungen

Für jede Zeile sollen festgehalten werden:

1. die direkte URL der offiziellen Datensatzseite oder der Schnittstelle,
2. eine ausdrücklich genannte Lizenz oder ein Link auf die Lizenzangabe,
3. was tatsächlich eingesehen oder heruntergeladen wurde,
4. das Prüfdatum,
5. Einschränkungen bei Raumbezug, Aktualisierungsrhythmus, Zeitraum, Maschinenlesbarkeit oder Vollständigkeit.

## Fortschreibung

Ein neuer Stand (z. B. `verfuegbarkeit-2027-10-25.csv`) wird als zusätzliche Datei angelegt, statt den Stand vom Oktober 2026 zu überschreiben. So bleibt die Entwicklung über die Jahre vergleichbar. Die Markdown-Tabelle im Ordner `berichte/` wird mit `skripte/bericht_erzeugen.py` aus den CSV-Dateien erzeugt.
