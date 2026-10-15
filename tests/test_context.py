"""Deterministic tests for PDF loading and instruction assembly (no API key needed)."""

import asyncio
import re

import pytest
from pypdf import PdfWriter

from hr_agent.context import format_pages, load_pages
from hr_agent.prompts import REFUSAL, build_instruction

EXPECTED_DOCUMENTS = ["Erster Arbeitstag", "Arbeitszeit & Urlaub", "IT & Sicherheit", "Benefits"]


@pytest.fixture(scope="module")
def pages():
    return load_pages()


def test_loads_all_documents_with_two_pages_each(pages):
    assert [p.document for p in pages[::2]] == EXPECTED_DOCUMENTS
    assert len(pages) == 2 * len(EXPECTED_DOCUMENTS)


def test_page_numbers_start_at_one_per_document(pages):
    for document in EXPECTED_DOCUMENTS:
        assert [p.number for p in pages if p.document == document] == [1, 2]


@pytest.mark.parametrize(
    ("document", "number", "fact"),
    [
        ("Erster Arbeitstag", 2, "Lena Hoffmann"),
        ("Arbeitszeit & Urlaub", 2, "30 Urlaubstage"),
        ("IT & Sicherheit", 1, "mindestens 14 Zeichen"),
        ("Benefits", 1, "30 Euro pro Monat"),
    ],
)
def test_known_fact_is_on_expected_page(pages, document, number, fact):
    page = next(p for p in pages if p.document == document and p.number == number)
    assert fact in page.text


def test_loading_is_stable(pages):
    assert load_pages() == pages


def test_every_page_block_starts_with_a_marker(pages):
    markers = re.findall(r"^\[(.+), Seite (\d+)\]$", format_pages(pages), flags=re.MULTILINE)
    assert markers == [(p.document, str(p.number)) for p in pages]


def test_empty_folder_fails_loudly(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_pages(tmp_path)


def test_page_without_text_fails_loudly(tmp_path):
    writer = PdfWriter()
    writer.add_blank_page(width=595, height=842)  # like a scanned page: no text layer
    writer.write(tmp_path / "scan.pdf")
    with pytest.raises(ValueError, match="kein Text"):
        load_pages(tmp_path)


def test_instruction_has_rules_before_fenced_documents(pages):
    instruction = build_instruction(format_pages(pages))
    assert REFUSAL in instruction
    assert instruction.index("Regeln:") < instruction.index("<dokumente>")
    assert instruction.rstrip().endswith("</dokumente>")
    for p in pages:
        assert f"[{p.document}, Seite {p.number}]" in instruction


def test_curly_braces_in_documents_reach_the_model_unchanged():
    # A string instruction would be templated by ADK ("{name}" -> KeyError);
    # bypass=True confirms the function path skips that.
    from hr_agent.agent import INSTRUCTION, root_agent

    assert "{name}" in build_instruction("Text mit {name} in Klammern")
    instruction, bypass = asyncio.run(root_agent.canonical_instruction(None))
    assert bypass is True
    assert instruction == INSTRUCTION
