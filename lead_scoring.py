import csv
from io import StringIO

def clean_text(text):
    """Clean and normalize text by removing extra spaces."""
    return ' '.join(text.strip().split())

def calculate_lead_score(company_size, job_title, location, industry):
    """Calculate lead score based on company size, job title, location, and industry."""
    score = 0

    # Normalize text
    job_title = job_title.lower()
    location = location.lower()
    industry = industry.lower()

    # Company Size
    if company_size >= 10000:
        score += 10
    elif 5000 <= company_size < 10000:
        score += 5
    elif 2000 <= company_size < 5000:
        score += 4
    elif 1000 <= company_size < 2000:
        score += 3
    elif 500 <= company_size < 1000:
        score += 2
    elif 100 <= company_size < 500:
        score += 1

    # Job Title
    if any(title in job_title for title in ["cto", "ceo", "founder"]):
        score += 6
    elif any(title in job_title for title in ["vp", "vice president", "director", "head"]):
        score += 4
    elif any(title in job_title for title in ["engineer", "developer", "scientist", "architect", "manager", "owner", "scrum master"]):
        score += 1

    # Industry
    if industry in [
        "saas", "fintech", "healthtech", "ai", "cybersecurity", "cloud services",
        "edtech", "blockchain", "devtools", "e-commerce tech", "iot solutions", "analytics platform"
    ]:
        score += 2
    else:
        score += 1

    # Location
    high_priority_locations = [
        "san francisco", "new york", "seattle", "austin", "boston", "berlin",
        "london", "toronto", "amsterdam", "tel aviv", "lisbon", "chicago", "paris", "los angeles"
    ]
    medium_priority_locations = ["miami", "dallas", "vancouver", "madrid", "munich"]

    if location in high_priority_locations:
        score += 2
    elif location in medium_priority_locations:
        score += 1

    return score

def process_leads(file_stream):
    """Process uploaded CSV file and return processed leads."""
    all_leads = []

    # Read the CSV from the uploaded file
    decoded = file_stream.read().decode('utf-8')
    csv_reader = csv.DictReader(StringIO(decoded), skipinitialspace=True)

    for row in csv_reader:
        lead_id = int(clean_text(row['Lead ID']))
        job_title = clean_text(row['Job Title'])
        company_name = clean_text(row['Company Name'])
        industry = clean_text(row['Industry'])
        company_size = int(clean_text(row['Company Size']))
        email = clean_text(row['Email'])
        location = clean_text(row['Location'])

        score = calculate_lead_score(company_size, job_title, location, industry)

        all_leads.append([
            lead_id, job_title, company_name, industry, company_size, email, location, score
        ])

    # Sort by Score (highest first)
    all_leads.sort(key=lambda x: x[7], reverse=True)

    return all_leads
