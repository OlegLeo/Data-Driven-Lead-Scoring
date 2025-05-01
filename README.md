# Data-Driven-Lead-Scoring

Welcome to the Data-Driven Lead Scoring MVP repository! 🚀
This project demonstrates a simple yet powerful lead scoring solution powered by data analytics. Designed as a minimal viable product (MVP), it helps SaaS companies prioritize their leads based on actionable data insights.

## 🎯 Product Vision
To empower small and mid-sized B2B companies to quickly identify and prioritize their highest-value leads through a simple, secure, and smart data-based lead scoring platform — without needing to adopt a full CRM solution or customize complex logic.

## 💡 MVP Product Strategy
Target Audience: 
  - Early B2B tech companies, agencies, or service providers in Portugal or EU markets
  - Don’t yet have a sophisticated CRM, or underutilize their CRM
  - Are overwhelmed by tools like HubSpot or Salesforce, or don’t want to invest in them

---
## 🧠 Project Overview
This project focuses on building a lead scoring system for SaaS companies using data-driven insights. It takes a CSV file with lead data, processes it, and scores leads based on specific criteria (such as company size, job title, etc.).

---

## 🛠️ Key Features

This MVP provides a lightweight, guided experience that enables client to have access to these core features:

🔒 Login system (email + password for companies)
→ Builds trust, protects their data, feels personalized

📁 CSV Upload of leads → Fast way to bring in lead data from their CRM/export/manual efforts

🧠 Hardcoded Scoring Logic → Based on company size, job title, industry, and location
→ Defined together with the client (done by you in early stages)

📊 Top 10 leads displayed → Easy visual overview of high-priority opportunities

📥 Download scored leads (CSV) → Fully scored and sorted dataset, ready for sales action

📈 Simple Chart: Leads submitted/requested over time → Trends over last 7 days, 30 days, quarter
→ Helps show ROI and activity flow


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

  - Streamlit/Flask/Django: For building the web-based MVP interface.

---



## 📂 Repository Structure
```
data-driven-lead-scoring/
│
├── datasets/                               # Sample datasets with lead data (CSV files)
│   ├── leads.csv                           # fake generated data of 10000 entries with fale_data_generated.py
│   ├── all_leads_scored.csv                # all the data is orginized by the score lead and outputed in this file from the leads.csv
│
├── docs/                                   # Project documentation and diagrams
│   ├── score_lead_definition.md            # Documentation for lead scoring logic
│   ├── data_flow.drawio                    # TODO: Diagram showing the flow from CSV to scoring
│   ├── project_overview.md                 # Overview of the project, its goals, and features 
|   ├── top_score_leads_output_example.png  # Python script output for top the score (score >= x)
|
├── scripts/                                # Python scripts for scoring leads
│   ├── fake_data_generator.py              # Creates 10000 fake data csv file
|   ├── score_calculation.pt                # Main scoring script (CSV input and output)
│
├── web/                                    # TODO: Web interface for uploading and exporting leads (optional)
│   ├── app.py                              # TODO: Streamlit/Flask app for handling the upload & export
│
├── tests/                                  # TODO: Test scripts for validating the scoring system
│   ├── test_scoring.py                     # TODO: Unit tests for the lead scoring function
│
├── README.md                               # Project overview and instructions
├── .gitignore                              # TODO: Files and directories to be ignored by Git
└── requirements.txt                        # Dependencies and requirements for the project

```
---

## 📖 Lead Scoring Rules
The lead scoring algorithm scores each lead based on multiple attributes. Here are some example rules:


Attribute	Points Rule
... REFINING SCORING SYSTEM ... IN PROGRESS ...
