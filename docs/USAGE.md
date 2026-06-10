# Usage Guide

This document explains how to use **Smart Content Purifier & Summary Hub** MVP v0.1.

Live Space:  
https://huggingface.co/spaces/pusakamediaid123/smart-content-purifier-summary-hub

## Basic Workflow

1. Open the Hugging Face Space.
2. Paste your raw text into the input box.
3. Choose one processing mode.
4. Click **Proses Teks**.
5. Review the generated output.
6. Click **Export Markdown** if you want a Markdown-formatted result.

## Available Modes

### Clean Text

Use this mode when your input text is messy, repetitive, or difficult to read.

Best for:

- Cleaning copied article text
- Removing unnecessary spacing
- Improving text readability
- Preparing text before summarization

### Short Summary

Use this mode when you want a shorter version of a longer text.

Best for:

- Article summaries
- Study notes
- Content review
- Quick reading preparation

### Key Points

Use this mode when you want the most important ideas in bullet-point format.

Best for:

- Meeting notes
- Learning materials
- Content planning
- Research preparation

### Export Markdown

Use this button after generating an output. The app will format the result with:

- Title
- Selected mode
- Processing date
- Generated result

## Recommended Input

For best results, use clear text with at least one paragraph. The app can process messy text, but the result will be better if the original text has enough context.

Recommended input length:

- Minimum: one short paragraph
- Best: 2–8 paragraphs
- Avoid: extremely long documents in MVP v0.1

## Notes

MVP v0.1 uses lightweight rule-based processing. It does not call an external AI API and does not require paid credits. This keeps the application simple, stable, and suitable for free Hugging Face Spaces deployment.
