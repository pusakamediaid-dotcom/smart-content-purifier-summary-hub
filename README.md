# Smart Content Purifier & Summary Hub

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Gradio](https://img.shields.io/badge/Gradio-MVP%20Demo-orange)](#)
[![Hugging%20Face%20Spaces](https://img.shields.io/badge/Hugging%20Face-Live%20Space-yellow)](https://huggingface.co/spaces/pusakamediaid123/smart-content-purifier-summary-hub)
[![Status](https://img.shields.io/badge/Status-MVP%20v0.1%20Live-success)](#)

Smart Content Purifier & Summary Hub is a lightweight Gradio application that helps users clean messy text, generate short summaries, extract key points, and export the result as Markdown.

This project is built as a practical AI portfolio project with a simple rule-based MVP approach. It is designed to run on Hugging Face Spaces using free CPU resources without paid APIs, private credentials, or external API keys.

## Live Demo

Hugging Face Space:  
https://huggingface.co/spaces/pusakamediaid123/smart-content-purifier-summary-hub

GitHub Repository:  
https://github.com/pusakamediaid-dotcom/smart-content-purifier-summary-hub

## Project Status

Current version: **MVP v0.1 live**

QC status: **Layak Lanjut Bersyarat**

The current MVP is ready for continued polish, documentation improvement, and small stability refinements. The application is intentionally simple and avoids heavy model dependencies so it can stay fast, stable, and easy to deploy.

## Core Features

### 1. Clean Text

Cleans raw or messy text by normalizing spacing, removing unnecessary symbols, reducing duplicated words, and improving readability.

### 2. Short Summary

Creates a short extractive summary using lightweight rule-based sentence selection.

### 3. Key Points

Extracts important points from the text and formats them as a Markdown bullet list.

### 4. Export Markdown

Exports the generated result into a clean Markdown format that can be copied, saved, or reused in documentation and content workflows.

## Why This Project Exists

Many users paste long, repetitive, or unstructured text into AI tools. This project provides a simple first layer for preparing that text before it is reused for summaries, notes, documentation, or content drafts.

For portfolio purposes, this project demonstrates:

- Python application structure
- Gradio interface development
- Hugging Face Spaces deployment
- Lightweight text processing
- Modular project architecture
- Documentation and MVP delivery discipline

## Tech Stack

- Python
- Gradio
- Standard library text processing
- Hugging Face Spaces
- GitHub

No paid API, no private credential, and no external AI API are required for MVP v0.1.

## Project Structure

```text
smart-content-purifier-summary-hub/
- app.py
- requirements.txt
- README.md
- core/
  - __init__.py
  - cleaner.py
  - processor.py
  - exporter.py
- config/
  - __init__.py
  - modes.py
- docs/
  - USAGE.md
  - QC.md
  - ROADMAP.md
  - CASE_STUDY.md
  - PROMOTION_ASSETS.md
  - FINAL_PORTFOLIO_PACKAGE.md
  - LAUNCH_NOTES.md
  - VISUAL_ASSETS.md
  - FINAL_PROJECT_STATUS.md
  - LAUNCH_POST_FINAL.md
```

## How It Works

The application follows a simple processing flow:

1. User enters raw text.
2. User selects a mode: Clean Text, Short Summary, or Key Points.
3. The app processes the text through the core processing module.
4. The result is displayed in the Gradio UI.
5. User can export the output as Markdown.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/pusakamediaid-dotcom/smart-content-purifier-summary-hub.git
cd smart-content-purifier-summary-hub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Then open the local Gradio URL shown in the terminal.

## Documentation

Additional project documentation is available in the `docs/` folder:

- [`docs/USAGE.md`](docs/USAGE.md) — how to use the application
- [`docs/QC.md`](docs/QC.md) — MVP quality control checklist
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — planned improvement direction
- [`docs/CASE_STUDY.md`](docs/CASE_STUDY.md) — portfolio case study covering problem, solution, architecture, deployment, QC, results, and roadmap
- [`docs/PROMOTION_ASSETS.md`](docs/PROMOTION_ASSETS.md) — reusable portfolio promotion assets for recruiters, clients, communities, and social media
- [`docs/FINAL_PORTFOLIO_PACKAGE.md`](docs/FINAL_PORTFOLIO_PACKAGE.md) — final portfolio-ready package for presenting the MVP
- [`docs/LAUNCH_NOTES.md`](docs/LAUNCH_NOTES.md) — final approval and launch readiness notes for MVP v0.1
- [`docs/VISUAL_ASSETS.md`](docs/VISUAL_ASSETS.md) — screenshot and demo asset tracking for portfolio presentation
- [`docs/FINAL_PROJECT_STATUS.md`](docs/FINAL_PROJECT_STATUS.md) — final completion status and closure summary for MVP v0.1
- [`docs/LAUNCH_POST_FINAL.md`](docs/LAUNCH_POST_FINAL.md) — final LinkedIn and Threads/X launch copy

## MVP Limitations

This version is intentionally lightweight. It does not use a large language model yet. The summary and key point extraction are rule-based, which makes the app easier to deploy and cheaper to run, but the output quality may be less advanced than model-based summarization.

Planned future improvements may include better summarization logic, JSON export, example inputs, and optional model-based processing if it remains compatible with free deployment resources.

## Portfolio Note

This project is part of a staged AI portfolio build. The first milestone focuses on a working live MVP. The next milestones focus on documentation polish, UI polish, and gradual feature expansion without breaking deployment stability.
