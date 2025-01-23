import requests
from bs4 import BeautifulSoup
import os
# from get_links import scrape

def scrape(URL: str) -> str:
    """:returns: html content from page"""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup



# REFACTORING
# TODO: create function to get the titles
# TODO: get a function to create a new txt page
# TODO: 
# TODO
def get_title(header: str) -> str:
    chapter_title_tag = header.find('h3')
    if chapter_title_tag:
        chapter_title = chapter_title_tag.text.strip()
    else:
        chapter_title = "Unknown Title"
    return chapter_title


def get_story(URL: str) -> None:
    
    soup = scrape(URL)
    chapter_content = soup.find('div', {'id': 'chapter-content'})
    # this is the content within the page
    next_div = chapter_content.find_next_sibling('div') 
    chapter_title = get_title(chapter_content)
    print(f"Chapter title: {chapter_title}")


    chapter_text = f"{chapter_title} \n\n" 
    # strip away the html from the content
    for line in next_div.find_all('p'):
        chapter_text += line.text.strip() + "\n\n" 
    
    # save to txt file
    chapter_number = 2 # change chapter number to be dynamic
    # create directory
    directory = "chapters"
    # create dir if it does not exist
    os.makedirs(directory, exist_ok=True)
    with open(f'{directory}/chapter{chapter_number}.txt', 'w') as f:
        f.write(chapter_text)
    
    


def main():
    # TODO replace URL with it being passed from another function which scrapes URLS from the main page
    URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
    URL4 = "https://novelfull.com/lord-of-the-mysteries/chapter-4-divination.html"
    get_story(URL4)
    
    # what page format does
    # is given a chapter link
    # it will save it to a txt file
    # now i want to be able to put all these txt files in a directory
        # create directory if not existing
        # save all txt file to directory
        

if __name__ == '__main__':
    main()
    
    

