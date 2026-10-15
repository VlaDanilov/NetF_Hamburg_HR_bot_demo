# US2: Agent antwortet auf Chat-Anfrage

**Als** neuer Mitarbeiter **möchte ich** meine Anfrage an den Agenten stellen und eine Antwort erhalten.

Status: umgesetzt. Ein Eval-Fall mit `gemini-3.8-flash` bestanden (2026-10-15); vollständiger Lauf (`make eval`) ausstehend.

## Akzeptanzkriterien

- [ ] Antworten auf Deutsch, freundlich und knapp, in der Sie-Form.
- [ ] Die erste Antwort eines Gesprächs beginnt mit dem KI-Hinweis (EU AI Act Art. 50).
- [ ] Fragen ohne Onboarding-Bezug werden kurz abgelehnt.

Umsetzung: `LlmAgent` in `hr_agent/agent.py`, Texte in `hr_agent/prompts.py`. Der Hinweis hängt davon ab, dass das Modell die Regel befolgt; das Eval prüft ihn in jedem Fall. Für die Produktion ist ein fester Hinweis im UI vorgesehen.
