"""Load the onboarding PDFs as text, one block per page with a citation marker."""

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "onboarding"


@dataclass(frozen=True)
class Page:
    document: str  # citation name, e.g. "Erster Arbeitstag"
    number: int  # 1-based
    text: str


def load_pages(folder: Path = DATA_DIR) -> list[Page]:
    """Read all PDFs in `folder`. Fails loudly on an empty folder or a page without text."""
    pdf_paths = sorted(folder.glob("*.pdf"))  # sorted: same order on every start
    if not pdf_paths:
        raise FileNotFoundError(f"Keine PDFs in {folder} gefunden. Erst `make data` ausführen.")

    pages = []
    for path in pdf_paths:
        reader = PdfReader(path)
        title = (reader.metadata.title if reader.metadata else None) or path.stem
        for number, pdf_page in enumerate(reader.pages, start=1):
            text = pdf_page.extract_text().strip()
            if not text:
                raise ValueError(
                    f"{path.name}, Seite {number}: kein Text gefunden (gescanntes PDF? OCR nötig)."
                )
            pages.append(Page(document=title, number=number, text=text))
    return pages


def format_pages(pages: list[Page]) -> str:
    """Join pages into one text, each starting with "[Dokument, Seite N]"."""
    return "\n\n".join(f"[{page.document}, Seite {page.number}]\n{page.text}" for page in pages)
