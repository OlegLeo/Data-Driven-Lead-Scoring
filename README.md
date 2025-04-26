# Data-Driven-Lead-Scoring

Welcome to the Data-Driven Lead Scoring MVP repository! 🚀
This project demonstrates a simple yet powerful lead scoring solution powered by data analytics. Designed as a minimal viable product (MVP), it helps SaaS companies prioritize their leads based on actionable data insights.

---
## 🧠 Project Overview
This project focuses on building a lead scoring system for SaaS companies using data-driven insights. It takes a CSV file with lead data, processes it, and scores leads based on specific criteria (such as company size, job title, etc.).

---

## 🛠️ Key Features
CSV Upload: Users can upload CSV files with lead data.

Lead Scoring: Scores leads based on predefined rules (e.g., job title, company size).

Simple Export: Download the results as a CSV with scores.

---

## 🚀 Data Flow & Lead Scoring Example
Here’s how the data flow looks for scoring the leads:

  - **CSV Input:** Upload a CSV with basic lead information (e.g., job title, company size, location).

  - **Scoring Algorithm:** The system applies predefined scoring rules to each lead based on their attributes.

  - **Export Scored Leads:** A downloadable CSV with the scores is provided, which can be used by sales teams to prioritize outreach.
---

## 🧑‍💻 Tech Stack
  - Python: For data processing and scoring algorithm.

  - Pandas: For working with CSV files and data manipulation.

  - Streamlit/Flask/Django (Optional): For building the web-based MVP interface.

---



## 📂 Repository Structure
```
data-driven-lead-scoring/
│
├── datasets/                           # Sample datasets with lead data (CSV files)
│
├── docs/                               # Project documentation and diagrams
│   ├── score_lead_definition.md        # Documentation for lead scoring logic
│   ├── data_flow.drawio                # TODO: Diagram showing the flow from CSV to scoring
│   ├── project_overview.md             # Overview of the project, its goals, and features
│
├── scripts/                            # Python scripts for scoring leads
│   ├── fake_data_generator.py          # Creates 10000 fake data csv file
|   ├── score_calculation.pt            # Main scoring script (CSV input and output)
│
├── web/                                # TODO: Web interface for uploading and exporting leads (optional)
│   ├── app.py                          # TODO: Streamlit/Flask app for handling the upload & export
│
├── tests/                              # TODO: Test scripts for validating the scoring system
│   ├── test_scoring.py                 # TODO: Unit tests for the lead scoring function
│
├── README.md                           # Project overview and instructions
├── .gitignore                          # TODO: Files and directories to be ignored by Git
└── requirements.txt                    # Dependencies and requirements for the project

```
---

## 📖 Lead Scoring Rules
The lead scoring algorithm scores each lead based on multiple attributes. Here are some example rules:


Attribute	Points Rule
... REFINING SCORING SYSTEM ... IN PROGRESS ...
