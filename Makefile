.PHONY: setup data run test eval

setup:
	uv sync

data:
	uv run python scripts/make_sample_pdfs.py

# Dev UI on http://127.0.0.1:8000. Sessions stay in memory (default would write to hr_agent/.adk/).
run:
	uv run adk web \
		--session_service_uri memory:// \
		--artifact_service_uri memory:// \
		hr_agent

# Lint + unit tests, no API key needed.
test:
	uv run ruff check .
	uv run ruff format --check .
	uv run pytest

# Real model calls: 1 request per case. Optional: make eval CASES="urlaubstage"
eval:
	uv run python -m tests.eval.run_eval $(CASES)
