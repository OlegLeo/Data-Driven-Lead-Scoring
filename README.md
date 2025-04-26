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
│   ├── lead_scoring_rules.md           # Documentation for lead scoring logic
│   ├── data_flow.drawio                # Diagram showing the flow from CSV to scoring
│   ├── project_overview.md             # Overview of the project, its goals, and features
│
├── scoring/                            # Python scripts for scoring leads
│   ├── score_leads.py                  # Main scoring script (CSV input and output)
│
├── web/                                # Web interface for uploading and exporting leads (optional)
│   ├── app.py                          # Streamlit/Flask app for handling the upload & export
│
├── tests/                              # Test scripts for validating the scoring system
│   ├── test_scoring.py                 # Unit tests for the lead scoring function
│
├── README.md                           # Project overview and instructions
├── .gitignore                          # Files and directories to be ignored by Git
└── requirements.txt                    # Dependencies and requirements for the project

```
---

## 📖 Lead Scoring Rules
The lead scoring algorithm scores each lead based on multiple attributes. Here are some example rules:


Attribute	Points Rule
Company Size	+20 points for companies with >50 employees
Job Title	+30 points for "Head of Marketing" or "CTO"
Email Domain	+10 points for non-Gmail email domains
Industry	+15 points for industries like Tech or Education
Location	+10 points for leads based in the US or EU
