````md
# KIKO Milano AI Reputation Monitoring System

## Project Overview

This project is an AI-driven reputation monitoring prototype designed to analyze customer reviews and detect reputational threats for KIKO Milano.

The system integrates data from multiple online platforms including:

- Trustpilot Reviews
- YouTube Comments (via YouTube Data API)

The architecture follows a modular multi-agent design where different agents handle specific responsibilities such as data collection, parsing, multilingual processing, threat detection, validation, and reporting.

The project aims to support automated reputation analysis through sentiment evaluation, contextual threat categorization, and visual reporting dashboards.


---

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


---

# Project Architecture

| Agent                 | Responsibility                                         |
| --------------------- | ------------------------------------------------------ |
| Collector Agent       | Collects YouTube comments using YouTube Data API       |
| Parser Agent          | Cleans, translates, and integrates datasets            |
| Threat Detector Agent | Detects reputational threats using contextual analysis |
| Validation Agent      | Generates quantitative evaluation metrics              |
| Reporter Agent        | Creates graphical dashboards and reports               |
| Orchestrator          | Runs the complete pipeline automatically               |

---

# Data Sources

## Trustpilot Dataset
Structured customer reviews collected using Apify.

## YouTube Data API
Customer comments collected from YouTube videos related to KIKO Milano reviews and product experiences.


---

# Threat Categories

The system currently identifies the following reputational threats:

- Health & Safety Threats
- Fraud & Scam Threats
- Product Quality Threats
- Customer Service Threats
- Delivery Issues

The current implementation uses contextual rule-based threat analysis with negation handling to reduce false positives.


---

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


---

# Validation Metrics

The validation layer includes:

- Sentiment distribution statistics
- Threat frequency analysis
- Precision-oriented evaluation
- Temporal trend analysis using review dates
- Comparative platform analysis

Generated visualizations help identify reputation risks across platforms.


---

# Repository Structure

```text
KIKO_REPUTATION_PROJECT/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── Src/
│   └── kiko agents/
│
├── Requirements.txt
├── README.md
└── .gitignore
````

---

# Installation

Install all dependencies:

```bash
pip install -r Requirements.txt
```

---

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

---

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

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* TextBlob
* Deep Translator
* LangDetect
* YouTube Data API

---

# Current Limitations

The current system is a lightweight research prototype and still has some limitations:

* Rule-based threat detection instead of deep contextual NLP
* Limited semantic understanding
* No real-time streaming analysis
* Basic sentiment modeling

---

# Future Improvements

Possible future enhancements include:

* Transformer-based NLP models
* Real-time reputation monitoring
* Dashboard web application
* Advanced multilingual language models
* Machine learning threat classification
* Context-aware semantic analysis

---

