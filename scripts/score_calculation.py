import csv
from tabulate import tabulate

def clean_text(text):
    return ' '.join(text.strip().split())

def calculate_lead_score_with_reasons(company_size, job_title, location):
    score = 0
    reasons = []

    if company_size >= 5000:
        score += 5
        reasons.append("Large Company Size (5000+ employees)")
    elif 500 < company_size <= 5000:
        score += 4

    decision_makers = ["CTO", "CEO", "Founder"]
    if any(title in job_title for title in decision_makers):
        score += 5
        reasons.append("Decision Maker Title (CTO/CEO/Founder)")
    elif "Manager" in job_title or "Director" in job_title:
        score += 3
        reasons.append("Manager/Director Title")
    elif "Engineer" in job_title or "Specialist" in job_title:
        score += 2
        reasons.append("Engineer/Specialist Title")

    high_priority_locations = ["New York", "San Francisco"]
    if location in high_priority_locations:
        score += 4
        reasons.append(f"Priority Location ({location})")

    return score, reasons

# Counters
total_leads_processed = 0
top_matches = []

# Read CSV
with open('datasets/leads.csv', 'r') as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    rows = list(reader)

    for row in rows:
        total_leads_processed += 1

        lead_id = int(clean_text(row['Lead ID']))
        company_size = int(clean_text(row['Company Size']))
        job_title = clean_text(row['Job Title'])
        location = clean_text(row['Location'])

        score, reasons = calculate_lead_score_with_reasons(company_size, job_title, location)

        if score >= 10:
            top_matches.append([
                lead_id,
                company_size,
                job_title,
                location,
                score,
                ", ".join(reasons)
            ])


# Final table output
if top_matches:
    # Sort by Score descending
    top_matches = sorted(top_matches, key=lambda x: x[4], reverse=True)

    # Add numbering
    top_matches_numbered = []
    for idx, match in enumerate(top_matches, 1):
        top_matches_numbered.append([idx] + match)

    print("\n🏆 Top Matching Leads (Score >= 10):\n")
    print(tabulate(
        top_matches_numbered,
        headers=["#", "Lead ID", "Company Size", "Job Title", "Location", "Score", "Reasons"],
        tablefmt="fancy_grid"
    ))
else:
    print("No top matches found.")

print(f"\nFinished. {total_leads_processed} leads processed, {len(top_matches)} top matches found (score >= 10).")