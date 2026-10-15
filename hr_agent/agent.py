from google.adk.agents import LlmAgent
from google.adk.agents.readonly_context import ReadonlyContext

from .context import format_pages, load_pages
from .prompts import build_instruction

# Exact model ID, no "-latest" alias: behaviour must not change silently.
MODEL = "gemini-3.8-flash"

# Built once at startup; a changed PDF needs a restart.
INSTRUCTION = build_instruction(format_pages(load_pages()))


def provide_instruction(ctx: ReadonlyContext) -> str:
    # A function, not a string: ADK treats "{name}" in string instructions as
    # session-state placeholders and fails on unknown names. PDF text may contain braces.
    return INSTRUCTION


root_agent = LlmAgent(
    name="onboarding_assistent",
    model=MODEL,
    description="Beantwortet Onboarding-Fragen neuer Mitarbeitender der Musterfirma GmbH.",
    instruction=provide_instruction,
)
