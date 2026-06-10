# AI Summary Upgrade Plan

Project:
Smart Content Purifier & Summary Hub

Target Version:
MVP v0.2 — Optional AI Summarization

Current Status:
MVP v0.1.1 Hardened

## 1. Goal

The goal of this upgrade is to plan a smarter AI summarization layer for MVP v0.2 while keeping the existing MVP v0.1.1 stable, lightweight, and safe for public deployment.

This upgrade must preserve:

- Rule-based fallback
- Free/low-cost deployment
- No mandatory API key
- No credential in the public repository
- Hugging Face Spaces stability

This document is a planning document only. It does not implement an AI model, add dependencies, or change the live application behavior.

## 2. Current Architecture

The current application architecture is intentionally simple and lightweight:

- `app.py` works as the Gradio UI and main application entry point.
- `core/processor.py` works as the rule-based processor for supported text modes.
- `core/cleaner.py` works as the text cleaner.
- `core/exporter.py` works as the Markdown exporter.
- `config/modes.py` stores the available mode list and mode metadata.

Current main modes:

- Clean Text
- Short Summary
- Key Points
- Export Markdown

The current processor remains rule-based by design so the app can stay stable on Hugging Face Spaces Free CPU without heavy model dependencies.

## 3. Upgrade Options

| Option | Description | Pros | Cons | Cost | Risk | Recommendation |
|---|---|---|---|---|---|---|
| A. Rule-Based Only | Keep the current rule-based summarization behavior. | Very stable, lightweight, no API required, easy to maintain. | Summary quality is limited because it does not use a real AI model. | Free | Low | Keep as the default fallback. |
| B. Hugging Face Open-Source Local Model | Use an open-source summarization model from Hugging Face. | Can be free, useful for a real AI portfolio, no user API key required. | Heavier dependencies, longer build time, slower CPU inference, possible memory issues. | Free if it runs on available hardware | Medium to High | Explore with a small model only after planning is approved. |
| C. OpenAI BYOK | User provides their own OpenAI API key at runtime. | Smarter output, no API cost paid by the app owner, flexible model quality. | Requires API key input UI, security handling, disclaimer, and strict no-logging rules. | Paid by user API usage | Medium | Add only as an advanced optional engine, not as default. |
| D. Gemini BYOK | User provides their own Gemini API key at runtime. | Smarter output, no API cost paid by the app owner, useful alternative to OpenAI. | Requires API key input UI, security handling, disclaimer, and strict no-logging rules. | Paid by user API usage | Medium | Add only as an advanced optional engine, not as default. |
| E. Hybrid Architecture | Default rule-based engine with optional AI engine and automatic fallback to rule-based if AI fails. | Preserves current stability while enabling smarter summaries as an option. | Requires careful architecture, testing, and UI clarity. | Free by default, optional user-paid API if BYOK is enabled | Medium | Recommended main direction. |

## 4. Recommended Direction

Recommended direction:
Hybrid Architecture.

Suggested implementation order:

1. Keep rule-based processing as the default.
2. Add `core/ai_summarizer.py` as a separate AI summarization interface.
3. Add an AI engine selector.
4. Start with a small Hugging Face open-source model exploration.
5. Add BYOK OpenAI/Gemini only as an advanced optional path.
6. Do not make any paid API the default engine.

This approach protects MVP v0.1.1 while giving MVP v0.2 a clear path toward smarter summarization.

## 5. Proposed v0.2 Architecture

Planned structure:

```text
smart-content-purifier-summary-hub/
- app.py
- requirements.txt
- core/
  - cleaner.py
  - processor.py
  - ai_summarizer.py
  - exporter.py
- config/
  - modes.py
  - ai_settings.py
- docs/
  - AI_UPGRADE_PLAN.md
- tests/
  - test_ai_summarizer.py
```

Note:
This structure is a plan only. Do not create these planned files during TQ-029 except `docs/AI_UPGRADE_PLAN.md`.

## 6. Proposed UI Change

Planned UI change for MVP v0.2:

Add an optional selector:

AI Engine:

- Rule-Based
- Hugging Face Local
- OpenAI BYOK
- Gemini BYOK

Add optional fields:

- API key input for OpenAI/Gemini
- API key input must be password/masked
- API key must not be stored
- API key must not be logged
- API key must not appear in Markdown export
- API key must not be committed to GitHub

The default AI Engine should remain Rule-Based until the optional AI path is approved, implemented, and tested.

## 7. Security Rules

Required security rules:

- Do not commit API keys.
- Do not store API keys in the repository.
- Do not store API keys in files.
- Do not log API keys.
- Do not hardcode credentials.
- Use BYOK only as runtime input.
- Add a disclaimer that users are responsible for their own API keys and API usage costs.

Additional security notes:

- API keys must never be included in exported Markdown.
- API keys must never be included in screenshots, logs, examples, tests, or documentation.
- Public repository files must remain credential-free.

## 8. Dependency Impact

Current dependencies:

- gradio
- markdown
- pytest

If Hugging Face local model is added later:

- transformers
- torch
- sentencepiece if required by the selected model
- Risk: heavier build, slower installation, slower CPU inference, and possible memory issues on free deployment hardware

If OpenAI BYOK is added later:

- openai package
- API key required at runtime

If Gemini BYOK is added later:

- google-genai or the relevant official Google package
- API key required at runtime

Note:
Do not add these dependencies in TQ-029. New dependencies may only be added in a later implementation task after this planning document is approved.

## 9. Testing Plan

Planned tests for MVP v0.2:

- Test rule-based fallback still works.
- Test AI summary returns a non-empty string.
- Test AI failure automatically falls back to rule-based summary.
- Test empty input.
- Test short input.
- Test long input.
- Test empty API key.
- Test OpenAI/Gemini are not called when the API key is empty.
- Test no API key appears in output.

## 10. Rollback Plan

If the AI model fails:

- Turn off the AI engine.
- Return to rule-based processing.
- Do not remove MVP v0.1.1 features.
- Do not change core cleaner/exporter behavior unnecessarily.
- Restore requirements if added dependencies become too heavy.

Rollback must prioritize keeping the public demo stable and usable.

## 11. Recommended Next Tasks

Recommended next tasks:

- TQ-030 — Implement AI Summarizer Interface
- TQ-031 — Add Hugging Face Local Summarizer
- TQ-032 — Add AI Engine Selector in UI
- TQ-033 — Add BYOK OpenAI/Gemini Planning
- TQ-034 — AI Summary QC and Benchmark
- TQ-035 — Release MVP v0.2

## 12. Final Decision

AI upgrade is worth continuing, but it must be done gradually.

Final decision:

- Rule-based remains the default.
- AI summarization must be optional.
- No mandatory API key.
- No mandatory cost.
- No credential in the public repository.
- Hybrid Architecture is recommended for MVP v0.2 planning.

Implementation status:
Planning only. AI summarization is not live yet.
