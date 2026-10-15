# Compliance: EU AI Act und DSGVO

Stand: 2026-10-15 · **Keine Rechtsberatung.** Diese Seite dokumentiert technische Entscheidungen und ersetzt nicht die Prüfung durch Datenschutzbeauftragte oder Rechtsabteilung.

## 1. Einordnung nach dem EU AI Act

- **Kein Hochrisiko-System.** [Anhang III Nr. 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3) (Beschäftigung) erfasst:
  - (a) Einstellung und Auswahl,
  - (b) Entscheidungen über Arbeitsbedingungen, Beförderung oder Kündigung, Aufgabenzuweisung nach Verhalten sowie die Überwachung und Bewertung von Leistung und Verhalten.

  Ein Assistent für organisatorische Onboarding-Fragen fällt unter keinen dieser Punkte. Das gilt nur, solange seine Daten nie zur Überwachung oder Bewertung einzelner Beschäftigter genutzt werden. Art. 6 Abs. 3 ist nicht einschlägig: Er regelt Ausnahmen für Systeme, die in Anhang III gelistet *sind*.
- **Transparenz ([Art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)), gilt seit 2. August 2026:** Nutzer müssen spätestens bei der ersten Interaktion erfahren, dass sie mit einem KI-System sprechen. Umsetzung: KI-Hinweis in der ersten Antwort jedes Gesprächs, vom Eval in jedem Fall geprüft.
- **Fristen:** Die [Verordnung (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) hat den AI Act geändert. Hochrisiko-Pflichten nach Anhang III gelten ab 2. Dezember 2027; Art. 50 wurde nicht verschoben.

## 2. Vor einem Produktivbetrieb

1. **Kein Free Tier mit echten Daten.** Google nutzt Eingaben im Free Tier zur Produktverbesserung, und für Nutzer im EWR sind nur Paid Services zulässig ([Gemini API Terms](https://ai.google.dev/gemini-api/terms)). Stattdessen: kostenpflichtige API oder Gemini Enterprise Agent Platform mit EU-Endpunkt, dazu ein Auftragsverarbeitungsvertrag ([Art. 28 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).
2. **Datenschutzhinweis (Art. 13 DSGVO)** im UI, vor der ersten Nachricht.
3. **Speicherfristen und Löschung (Art. 5 Abs. 1 lit. c, e DSGVO):** Sessions nur im Arbeitsspeicher; Themen-Log (AS1) 90 Tage, Löschung per `make purge-topics`.
4. **Themen-Log ohne Personenbezug.** Ein personenbezogenes Log wäre Leistungs- und Verhaltensüberwachung: Hochrisiko nach Anhang III Nr. 4(b) und Mitbestimmung des Betriebsrats nach [§ 87 Abs. 1 Nr. 6 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html).
5. **Gesundheitsdaten (Art. 9 DSGVO):** Der Agent fragt nicht danach und wiederholt sie nicht; der Hinweis bittet, keine persönlichen Daten einzugeben.
6. **KI-Kompetenz ([Art. 4 AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)):** Schulung der HR-Mitarbeitenden, die Unterlagen pflegen und Auswertungen lesen.
7. **Prüfung durch die/den Datenschutzbeauftragte(n)** vor dem Go-live, inklusive Schwellwertprüfung zur Datenschutz-Folgenabschätzung (Art. 35 DSGVO).

## 3. Status

| Anforderung | Demo | Maßnahme für Produktion |
| --- | --- | --- |
| KI-Hinweis (Art. 50 AI Act) | In der ersten Antwort, per Eval geprüft | Fester Hinweis im UI vor der ersten Nachricht |
| Keine Hochrisiko-Nutzung | Erfüllt: keine Überwachung | Schriftliche Regel: Logs nie personenbezogen |
| Daten | Nur synthetische Daten | Echte Unterlagen erst nach DSB-Prüfung |
| API-Tarif, AVV (Art. 28 DSGVO) | Free Tier, nur lokale Entwicklung | Paid / Enterprise Agent Platform mit EU-Endpunkt; AVV |
| Datenschutzhinweis (Art. 13 DSGVO) | Nicht nötig für die Demo | Im UI anzeigen |
| Speicherung und Löschung | Sessions nur im Speicher (`memory://`) | Fristen festlegen, Löschung testen |
| Themen-Log (AS1) | Noch nicht gebaut; spezifiziert ohne Personenbezug | Nur Aggregate mit Mindestanzahl |
| Betriebsrat (§ 87 Abs. 1 Nr. 6 BetrVG) | Nicht betroffen | Informieren; Betriebsvereinbarung bei Auswertungen |
| KI-Kompetenz (Art. 4 AI Act) | – | Schulung der HR-Operatoren |
| DSB-Prüfung, DSFA-Schwellwert | – | Vor dem Go-live |
