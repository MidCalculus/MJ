import requests

HEADERS = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
PAGES = ["home", "about", "academics", "admissions", "careers", "community", "student-life"]


for name in PAGES:
    URL = "https://www.yisseoul.org/" + name
    DATA = requests.get(URL, headers = HEADERS)
    with open( name +".html", 'w', encoding = "UTF-8") as f:
        f.write(DATA.text)
