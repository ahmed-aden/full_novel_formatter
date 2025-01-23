import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# global constants
BASE_URL = "https://novelfull.com"
NUM_OF_CHAPTERS = 50

## so this gets all the links on the first page. 

def scrape(URL: str) -> str:
    """:returns: html content from page"""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def get_links(chapters_page_url: str) -> list[str]:
    soup = scrape(chapters_page_url)
    container = soup.find(id="list-chapter")
    links = container.find_all("a")
    # attach the base url to the relative chapter links using URL join
    href_values = [urljoin(BASE_URL, link.get('href')) for link in links]
    return href_values
    
def get_last_page_num(url: str) -> int:
    """:returns: the upper bound of which we will be searching using the links"""
    soup = scrape(url)
    last_page = soup.find(class_="last")
    link = last_page.find("a")
    return (int(link['data-page']) + 1) 

def get_chapters(url: str) -> list[str]:
    """:returns: a list of chapters links available on the page"""
    links = get_links(url)
    chapter_links = links[0:NUM_OF_CHAPTERS]
    return chapter_links



