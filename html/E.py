import requests
from bs4 import BeautifulSoup

HEADERS = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

page = 1
ranks = 1

while page < 6:

    URL = "https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page="


    DATA = requests.get(URL, headers = HEADERS)
    SOUP = BeautifulSoup(DATA.text, "html.parser")

    Books = SOUP.find_all("div", {"class" : "product-info-view"})

    print(Books)


    for book in Books:
        title = book.select_one("h3 > a").text
        released = book.select_one("h3 > span").text
        author = book.select_one("div.product-shelf-author > a").text

        print(str(ranks) + "." + title + "by" + author + " " +released)
        ranks += 1
    
    page += 1