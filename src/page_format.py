import requests
from bs4 import BeautifulSoup


URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

story = soup.find(id="chapter-content")
content = story.find_all("p")

for line in content:
    print(line.text.strip(), end="\n" *2)
    
