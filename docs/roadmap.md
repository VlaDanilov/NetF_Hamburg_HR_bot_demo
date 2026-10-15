# Roadmap

Jeder Schritt hat einen Auslöser: Wir bauen ihn, wenn eine messbare Bedingung eintritt.

| Schritt | Auslöser | Aufwand | Hauptrisiko |
| --- | --- | --- | --- |
| [AS1 Themen-Log](stories/AS1-topic-logging.md) | HR will wissen, welche Themen häufig sind | Klein: ein Tool, eine Testdatei | Log enthält doch personenbezogene Daten |
| [AS2 Experten-Agenten](stories/AS2-expert-agents.md) (`AgentTool`; A2A für Agenten anderer Teams) | Viele Ablehnungen oder „Sonstiges“ zu einem Fachgebiet | Mittel | Falsches Routing; Experten antworten ohne Quelle |
| RAG (eigene Pipeline vs. Gemini File Search, Wahl per Messung) | Dokumente werden groß, ändern sich häufig oder brauchen Berechtigungen | Mittel bis groß | Suche verfehlt die richtige Seite |
| Eigenes UI + SSO + Datenschutzhinweis | Echte Nutzer über einen Pilot hinaus | Mittel | Wird zum Produktprojekt |
| Betrieb in EU-Region mit AVV | Vor den ersten echten Daten | Mittel | Free-Tier-Key oder globaler Endpunkt gelangt in Produktion |
| Eval in CI, Monitoring, Feedback-Buttons | Jede Prompt- oder Modelländerung nach dem Go-live | Klein bis mittel | Instabile Evals blockieren Releases; Feedback-Freitext enthält persönliche Daten |
