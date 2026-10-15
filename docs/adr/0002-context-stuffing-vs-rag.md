# ADR 0002: Alle Dokumente in die Instruktion statt RAG

Status: angenommen · 2026-10-15

## Kontext

Der Agent soll nur aus den Onboarding-PDFs antworten und die Quelle (Dokument, Seite) nennen. Es gibt 4 PDFs mit je 2 Seiten, zusammen rund 5.400 Zeichen. Das Modell akzeptiert rund 1 Million Eingabe-Tokens.

## Entscheidung

**Context Stuffing:** Beim Start werden alle Seiten mit pypdf gelesen, mit `[Dokument, Seite N]` markiert und vollständig in die Instruktion gelegt.

- Das Modell sieht immer alle Seiten. Es gibt keinen Suchschritt, der die richtige Stelle verfehlen kann.
- Keine Embeddings, kein Vektorspeicher, kein Chunking.
- Laden und Markierungen sind ohne API-Key testbar.

## Alternativen

| Option | Warum nicht (jetzt) |
| --- | --- |
| Eigene RAG-Pipeline (Chunking, Embeddings, Vektorsuche) | Viel Aufwand und eine neue Fehlerquelle (Suche verfehlt die Seite), bei 8 Seiten ohne Nutzen. |
| Gemini File Search (verwaltetes RAG) | Weniger Aufwand als eigenes RAG, aber weniger Kontrolle, und die Daten liegen bei Google. |
| PDFs direkt ans Modell | Das Modell sieht auch Bilder, aber wir haben keine Kontrolle über Seitenmarkierungen und weniger Testbarkeit. |

## Konsequenzen

- Jede Frage schickt die ganze Instruktion mit. Bei rund 2.000 Tokens ist das günstig.
- Geänderte PDFs werden erst nach einem Neustart sichtbar.
- Alle Mitarbeitenden sehen über den Agenten alle Dokumente. Das passt für allgemeine Onboarding-Infos.
- **Wechsel zu RAG, sobald eine dieser Bedingungen eintritt:**
  - die Dokumente erreichen Zehntausende Tokens,
  - sie ändern sich häufig,
  - nicht alle dürfen alle Dokumente sehen (Berechtigungen).

  Eigenes RAG oder File Search wird dann per Messung entschieden (Trefferquote auf dem Eval-Set).
