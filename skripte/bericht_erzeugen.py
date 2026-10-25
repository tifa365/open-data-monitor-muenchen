#!/usr/bin/env python3
"""Erzeugt die Markdown-Tabelle in berichte/ aus den beiden CSV-Dateien.

Aufruf aus dem Projektverzeichnis:
    python3 skripte/bericht_erzeugen.py [STAND]
STAND ist das Datum des Verfügbarkeitsstands (Standard: 2026-10-25).
"""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAND = sys.argv[1] if len(sys.argv) > 1 else "2026-10-25"

LABELS = {
    "open": "✅ Offen verfügbar",
    "partial": "🟡 Teilweise verfügbar",
    "public_only": "📄 Öffentlich zugänglich, offene Lizenz unklar",
    "not_found": "❌ Keine passende Quelle nachgewiesen",
}
ORDER = ["open", "partial", "public_only", "not_found"]


def md(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def datum_de(iso: str) -> str:
    j, m, t = iso.split("-")
    return f"{int(t)}. {['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'][int(m)-1]} {j}"


def main() -> None:
    with open(ROOT / "daten" / "bestandsaufnahme-2022.csv", encoding="utf-8", newline="") as f:
        inventar = {r["id"]: r for r in csv.DictReader(f)}
    with open(ROOT / "daten" / f"verfuegbarkeit-{STAND}.csv", encoding="utf-8", newline="") as f:
        bewertung = list(csv.DictReader(f))

    fehlend = set(inventar) ^ {r["id"] for r in bewertung}
    if fehlend:
        sys.exit(f"IDs stimmen nicht überein: {sorted(fehlend, key=int)}")
    unbekannt = {r["status"] for r in bewertung} - set(LABELS)
    if unbekannt:
        sys.exit(f"Unbekannte Statuswerte: {unbekannt}")

    zaehler = Counter(r["status"] for r in bewertung)
    out = []
    out.append(f"# Verfügbarkeit der 96 Datensätze aus der Bestandsaufnahme 2022 – Stand {datum_de(STAND)}\n")
    out.append(
        "Die Tabelle verbindet die **ursprüngliche Liste der Stadtverwaltung aus dem Jahr 2022** mit einer "
        f"**unabhängigen Einschätzung der Verfügbarkeit zum {datum_de(STAND)}**. Die Einstufungen stammen aus "
        "einer unabhängigen Recherche im Münchner Open-Data-Katalog, in den Geodiensten und auf Fachseiten. "
        "Für Katalogdatensätze gilt grundsätzlich DL-DE-BY 2.0, für MVV- und MVG-Daten CC BY 4.0; Abweichungen "
        "stehen in der Lizenzspalte. Statusdefinitionen, Spalten und Belegstufen: [METHODIK.md](../METHODIK.md).\n"
    )
    out.append("| Status | Anzahl |\n| --- | ---: |")
    for s in ORDER:
        out.append(f"| {LABELS[s]} | {zaehler.get(s, 0)} |")
    out.append(f"| **Gesamt** | **{len(bewertung)}** |\n")
    tabelle = []
    tabelle.append("| Nr. | Stelle (2022) | Datensatz / Datenangebot (2022) | Vermerk 2022 | Status 2026 | Einstufung im Detail | Rechercheanmerkung | Fundstelle | Lizenz |")
    tabelle.append("| ---: | --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in sorted(bewertung, key=lambda r: int(r["id"])):
        i = inventar[r["id"]]
        url = r.get("dataset_url", "").strip()
        weitere = r.get("additional_urls", "").split()
        fundstelle = f"[Link]({url})" if url else "–"
        if weitere:
            fundstelle += ", " + ", ".join(f"[Link {n}]({u})" for n, u in enumerate(weitere, start=2))
        lizenz = r.get("license", "").strip()
        lurl = r.get("license_url", "").strip()
        lizenz_md = f"[{md(lizenz)}]({lurl})" if lizenz and lurl else (md(lizenz) if lizenz else "–")
        tabelle.append(
            f"| {r['id']} | {md(i['provider_2022'])} | {md(i['dataset_title_2022'])} | {md(i['administrative_note_2022'])} "
            f"| {LABELS[r['status']]} | {md(r['status_detail'])} | {md(r['assessment_notes'])} | {fundstelle} | {lizenz_md} |"
        )
    out.extend(tabelle)
    out.append(
        "\nQuellen: [Sitzungsvorlage V 05865 (2022)](https://www.muenchen-transparent.de/dokumente/7132160), "
        "[Sitzungsvorlage V 17861 (2025)](https://www.muenchen-transparent.de/dokumente/9285003). "
        "Die Einstufung ist eine unabhängige Recherche und keine offizielle Bewertung der Landeshauptstadt München.\n"
    )
    ziel = ROOT / "berichte" / f"{STAND}.md"
    ziel.write_text("\n".join(out), encoding="utf-8")
    print(f"{ziel.relative_to(ROOT)} geschrieben: {len(bewertung)} Zeilen, {dict(zaehler)}")

    # Dieselbe Tabelle zwischen den Markierungen in der README einsetzen.
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    a, e = "<!-- TABELLE:ANFANG -->", "<!-- TABELLE:ENDE -->"
    start, ende = text.find(a), text.find(e)
    if start == -1 or ende == -1 or ende < start:
        sys.exit("Markierungen TABELLE:ANFANG/TABELLE:ENDE in README.md nicht gefunden")
    neu = text[: start + len(a)] + "\n" + "\n".join(tabelle) + "\n" + text[ende:]
    if neu != text:
        readme.write_text(neu, encoding="utf-8")
        print("README.md aktualisiert")
    else:
        print("README.md unverändert")


if __name__ == "__main__":
    main()
