# AS2: Rückfrage bei Experten-Agenten

**Als** neuer Mitarbeiter **möchte ich** auch dann eine fundierte Antwort bekommen, wenn meine Frage nicht in den Onboarding-Unterlagen steht, indem der Agent bei einem Experten-Agenten nachfragt.

Status: Roadmap – nicht Teil des MVP

## Optionen in ADK

| Variante | Verhalten | Eignung |
| --- | --- | --- |
| `sub_agents` (Übergabe) | Der Experte übernimmt das Gespräch. | Einfach, aber Zitier- und Datenschutzregeln gelten dann nicht automatisch weiter. |
| `AgentTool` (Agent als Werkzeug) | Der Onboarding-Agent ruft den Experten auf und formuliert die Antwort selbst. | **Bevorzugt:** Kontrolle, Quellen und Hinweis bleiben beim Onboarding-Agenten. |
| A2A-Protokoll | Aufruf eines Agenten über das Netzwerk, z. B. von einem anderen Team. | Für Agenten außerhalb dieses Repos (in ADK experimentell). |

## Akzeptanzkriterien (Entwurf)

- [ ] Ist eine Frage nicht in den Unterlagen, wählt der Agent anhand der `description` einen zuständigen Experten, sonst bleibt es bei der Ablehnung mit HR-Kontakt.
- [ ] Antworten eines Experten sind als solche gekennzeichnet und nennen ihre Quelle.
- [ ] Experten erhalten nur die Frage, keine persönlichen Daten aus dem Gespräch.
- [ ] Eval-Fälle für richtiges und falsches Routing.

**Auslöser:** Das Themen-Log (AS1) oder das Eval zeigt viele Ablehnungen oder „Sonstiges“ zu einem Fachgebiet.
