import requests
from bs4 import BeautifulSoup
import json

columns = []

for i in range(1, 9999):
    response = requests.get(f"https://lajornadahidalgo.com/author/naty-castrejon/page/{i}")

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("div", {"class": "post-details"})
    for item in items:
        columns.append({
            "title": item.find("h2", {"class": "post-title"}).get_text(),
            "description": item.find("p", {"class": "post-excerpt"}).get_text(),
            "link": item.find("a", {"class": "more-link button"})["href"]
        })

with open('dataNaty.json', 'w') as file:
    json.dump(columns, file, indent=2)
