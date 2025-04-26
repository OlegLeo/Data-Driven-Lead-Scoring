from faker import Faker
import csv
import random

# Initialize Faker
fake = Faker()

# Set number of leads to generate
num_leads = 10000

# Lists for custom generation
top_job_titles = ["CEO", "CTO", "Founder"]
mid_job_titles = ["VP of Engineering", "Director of Engineering", "Engineering Manager", "Product Manager", "Tech Lead", "Product Owner"]
low_job_titles = ["Software Engineer", "Data Analyst", "IT Specialist", "Developer", "QA Tester", "Support Engineer", "Scrum Master"]

tech_industries = ["SaaS", "Fintech", "Healthtech", "AI", "Cybersecurity", "Cloud Services", "DevTools", "Analytics Platform"]
non_tech_industries = ["Retail", "Construction", "Hospitality", "Transportation", "Manufacturing", "Education", "Healthcare"]

high_priority_cities = ["San Francisco", "New York", "Seattle", "Austin", "Boston", "Berlin", "London", "Toronto", "Amsterdam", "Tel Aviv", "Lisbon", "Chicago", "Paris", "Los Angeles"]
normal_cities = [fake.city() for _ in range(100)]

# Create CSV file
with open('datasets/leads.csv', 'w', newline='') as csvfile:
    fieldnames = ['Lead ID', 'Job Title', 'Company Name', 'Industry', 'Company Size', 'Email', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for lead_id in range(1, num_leads + 1):
        
        # Assign company size with probability
        size_bucket = random.choices(
            ['small', 'medium', 'large'],
            weights = [0.99, 0.01, 0.001], # 98% small, 1% mid, 0.1% large
            k=1
        )[0]

        if size_bucket == 'small':
            company_size = random.randint(10, 500)
        elif size_bucket == 'medium':
            company_size = random.randint(501, 5000)
        else:
            company_size = random.randint(5001, 20000)

        # Assign job title with probability
        title_bucket = random.choices(
            ['top', 'mid', 'low'],
            weights=[0.001, 0.2, 0.989],  # 0.01% C-level, 2% managers, 98.9% technical
            k=1
        )[0]

        if title_bucket == 'top':
            job_title = random.choice(top_job_titles)
        elif title_bucket == 'mid':
            job_title = random.choice(mid_job_titles)
        else:
            job_title = random.choice(low_job_titles)

        # Assign industry
        industry = random.choice(tech_industries + non_tech_industries)

        # Assign location with probability
        location_bucket = random.choices(
            ['high', 'normal'],
            weights=[0.1, 0.9],  # 90% tech hubs, 10% random cities
            k=1
        )[0]

        if location_bucket == 'high':
            location = random.choice(high_priority_cities)
        else:
            location = random.choice(normal_cities)

        writer.writerow({
            'Lead ID': lead_id,
            'Job Title': job_title,
            'Company Name': fake.company(),
            'Industry': industry,
            'Company Size': company_size,
            'Email': fake.email(),
            'Location': location
        })

print("CSV leads generetaed successfully!")
