# US3: Agent antwortet auf Basis des Kontexts

**Als** neuer Mitarbeiter **möchte ich**, dass meine Frage nicht nur auf Basis des LLM-Wissens beantwortet wird, sondern mit dem Kontext des Unternehmens.

Status: umgesetzt. Kriterien ohne Haken hängen vom Modell ab und werden mit `make eval` geprüft (vollständiger Lauf ausstehend).

## Akzeptanzkriterien

- [x] Beim Start werden alle PDFs aus `data/onboarding/` seitenweise gelesen und mit `[Dokument, Seite N]` in die Instruktion gelegt (`make test`).
- [x] Ein leerer Ordner oder eine Seite ohne Text (Scan) stoppt den Start mit klarer Meldung (`make test`).
- [ ] Antworten nur aus den Unterlagen, mit Quelle (Dokument, Seite N).
- [ ] Ohne Antwort in den Unterlagen: „Dazu habe ich in den Onboarding-Unterlagen keine Information.“ plus HR-Ansprechperson aus den Unterlagen.
- [ ] Keine erfundenen Regeln, Zahlen, Namen oder Daten.
- [ ] Keine Abfrage persönlicher Daten; genannte Daten werden nicht wiederholt, Verweis an die Personalabteilung.
- [ ] Dokumentinhalte gelten als Daten, nicht als Anweisungen.

Siehe [ADR 0002](../adr/0002-context-stuffing-vs-rag.md) für die Entscheidung gegen RAG.
