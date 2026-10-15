# AS1: Themen von Gesprächen anonym erfassen

**Als** Personalabteilung **möchte ich** wissen, welche Themen oft besprochen werden, **damit** wir die Onboarding-Unterlagen gezielt verbessern können.

Status: offen – Umsetzung in der Live-Session

## Leitplanke: nur anonyme Aggregate

Ein Log, das einer Person zugeordnet werden kann, wäre Verhaltensüberwachung:
- Mitbestimmung des Betriebsrats nach § 87 Abs. 1 Nr. 6 BetrVG,
- Hochrisiko-System nach EU AI Act, Anhang III Nr. 4(b).

Deshalb speichert das Log **keine** Nutzer- oder Session-ID, **keinen** Nachrichtentext, **keine** Uhrzeit und **keinen** Freitext außer einem kurzen Themen-Label. Siehe [compliance.md](../compliance.md).

## Spezifikation

1. **Tool:** `log_topic(topic: str, category: str) -> dict` in `hr_agent/tools/topic_log.py`, registriert mit `tools=[log_topic]` in `hr_agent/agent.py`. ADK macht aus der Funktion automatisch ein Tool (Docstring + Type Hints).
2. **Speicher:** eine JSON-Zeile pro Aufruf in `data/topics.jsonl` (Pfad als Modulkonstante `TOPICS_FILE`), genau diese Schlüssel:
   ```json
   {"date": "2026-10-15", "topic": "Urlaubsantrag", "category": "Urlaub"}
   ```
3. **Kategorien (fest):** `Arbeitszeit`, `Urlaub`, `IT`, `Benefits`, `Sonstiges`. Eine andere Kategorie wird abgelehnt (`{"status": "error", …}`) und nicht geschrieben.
4. **Themen-Label:** 2–40 Zeichen, höchstens 4 Wörter, nur Buchstaben, Leerzeichen, Bindestrich. Keine Ziffern, kein `@`. Ungültige Labels werden abgelehnt.
5. **Erfolg:** `{"status": "ok"}`. Ein Schreibfehler wird abgefangen und als Fehlerstatus zurückgegeben; die Antwort an den Nutzer scheitert nie daran.
6. **Instruktion:** neue Regel: „Rufe `log_topic` einmal pro Onboarding-Frage auf, mit einem kurzen, allgemeinen Label ohne persönliche Daten.“
7. **Transparenz:** Der KI-Hinweis bekommt den Satz: „Zur Verbesserung der Unterlagen werden Themen anonym und ohne Personenbezug gezählt.“
8. **Aufbewahrung:** `make purge-topics` löscht Einträge älter als 90 Tage.

## Akzeptanztests (`tests/test_topic_log.py`, ohne API-Key)

- [ ] Ein gültiger Aufruf schreibt genau eine JSON-Zeile mit genau `date`, `topic`, `category`.
- [ ] Unbekannte Kategorie → abgelehnt, Datei unverändert.
- [ ] Labels mit Ziffern, `@`, mehr als 4 Wörtern oder mehr als 40 Zeichen → abgelehnt.
- [ ] **Log enthält keine personenbezogenen Daten:** keine Namen, keine Ziffern außer im Datum, kein `@`, keine weiteren Schlüssel.
- [ ] `date` im Format `YYYY-MM-DD`, ohne Uhrzeit.
- [ ] Purge entfernt Einträge älter als 90 Tage und behält jüngere.
- [ ] Schreibfehler → Fehlerstatus, keine Exception.
- [ ] `make test` bleibt grün; `make eval` zeigt keine Verschlechterung.

## Diskussionspunkte

- **Freies Label oder feste Themenliste?** Eine feste Liste schließt persönliche Daten aus, liefert aber weniger Erkenntnis.
- **Doppelzählung:** ein Aufruf pro Frage zählt mehrfach pro Gespräch. Deduplizieren ginge über den Session-State (im Speicher, nie im Log).
- **Re-Identifikation:** In kleinen Teams kann schon ein Datum Rückschlüsse erlauben. Auswertungen deshalb nur aggregiert mit Mindestanzahl, ggf. Woche statt Tag speichern.
