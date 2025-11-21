import requests
from bs4 import BeautifulSoup

print("Interactive Web Scraper")
url = input("Enter website URL to scrape: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

print("\n--- SCRAPED DATA ---")
for i in range(len(quotes)):
    print(f"{i+1}. {quotes[i].text} - {authors[i].text}")
