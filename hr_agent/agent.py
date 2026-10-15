import os

from google.adk.agents import LlmAgent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.models import Gemini
from google.genai import types

from .context import format_pages, load_pages
from .prompts import build_instruction

# Exact model ID, no "-latest" alias: behaviour must not change silently.
# GEMINI_MODEL in .env overrides it, e.g. when the default model is overloaded.
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

# Built once at startup; a changed PDF needs a restart.
INSTRUCTION = build_instruction(format_pages(load_pages()))


def provide_instruction(ctx: ReadonlyContext) -> str:
    # A function, not a string: ADK treats "{name}" in string instructions as
    # session-state placeholders and fails on unknown names. PDF text may contain braces.
    return INSTRUCTION


# Without retry_options ADK makes a single attempt. Retry only temporary errors
# (timeouts, 5xx); a 429 quota error won't recover within seconds.
RETRY = types.HttpRetryOptions(attempts=3, http_status_codes=[408, 500, 502, 503, 504])

root_agent = LlmAgent(
    name="onboarding_assistent",
    model=Gemini(model=MODEL, retry_options=RETRY),
    description="Beantwortet Onboarding-Fragen neuer Mitarbeitender der Musterfirma GmbH.",
    instruction=provide_instruction,
)
