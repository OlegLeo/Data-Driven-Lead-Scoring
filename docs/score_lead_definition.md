# Introduction

This Lead Scoring System is designed to help prioritize business leads based on various factors that indicate their potential value. By evaluating company size, job title, location, and industry, the system assigns a score to each lead, making it easier for teams to focus on the most promising opportunities.

The system processes a list of leads, calculates their scores based on predefined criteria, and then sorts them from the highest to the lowest score. The leads are saved into a CSV file, and the highest-scoring leads are displayed in an easy-to-read table.

# The lead scoring system can be based on simple criteria like:

📈 Company Size	Important	Bigger companies = more seats/licenses = $$$

🎯 Job Title	Very Important	You want decision makers or influential tech people.

🏢 Industry	Important	Make sure it's a tech company (bonus points).

📍 Location	Medium importance	Being in a tech hub makes a lead "hotter", but you wouldn't disqualify leads from other places.

---

# Real world scenarios research:

🎯 Real-world "lead" distributions are:
Only 5%-10% of companies are huge (5000+ employees).

Only few people per company are CTO, CEO, Founder.

Many companies are in non-tech industries too.

Locations vary a lot — many companies are outside of "top hubs."

# Processing the Leads

The system begins by reading a list of leads stored in a CSV file. Each lead contains the following information:

    - Lead ID

    - Job Title

    - Company Name

    - Industry

    - Company Size

    - Email

    - Location

The data is first cleaned to ensure that any extra spaces or formatting issues are removed, making the information consistent. Once cleaned, the system processes each lead, evaluating the four factors mentioned above.

The score for each lead is then calculated based on the criteria for company size, job title, industry, and location. Once all leads have been processed and scored, they are sorted in descending order, with the highest-scoring leads appearing at the top of the list.

Output
The results are saved into a CSV file that includes the following columns:

    - Lead ID

    - Job Title

    - Company Name

    - Industry

    - Company Size

    - Email

    - Location

    - Score

In addition to the **[CSV output](docs/top_score_leads_output_example.png):**, the system identifies the top-scoring leads (those with a score of 11 or higher) and presents them in a formatted table. This table provides a quick and easy overview of the best opportunities, with key details such as lead ID, company name, job title, industry, and location, along with their score.
---

        
