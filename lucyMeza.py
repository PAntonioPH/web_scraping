import requests
from bs4 import BeautifulSoup
import json

columns = []

# response = requests.get("https://www.senado.gob.mx/65/intervenciones/1035#info")
# soup = BeautifulSoup(response.text, "html.parser")
# items = soup.find_all("div", {"class": "panel-body"})
# dates = soup.find_all("div", {"class": "panel-heading text-right"})
#
# for item, date in zip(items, dates):
#     descriptions = item.find_all("p")
#     columns.append({
#         "title": item.find("strong").get_text(),
#         "description": "\n".join([description.get_text() for description in descriptions]),
#         "img": item.find("img")["src"] if item.find("img") else "None",
#         "date": date.find("strong").get_text(),
#         "link": f"https://www.senado.gob.mx{item.find('a')['href']}"
#     })
#
# with open('dataIntervencionesLucyMeza.json', 'w') as file:
#     json.dump(columns, file, indent=2)


response = requests.get("https://www.senado.gob.mx/65/senador/1035")
soup = BeautifulSoup(response.text, "html.parser")
items = soup.find_all("div", {"class": "panel-body"})

for item in items:
    print(item.find("div", {"class": "col-sm-7"}).find('strong').find('strong').get_text() if item.find("div", {"class": "col-sm-7"}) else "Nones")

    itemsP = item.find_all("p")

    columns.append({
        "title": item.find("div", {"class": "col-sm-7"}).find('strong').find('strong').get_text() if item.find("div", {"class": "col-sm-7"}) else "Nones",
        "link": f"https://www.senado.gob.mx{itemsP[0].find('a')['href']}" if (len(itemsP) > 0 and itemsP[0].find('a')) else "Nones",
        "description": itemsP[0].find('a').get_text() if (len(itemsP) > 0 and itemsP[0].find('a')) else "Nones",
        "action": itemsP[1].find('b').get_text() if len(itemsP) > 1 and itemsP[1].find('b') else "Nones",
        "date": itemsP[2].find('strong').next_sibling if len(itemsP) > 2 and itemsP[2].find('strong') else "Nones",
    })

initiatives = list(filter(lambda x: "Iniciativas" in x["title"], columns))
proposals = list(filter(lambda x: "Proposiciones" in x["title"], columns))
communications = list(filter(lambda x: "Comunicaciones" in x["title"], columns))

with open('dataIniciativasLucyMeza.json', 'w') as file:
    json.dump(initiatives, file, indent=2)

with open('dataProposicionesLucyMeza.json', 'w') as file:
    json.dump(proposals, file, indent=2)

with open('dataComunicacionesLucyMeza.json', 'w') as file:
    json.dump(communications, file, indent=2)
