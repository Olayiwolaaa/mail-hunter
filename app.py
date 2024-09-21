import re
import requests
from bs4 import BeautifulSoup

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

# Example usage
url = 'https://business.nova.edu/people/index.html'
emails = scrape_emails(url)

# Printing the emails found
for email in emails:
    print(email)
