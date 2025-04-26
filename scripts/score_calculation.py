import csv
from tabulate import tabulate

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
        score += 10  # Very large companies
    elif 5000 <= company_size < 10000:
        score += 5  # Large companies
    elif 2000 <= company_size < 5000:
        score += 4  # Upper mid-sized companies
    elif 1000 <= company_size < 2000:
        score += 3  # Mid-sized companies
    elif 500 <= company_size < 1000:
        score += 2  # Small mid-sized companies
    elif 100 <= company_size < 500:
        score += 1  # Small companies

    # Job Title
    if any(title in job_title for title in ["cto", "ceo", "founder"]):
        score += 6
    elif any(title in job_title for title in ["vp", "vice president", "director", "head"]):
        score += 4
    elif any(title in job_title for title in ["engineer", "developer", "scientist", "architect", "manager", "owner", "scrum master"]):
        score += 1
    else:
        score += 0

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
    else:
        score += 0

    return score

def save_all_leads_to_csv(all_leads, output_path="datasets/all_leads_scored.csv"):
    """Save all leads (sorted by score) to a CSV file."""
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Lead ID", "Job Title", "Company Name", "Industry", "Company Size", "Email", "Location", "Score"])
        for lead in all_leads:
            writer.writerow(lead)
    print(f"✅ All leads saved to '{output_path}'\n")

# --- Main Process ---

# Counters
total_leads_processed = 0
all_leads = []

# Read the CSV
with open('datasets/leads.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    rows = list(reader)

    for row in rows:
        total_leads_processed += 1

        lead_id = int(clean_text(row['Lead ID']))
        job_title = clean_text(row['Job Title'])
        company_name = clean_text(row['Company Name'])
        industry = clean_text(row['Industry'])
        company_size = int(clean_text(row['Company Size']))
        email = clean_text(row['Email'])
        location = clean_text(row['Location'])

        score = calculate_lead_score(company_size, job_title, location, industry)

        all_leads.append([
            lead_id,
            job_title,
            company_name,
            industry,
            company_size,
            email,
            location,
            score
        ])

# Sort all leads by Score descending
all_leads = sorted(all_leads, key=lambda x: x[7], reverse=True)  # Fix: should be `x[7]` as the score is at index 7

# Save all leads to CSV
save_all_leads_to_csv(all_leads)

# Display only top matches (score >= 15)
top_matches = [lead for lead in all_leads if lead[7] >= 11]

if top_matches:
    top_matches_numbered = []
    for idx, match in enumerate(top_matches, 1):
        top_matches_numbered.append([idx] + match)

    print("\n🏆 Top Matching Leads (Score >= 15):\n")
    print(tabulate(
        top_matches_numbered,
        headers=["#", "Lead ID", "Job Title", "Company Name", "Industry", "Company Size", "Email", "Location", "Score"],
        tablefmt="fancy_grid"
    ))
else:
    print("No top matches found.")

print(f"\nFinished. {total_leads_processed} leads processed, {len(top_matches)} top matches found (score >= 15).")
