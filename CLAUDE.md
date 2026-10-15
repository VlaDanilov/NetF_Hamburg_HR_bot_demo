# Regeln für KI-gestützte Entwicklung in diesem Repo

## Daten und Datenschutz
- Nur synthetische Daten. Keine echten Namen, Dokumente oder personenbezogenen Daten ins Repo.
- Keine Identität in Logs: keine Nutzer- oder Session-IDs, keine Nachrichtentexte, keine Uhrzeiten (siehe `docs/stories/AS1-topic-logging.md`).
- Secrets nur in `.env` (git-ignoriert). Vor jedem Commit prüfen, dass kein Key gestaged ist.

## Code
- Nur `hr_agent/agent.py` importiert ADK; `context.py` und `prompts.py` bleiben framework-frei.
- Die Instruktion bleibt eine Funktion, keine String-Instruktion: ADK ersetzt `{…}` in Strings.
- `adk web` nur mit In-Memory-Sessions starten (`make run`).
- ADK- und Gemini-APIs ändern sich schnell: in der installierten Version bzw. auf adk.dev und ai.google.dev prüfen, nichts aus dem Gedächtnis.
- Versionen und Modell-ID bleiben exakt gepinnt; Änderungen nur mit Eval-Lauf davor und danach.
- Tool-Eingaben im Code validieren, nicht nur per Prompt-Regel.
- Nutzersichtbare Texte auf Deutsch.

## Prüfen
- Nach jeder Änderung `make test`. Nach Änderungen an Prompt, Modell oder Daten zusätzlich `make eval` (kostet API-Anfragen).
- Fehlschlagende Tests an der Ursache beheben, nie abschwächen.
