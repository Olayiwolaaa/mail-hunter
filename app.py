import re
import requests
import csv
from bs4 import BeautifulSoup
import keywords_arr  # Make sure this module contains your URLs

# Function to scrape emails from a given URL
def scrape_emails(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Regular expression to find emails
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, soup.text)

        return emails

    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

# List to hold all found emails
all_emails = []

# Scraping emails from each URL
for url in keywords_arr.urls:
    emails = scrape_emails(url)
    all_emails.extend(emails)  # Add found emails to the list

# Save emails to a CSV file
with open('emails.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Emails'])  # Write header

    for email in all_emails:
        writer.writerow([email])  # Write each email in a new row

print(f"Saved {len(all_emails)} emails to emails.csv.")
