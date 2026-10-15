# ADR 0003: Modellwahl und Datenstandort

Status: angenommen · 2026-10-15

## Kontext

Der Agent beantwortet einfache Nachschlagefragen aus wenigen Seiten Text. Die Demo nutzt nur synthetische Daten. Im Produktivbetrieb würden Mitarbeitende in der EU auch persönliche Fragen stellen.

## Entscheidung

- **Modell: `gemini-3.8-flash`**, das aktuelle stabile Flash-Modell ([Modellübersicht](https://ai.google.dev/gemini-api/docs/models), Stand 2026-10-13): schnell, günstig, 1M-Token-Kontext.
  - Die ID ist exakt gepinnt, kein Alias wie `gemini-flash-latest`, damit sich das Verhalten nicht unbemerkt ändert.
  - `GEMINI_MODEL` in `.env` überschreibt sie ohne Codeänderung.
- **Demo:** Gemini API mit AI-Studio-Key (Free Tier), nur synthetische Daten, nur lokale Entwicklung.
- **Produktion:** kostenpflichtiges Projekt auf der Gemini Enterprise Agent Platform (früher Vertex AI) mit `eu`- oder Regional-Endpunkt (z. B. `europe-west3`) und Auftragsverarbeitungsvertrag.

## Alternativen

| Option | Bewertung |
| --- | --- |
| `gemini-3.5-flash-lite` | Günstiger und schneller; hat das Eval 10/10 bestanden (ein Lauf). Gute Ausweichoption, z. B. bei Überlastung oder erschöpftem Kontingent. |
| Pro-/Flaggschiff-Modelle | Stärkeres Reasoning, langsamer und teurer – für Nachschlagefragen nicht nötig. |
| Free Tier mit echten Daten | Ausgeschlossen. Laut [Gemini API Terms](https://ai.google.dev/gemini-api/terms) nutzt Google Eingaben im Free Tier zur Produktverbesserung, menschliche Prüfer können sie lesen, und für Nutzer im EWR sind nur Paid Services zulässig. |

## Konsequenzen

- Der Wechsel von der Demo zur Produktion ist vor allem Konfiguration (Projekt, Region, `GOOGLE_GENAI_USE_ENTERPRISE`), kaum Code.
- Das Free Tier ist klein: 20 Anfragen pro Tag und Modell für `gemini-3.8-flash` (beobachtet am 2026-10-14). Ein voller Eval-Lauf braucht 10. Für Demos daher einen Key mit Abrechnung verwenden oder auf Flash-Lite ausweichen.
- Gepinnte Modell-IDs werden irgendwann abgeschaltet. Die [Deprecations-Seite](https://ai.google.dev/gemini-api/docs/deprecations) muss beobachtet werden.
- Der globale Endpunkt garantiert keinen Datenstandort; der EU-Endpunkt muss explizit gewählt werden.
