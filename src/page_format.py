import requests
from bs4 import BeautifulSoup
import os


def get_story(URL: str):
    # get the page from the URL
    page = requests.get(URL)
    # scrape the html off the page
    soup = BeautifulSoup(page.content, "html.parser")
    # get the title tag
    
    
    # get the chapter content
    story = soup.find(id="chapter-content")
    # get the story in the chapter
    content = story.find_all("p")
    
    # alr i got the chapter title
    chapter_title = content[2].text.strip()
    print(f" chapter title: {chapter_title}")
    chapter_text = ""
    for line in content:
        # strip the useless stuff, and add 2 newlines
        chapter_text += line.text.strip() + "\n\n" 
    
    # save to txt file
    chapter_number = 1 # change chapter number to be dynamic
    # create directory
    directory = "chapters"
    # create dir if it does not exist
    os.makedirs(directory, exist_ok=True)
    with open(f'{directory}/chapter{chapter_number}.txt', 'w') as f:
        f.write(chapter_text)
    
    


def main():
    # TODO replace URL with it being passed from another function which scrapes URLS from the main page
    URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
    get_story(URL)
    # what page format does
    # is given a chapter link
    # it will save it to a txt file
    # now i want to be able to put all these txt files in a directory
        # create directory if not existing
        # save all txt file to directory
        

if __name__ == '__main__':
    main()
    

