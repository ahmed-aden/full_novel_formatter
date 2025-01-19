import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://novelfull.com/lord-of-the-mysteries.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
container = soup.find(id="list-chapter")
base_url = "https://novelfull.com/"
links = container.find_all("a")

# links for everything on page 1
href_values = [urljoin(base_url, link.get('href')) for link in links]


for href in href_values:
    print(href, end="\n" *2)

## so this gets all the links on the first page. 
## hmm 







