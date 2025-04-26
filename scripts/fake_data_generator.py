from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Set number of leads to generate
num_leads = 10000

# Create CSV file
with open('datasets/leads.csv', 'w', newline='') as csvfile:
    fieldnames = ['Lead ID', 'Job Title', 'Company Name', 'Company Size', 'Email', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for lead_id in range(1, num_leads + 1):
        writer.writerow({
            'Lead ID': lead_id,
            'Job Title': fake.job(),
            'Company Name': fake.company(),
            'Company Size': fake.random_int(min=10, max=10000),
            'Email': fake.email(),
            'Location': fake.city(),
        })

print("CSV file generated successfully!")
