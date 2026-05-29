
# KIKO Milano AI Reputation Monitoring System

Project Overview
This repository contains a fully functional, modular **Multi-Agent AI System** designed to monitor, analyze, and quantify the digital brand reputation of **KIKO Milano**. By mining unstructured multi-platform public discourse (Trustpilot and YouTube), the system automatically processes multilingual feedback, evaluates sentiment polarity, detects specific reputational threat categories, and generates actionable analytical dashboards for strategic decision-making.

### Key Objectives
*   **Multi-Platform Data Ingestion:** Automating large-scale extraction of structured reviews from Trustpilot (via Apify) and public comments from YouTube (via YouTube Data API).
*   **Multilingual Support & Translation:** Automatically detecting European languages (Italian, French, German, Spanish, Dutch) and translating them to English for standardized processing.
*   **Contextual Threat Detection:** Identifying high-risk reputational threats including *Fraud & Scam*, *Product Quality*, *Customer Service*, and *Health & Safety* concerns.
*   **Quantitative Validation & Reporting:** Evaluating pipeline accuracy through precise empirical metrics and outputting visual trend dashboards.

## 🤖 Multi-Agent Architecture & Flow

The system runs on an agentic workflow orchestrated sequentially to manage data pipeline execution without duplication.

              ┌──────────────────────────────┐
              │      1. COLLECTOR AGENT      │ <── Ingests Trustpilot (Apify) & YouTube API
              └──────────────┬───────────────┘
                             │ ──> Generates: kiko_trustpilot_raw.xlsx & kiko_youtube_raw.csv
                             v
              ┌──────────────────────────────┐
              │        2. PARSER AGENT       │ <── Cleans text, detects language & translates
              └──────────────┬───────────────┘
                             │ ──> Generates Unified Format: kiko_final_integrated.csv
                             v
              ┌──────────────────────────────┐
              │    3. THREAT DETECTOR AGENT  │ <── Keyword mapping, sentiment filtering & rules
              └──────────────┬───────────────┘
                             │ ──> Generates: kiko_threat_report.csv
                             v
              ┌──────────────────────────────┐
              │      4. VALIDATION AGENT     │ <── Calculates precision & temporal trend lines
              └──────────────┬───────────────┘
                             │ ──> Generates: validation_metrics.txt & temporal_threat_analysis.png
                             v
              ┌──────────────────────────────┐
              │       5. REPORTER AGENT      │ <── Compiles donut charts & sentiment distribution
              └──────────────────────────────┘
                               ──> Generates Final Dashboard: kiko_reputation_report.png

# Features

- Multi-agent architecture
- YouTube Data API integration
- Trustpilot review integration
- Multilingual review translation
- Sentiment analysis pipeline
- Contextual threat detection
- Automated report generation
- Validation metrics and temporal analysis
- Visual reputation dashboards


# Project Architecture

| Agent                 | Responsibility                                         |
| --------------------- | ------------------------------------------------------ |
| Collector Agent       | Collects YouTube comments using YouTube Data API       |
| Parser Agent          | Cleans, translates, and integrates datasets            |
| Threat Detector Agent | Detects reputational threats using contextual analysis |
| Validation Agent      | Generates quantitative evaluation metrics              |
| Reporter Agent        | Creates graphical dashboards and reports               |
| Orchestrator          | Runs the complete pipeline automatically               |


# Data Sources

## Trustpilot Dataset
Structured customer reviews collected using Apify.

## YouTube Data API
Customer comments collected from YouTube videos related to KIKO Milano reviews and product experiences.

## Architecture Diagram
<img width="1171" height="1343" alt="image" src="https://github.com/user-attachments/assets/e45d0ac8-57c3-49fa-8972-83804142c61a" />

# Threat Categories

The system currently identifies the following reputational threats:

- Health & Safety Threats
- Fraud & Scam Threats
- Product Quality Threats
- Customer Service Threats
- Delivery Issues

The current implementation uses contextual rule-based threat analysis with negation handling to reduce false positives.

# Multilingual Processing

The dataset contains multilingual reviews including:

- English
- Italian
- French
- Spanish
- German
- Dutch

The system performs:

1. Automatic language detection
2. Translation to English
3. Sentiment analysis
4. Threat detection

This improves the realism and effectiveness of the reputation monitoring pipeline.

# Validation Metrics

The validation layer includes:

- Sentiment distribution statistics
- Threat frequency analysis
- Precision-oriented evaluation
- Temporal trend analysis using review dates
- Comparative platform analysis

Generated visualizations help identify reputation risks across platforms.

# Installation

Install all dependencies:

```bash
pip install -r Requirements.txt
```

# Running the Project

Run the complete automated pipeline:

```bash
python Orchestrator.py
```

The orchestrator automatically executes:

1. Parser Agent
2. Threat Detector Agent
3. Validation Agent
4. Reporter Agent

# Generated Outputs

## Processed Data

Generated files:

```text
data/processed/kiko_final_integrated.csv
data/processed/kiko_threat_report.csv
```

## Visual Reports

Generated report:

```text
reports/kiko_reputation_report.png
```

# Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* TextBlob
* Deep Translator
* LangDetect
* YouTube Data API

