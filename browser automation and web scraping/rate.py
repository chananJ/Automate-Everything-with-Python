from bs4 import BeautifulSoup
import requests
def get_currency(in_curr, out_curr):
    url=f'https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1'
    content=requests.get(url).text
    soup=BeautifulSoup(content,'html.parser')
    currency= soup.find("span",class_="ccOutputRslt").get_text()
    currency=float(currency[0:-4])
    return currency

print(get_currency('EUR','ILS'))



