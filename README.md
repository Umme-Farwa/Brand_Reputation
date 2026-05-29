
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
| Collector Agent       | Connects to Apify and YouTube Data API to harvest raw feedback while preserving critical metadata (timestamps, rating scores).   |
| Parser Agent          | Uses `LangDetect` and `Deep Translator` to normalize text, remove duplicate entries, and assign base sentiment ratings using `TextBlob`.|
| Threat Detector Agent | Evaluates contextual rule-based risks (e.g., mapping expressions regarding skin irritation to *Health & Safety* or delivery issues to *Customer Service*).|
| Validation Agent      | Tracks statistical validity, performing precision-oriented evaluations on flagged anomalies over time. |
| Reporter Agent        |  Generates data-driven charts converting raw textual telemetry into visual executive assets. |
| Orchestrator          | Runs the complete pipeline automatically               |


---

## Empirical Evaluation & Outputs

The system delivers a highly reliable baseline for threat classification, verified through manual auditing metrics.

### Statistical Performance Summary
*   **Total Reviews Analyzed:** 658  
*   **Total Threats Flagged:** 69  
*   **True Positives (Verified Risks):** 60  
*   **System Precision Score:** **86.96%**  

### Visual Analytics Dashboards
Upon system execution, the following charts are generated inside the `reports/` folder:

1.  **KIKO Brand Reputation Dashboard (`reports/kiko_reputation_report.png`)**  
    Contains threat distribution donut charts, platform comparison breakdowns, and overall average sentiment rating distributions.
2.  **Temporal Threat Trends Line Graph (`reports/temporal_threat_analysis.png`)**  
    Tracks fluctuations and spikes in review volumes and flagged risks over specific chronological intervals.

---

## ⚙️ Quick Start Guide (Execution Steps for Evaluation)

Follow these precise instructions to provision the environment, resolve system dependencies, and execute the multi-agent orchestration layer.

### Prerequisites
*   Python 3.8 or higher installed globally.
*   Internet access for real-time translation and dependency fetching.

### Step 1: Clone the Repository
Open a terminal workspace or command prompt window and run:
```bash
git clone [https://github.com/Umme-Farwa/Brand_Reputation.git](https://github.com/Umme-Farwa/Brand_Reputation.git)
cd Brand_Reputation

### **Step 2:Initialize Virtual Environment**
Initialize an isolated environment sandbox to manage dependencies cleanly:

Bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS / Linux
python3 -m venv env
source env/bin/activate

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

