# ADR 0001: Agent-Framework – Google ADK

Status: angenommen · 2026-10-15

## Kontext

Wir brauchen einen Chat-Agenten mit Browser-Oberfläche (US1), der auf Deutsch antwortet (US2) und sich auf die Onboarding-PDFs stützt (US3). Danach folgen ein Tool (AS1) und Experten-Agenten (AS2). Das PRD nennt Google ADK, Pydantic AI und CrewAI.

## Entscheidung

**Google Agent Development Kit (`google-adk` 2.11.0).**

- `adk web` bringt Chat-Oberfläche und Session-Verwaltung mit. US1 ist damit ohne eigenes Frontend erfüllt.
- Normale Python-Funktionen werden zu Tools (AS1).
- Sub-Agents, `AgentTool` und A2A decken AS2 ab.
- ADK stammt vom selben Anbieter wie Gemini.

## Alternativen

| Option | Warum nicht (jetzt) |
| --- | --- |
| Pydantic AI | Typsicher und modellunabhängig, aber ohne fertige Chat-Oberfläche. Für US1 bräuchte es zusätzlich z. B. Streamlit. |
| CrewAI | Für mehrstufige Multi-Agenten-Abläufe gebaut; für einen einzelnen Q&A-Agenten zu viel Abstraktion. |
| LangGraph | Feine Kontrolle über Zustand und Abläufe, aber mehr Boilerplate als nötig. |
| Ohne Framework (`google-genai`) | Wenigste Abhängigkeiten; Sessions, Tool-Schleife und UI wären Eigenbau. |

## Konsequenzen

- Nur `hr_agent/agent.py` importiert ADK; `context.py` und `prompts.py` sind reines Python.
- `adk web` ist eine Entwickler-Oberfläche, kein Produkt-UI (siehe Roadmap).
- ADK ändert sich schnell: Version exakt gepinnt, Upgrades nur mit Eval-Lauf.
- Drei ADK-Standardverhalten sind im Code abgefangen:
  - Eine Instruktion als String wird als Template behandelt (`{name}` führt zu einem Fehler). Deshalb übergeben wir eine Funktion.
  - `adk web` speichert Sessions auf der Festplatte. Deshalb startet `make run` mit `memory://`.
  - Ohne Konfiguration gibt es keine Wiederholung bei Serverfehlern. Deshalb sind Retries für 408/5xx gesetzt.
