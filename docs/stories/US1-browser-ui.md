# US1: Interface im Browser erreichbar

**Als** neuer Mitarbeiter **möchte ich** ein User Interface im Browser aufrufen können.

Status: umgesetzt

## Akzeptanzkriterien

- [x] Ein Befehl startet die Oberfläche: `make run`.
- [x] Unter http://127.0.0.1:8000 ist ein Chat mit dem Agenten `hr_agent` erreichbar.
- [x] Gespräche bleiben nur im Arbeitsspeicher (`memory://`); es entsteht kein `.adk/`-Ordner.

Umsetzung: ADK-Entwickleroberfläche `adk web` ([ADR 0001](../adr/0001-agent-framework.md)). Ein eigenes UI steht auf der [Roadmap](../roadmap.md).
