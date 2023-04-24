from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

@dataclass
class WebsiteWikipediaData:
    website: str
    popularity: str
    frontend: str
    backend: str
    database: str
    notes: str
def fetch_data():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})
    rows = table.find_all("tr")

    wikitable = []

    for row in rows[1:]:
        cells = row.find_all("td")
        website_data = WebsiteWikipediaData(
            website=cells[0].text.strip(),
            popularity=cells[1].text.strip(),
            frontend=cells[2].text.strip(),
            backend=cells[3].text.strip(),
            database=cells[4].text.strip(),
            notes=cells[5].text.strip()
        )
        wikitable.append(website_data)

    return wikitable

if __name__=='__main__':
    data1 = fetch_data()
    for item in data1:
        print(item)
