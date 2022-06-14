from time import sleep
import requests
from bs4 import BeautifulSoup

url = "https://www.bazos.cz/"
r = requests.get(url)

content = r.text
soup = BeautifulSoup(content, "html.parser")

body = soup.find("body")
body = body.find("div", {"class": "sirka"})
body = body.find("div", {"class", "maincontent"})
inzeraty = body.find_all("div", {"class": "inzeraty"})

for inzerat in inzeraty:
    b = inzerat.find("h2", {"class": "nadpis"})
    inzerat_url = url[:-1] + b.find("a")["href"]

    r = requests.get(inzerat_url)
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    x = soup.find("h1", {"class", "nadpisdetail"})

    print(x.text.strip())