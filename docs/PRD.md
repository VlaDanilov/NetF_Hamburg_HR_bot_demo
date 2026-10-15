# KI-Agent für HR-Abteilung

## 1. Kontext & Idee
Für unsere Personalabteilung soll ein KI-Agent erstellt werden, der einfache Antwort auf alltägliche Fragen geben kann. Hierdurch sollen die Kolleginnen und Kollegen ihre wertvolle Arbeitszeit auf die komplizierteren Aufgaben konzentrieren können.

In einer ersten Version des KI-Agenten wollen wir die typischen Onboarding-Informationen für neue Mitarbeiter und Mitarbeiterinnen der Firma als Kontext zur Verfügung stellen. Ein einfaches Chat-Interface kann den Starterinnen und Startern bei ihrer neuen Arbeit als Werkzeug dienen. Organisatorische Fragen können schnell und unkompliziert mit dem Chat-Agenten geklärt werden.

---

## 2. Scope für die erste Version des Chat-Agenten

Anfangs wollen wir die bestehende Dokumentation (liegt als PDF Dokumente vor) als Kontext verwenden. Für eine kleine Python Applikation können wir ein Framework wie Google Agent Development Kit, Pydantic oder CrewAI verwenden.

### 2.1 User Stories
* **US1: Interface erreichbar**
  Als neuer Mitarbeiter möchte ich ein User Interface im Browser aufrufen können.

* **US2: Agent antwortet auf Chat-Anfrage**
  Als neuer Mitarbeiter möchte ich meine Anfrage an den Agenten stellen und eine Antwort erhalten.

* **US3: Agent gibt eine Antwort auf Basis des Kontexts**
  Als neuer Mitarbeiter möchte ich, dass meine Frage nicht nur auf Basis des LLM-Wissens beantwortet wird. Der Chat-Agent soll die Kontext-Dateien berücksichtigen und die Antwort auf meine Frage so detailliert wie möglich mit dem Kontext des Unternehmens beantworten.


---

## 3. Weiterentwicklung
*Diese Ideen sollen als Dikussionsgrundlage dienen. Im Gespräch möchten wir auf die Möglichkeiten eingehen und schauen, wie wir zu einer Feature-Roadmap kommen können.*

### Beispiele
### Ausbaustufe 1: Chat-Agent kann auf Tools zugreifen
* **Kontext**: Die HR-Abteilung möchte wissen, welche Themen oft mit dem Chat-Agenten besprochen werden.
* **Anforderung**: Der Chat-Agent braucht ein Tool, mit dem die Haupt-Themen einer Unterhaltung erfasst und lokal gespeichert werden können.

### Ausbaustufe 2: Chat-Agent kann bei anderen Agenten nachfragen
* **Kontext**: Manchmal ist eine Anfrage nicht direkt im zur Verfügung stehenden Kontext zu finden. Es kann dann nützlich sein, wenn ein Multi-Agenten-System aufgesetzt wird, um eine Anfrage von Experten-Agenten bearbeiten zu lassen.
* **Anforderung**: Der Chat-Agent braucht die Möglichkeit, eine Rückfrage bei einem anderen Agenten zu stellen.

---# Netfond-Gemini_HR_agent_demo
