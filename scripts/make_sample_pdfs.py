"""Generate synthetic onboarding PDFs for the fictional "Musterfirma GmbH".

Every document has exactly 2 pages so page citations can be tested.
Parental leave and company pension are deliberately not covered (refusal tests).

Run: make data
"""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "onboarding"
COMPANY = "Musterfirma GmbH"
FOOTER_NOTE = "Fiktive Beispieldaten – nur für Demozwecke"

# Per page: "## " starts a heading, a blank line separates paragraphs.
DOCUMENTS = [
    {
        "file": "01_erster_arbeitstag.pdf",
        "title": "Erster Arbeitstag",
        "pages": [
            """
            ## Ablauf des ersten Arbeitstags
            Bitte kommen Sie an Ihrem ersten Arbeitstag um 9:00 Uhr an den Empfang
            im Hauptgebäude, Musterstraße 1, 12345 Musterstadt.

            9:00 Uhr: Empfang und Ausgabe des Mitarbeiterausweises.

            9:30 Uhr: Begrüßung durch die Personalabteilung.

            10:30 Uhr: Übergabe von Laptop und Benutzerkonto durch den IT-Service-Desk.

            12:00 Uhr: Gemeinsames Mittagessen mit Ihrem Team.
            Die Kosten übernimmt die Musterfirma.

            14:00 Uhr: Rundgang durch das Gebäude.

            15:30 Uhr: Erstes Gespräch mit Ihrer Führungskraft.

            ## Buddy-Programm
            Jede neue Mitarbeiterin und jeder neue Mitarbeiter bekommt für die ersten
            drei Monate einen Buddy aus einem anderen Team. Das erste Treffen findet
            in der ersten Arbeitswoche statt.
            """,
            """
            ## Ansprechpartner
            Personalabteilung: Lena Hoffmann, Personalreferentin.
            E-Mail: personal@musterfirma.example, interne Durchwahl 120.
            Sie ist Ihre Ansprechpartnerin für alle Fragen, die in diesen Unterlagen
            nicht beantwortet werden.

            IT-Service-Desk: it-service@musterfirma.example, interne Durchwahl 300,
            Raum 0.14, erreichbar Montag bis Freitag von 8:00 bis 17:00 Uhr.

            ## IT-Zugang
            Ihr Benutzerkonto erhalten Sie am ersten Tag um 10:30 Uhr zusammen mit
            Ihrem Laptop. Das Initialpasswort müssen Sie bei der ersten Anmeldung ändern.

            Der Laptop wird im Raum 0.14 gegen Unterschrift ausgegeben.
            """,
        ],
    },
    {
        "file": "02_arbeitszeit_urlaub.pdf",
        "title": "Arbeitszeit & Urlaub",
        "pages": [
            """
            ## Gleitzeit und Kernzeit
            Die regelmäßige Wochenarbeitszeit beträgt 40 Stunden.
            Sie können Ihre Arbeitszeit im Gleitzeitrahmen von 7:00 bis 19:00 Uhr
            frei einteilen.

            Kernzeit ist Montag bis Donnerstag von 10:00 bis 15:00 Uhr und
            Freitag von 10:00 bis 13:00 Uhr. In der Kernzeit sind alle Mitarbeitenden
            erreichbar, sofern sie nicht Urlaub haben oder krank sind.

            ## Zeiterfassung
            Die Arbeitszeit wird im ZeitPortal erfasst, spätestens bis zum Ende der
            folgenden Woche. Das Gleitzeitkonto darf höchstens 40 Plusstunden und
            20 Minusstunden aufweisen.
            """,
            """
            ## Urlaub
            Bei einer 5-Tage-Woche haben Sie 30 Urlaubstage pro Kalenderjahr.
            Urlaub beantragen Sie im HR-Portal mindestens zwei Wochen vor Beginn.
            Resturlaub kann bis zum 31. März des Folgejahres genommen werden.

            ## Krankmeldung
            Wenn Sie krank sind, melden Sie sich am ersten Krankheitstag bis 9:00 Uhr
            telefonisch oder per E-Mail bei Ihrer Führungskraft und bei
            personal@musterfirma.example.

            Ab dem dritten Krankheitstag ist eine ärztliche Arbeitsunfähigkeitsbescheinigung
            nötig. Die Personalabteilung ruft sie elektronisch bei Ihrer Krankenkasse ab;
            bitte lassen Sie sich die Arbeitsunfähigkeit dafür in der Arztpraxis feststellen.
            """,
        ],
    },
    {
        "file": "03_it_sicherheit.pdf",
        "title": "IT & Sicherheit",
        "pages": [
            """
            ## Passwörter
            Passwörter müssen mindestens 14 Zeichen lang sein. Für alle Passwörter
            nutzen Sie den Firmen-Passwortmanager, der auf Ihrem Laptop installiert ist.

            Passwörter werden nicht regelmäßig gewechselt, sondern nur bei Verdacht auf
            Missbrauch. Geben Sie Ihr Passwort niemals weiter, auch nicht an den
            IT-Service-Desk.

            ## Mehrfaktor-Anmeldung
            Für alle Firmenkonten ist eine Mehrfaktor-Anmeldung mit der Authenticator-App
            Pflicht. Die Einrichtung erfolgt am ersten Tag bei der Übergabe des Laptops.

            Sperren Sie Ihren Bildschirm, wenn Sie den Arbeitsplatz verlassen.
            Nach 5 Minuten ohne Eingabe sperrt er sich automatisch.
            """,
            """
            ## VPN
            Außerhalb des Firmennetzes ist das VPN Pflicht. Der VPN-Client MF-Connect
            ist auf Ihrem Laptop vorinstalliert. Sie melden sich mit Ihrem Firmenkonto
            und der Authenticator-App an.

            ## Phishing melden
            Verdächtige E-Mails leiten Sie als Anhang an sicherheit@musterfirma.example
            weiter und löschen sie danach. Klicken Sie keine Links an und öffnen Sie
            keine Anhänge.

            Wenn Sie bereits auf einen Link geklickt haben, rufen Sie sofort den
            IT-Service-Desk an (interne Durchwahl 300). Ansprechpartner für IT-Sicherheit
            ist Jonas Becker.
            """,
        ],
    },
    {
        "file": "04_benefits.pdf",
        "title": "Benefits",
        "pages": [
            """
            ## Deutschlandticket
            Die Musterfirma bezuschusst das Deutschlandticket mit 30 Euro pro Monat.
            Den Zuschuss beantragen Sie einmalig im HR-Portal; er wird mit dem Gehalt
            ausgezahlt.

            ## Weiterbildung
            Jede Mitarbeiterin und jeder Mitarbeiter hat ein Weiterbildungsbudget von
            1.000 Euro pro Kalenderjahr und zusätzlich 3 Weiterbildungstage.
            Weiterbildungen beantragen Sie bei Ihrer Führungskraft mindestens vier Wochen
            vor Beginn.
            """,
            """
            ## Homeoffice
            Nach Absprache im Team können Sie bis zu 3 Tage pro Woche im Homeoffice
            arbeiten.

            Für die Einrichtung Ihres Arbeitsplatzes zu Hause erhalten Sie einmalig eine
            Ausstattungspauschale von 300 Euro. Sie beantragen sie im HR-Portal innerhalb
            der ersten sechs Monate. Laptop und Headset stellt die Musterfirma.
            """,
        ],
    },
]


def _blocks(page_text: str) -> list[tuple[str, str]]:
    """Split one page's text into ("h", heading) and ("p", paragraph) blocks."""
    blocks = []
    for chunk in page_text.strip().split("\n\n"):
        lines = [line.strip() for line in chunk.strip().splitlines()]
        if lines[0].startswith("## "):
            blocks.append(("h", lines[0][3:]))
            lines = lines[1:]
        if lines:
            blocks.append(("p", " ".join(lines)))
    return blocks


def _footer(title: str):
    """Return a callback that reportlab calls on every page to draw the footer."""

    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(2 * cm, 1.5 * cm, f"{COMPANY} · {title} · Seite {doc.page}")
        canvas.drawRightString(A4[0] - 2 * cm, 1.5 * cm, FOOTER_NOTE)
        canvas.restoreState()

    return draw


def build_pdf(document: dict, out_dir: Path) -> Path:
    styles = getSampleStyleSheet()
    path = out_dir / document["file"]
    pdf = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        title=document["title"],
        author=COMPANY,
        invariant=1,  # reproducible output: no timestamp diffs
    )

    story = [Paragraph(escape(f"{COMPANY} – {document['title']}"), styles["Title"])]
    for page_number, page_text in enumerate(document["pages"]):
        if page_number > 0:
            story.append(PageBreak())
        for kind, text in _blocks(page_text):
            style = styles["Heading2"] if kind == "h" else styles["BodyText"]
            story.append(Paragraph(escape(text), style))
            story.append(Spacer(1, 0.2 * cm))

    footer = _footer(document["title"])
    pdf.build(story, onFirstPage=footer, onLaterPages=footer)
    return path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for document in DOCUMENTS:
        print(f"wrote {build_pdf(document, OUT_DIR).relative_to(OUT_DIR.parent.parent)}")


if __name__ == "__main__":
    main()
