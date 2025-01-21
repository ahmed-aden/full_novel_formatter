from bs4 import BeautifulSoup
import requests
from get_links import scrape



URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
URL2 = "https://novelfull.com/lord-of-the-mysteries/chapter-2-situation.html"
def main():
    
    page2 = scrape(URL2)
    print(page2)

if __name__ == '__main__':
    main()