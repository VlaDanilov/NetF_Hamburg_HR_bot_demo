from google.adk.agents import LlmAgent

# Exact model ID, no "-latest" alias: behaviour must not change silently.
MODEL = "gemini-3.8-flash"

root_agent = LlmAgent(
    name="onboarding_assistent",
    model=MODEL,
    description="Beantwortet Onboarding-Fragen neuer Mitarbeitender der Musterfirma GmbH.",
    instruction="Du bist ein hilfreicher Assistent. Antworte auf Deutsch.",
)
