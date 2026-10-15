.PHONY: setup data

setup:
	uv sync

data:
	uv run python scripts/make_sample_pdfs.py
