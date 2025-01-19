import requests
from bs4 import BeautifulSoup



def get_story(URL: str):
    # get the page from the URL
    page = requests.get(URL)
    # scrape the html off the page
    soup = BeautifulSoup(page.content, "html.parser")
    # get the chapter content
    story = soup.find(id="chapter-content")
    # get the story in the chapter
    content = story.find_all("p")
    # for each line in the story
    for line in content:
        # strip the useless stuff, and add 2 newlines
        print(line.text.strip(), end="\n" * 2)


def main():
    # TODO replace URL with it being passed from another function which scrapes URLS from the main page
    URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
    get_story(URL)

if __name__ == '__main__':
    main()
    

