import requests
import pandas as pd
from bs4 import BeautifulSoup

#url = "https://www.basket.co.il/stats-individual.asp?cYear=2024"
url = "https://www.nba.com/standings"
r = requests.get(url)
print(r)
soup= BeautifulSoup(r.text,"lxml")
table=soup.find("table",class_="Crom_container__C45Ti crom-container")
print(table)
#
#
# headers=table.find_all("td")
# #print(headers)
#
# titles=[]
# for i in headers:
#     title=i.text
#     print(str(title))
#     titles.append(title)
# print(titles)
