import requests
from bs4 import BeautifulSoup

HEADERS = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

print("------------------")
print("1. All time")
print("2. Last 24 hours")
print("3. Last 3 days")
print("4. Last 7 days")
ans = int(input("Time period to check(Write the number)?"))

if ans == 1:
    URL = "https://www.planetminecraft.com/data-packs/"
elif ans == 2:
    URL ="https://www.planetminecraft.com/data-packs/?time_machine=last24h"
elif ans == 3:
    URL ="https://www.planetminecraft.com/data-packs/?time_machine=last3d"
elif ans == 4:
    URL ="https://www.planetminecraft.com/data-packs/?time_machine=last7d"

URL = "https://www.planetminecraft.com/texture-packs/"
DATA = requests.get(URL, headers = HEADERS)
SOUP = BeautifulSoup(DATA.text, "html.parser")

PACKS = SOUP.find_all("div", {"class":"r-info"})
print(PACKS)

for pack in PACKS:
    title = pack.select_one("a").text
    link = "(https://www.planetminecraft.com" + pack.select_one("a").get("href") + ")"
    print(title + link)

