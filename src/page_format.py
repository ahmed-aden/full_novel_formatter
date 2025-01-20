import requests
from bs4 import BeautifulSoup
import os


def get_story(URL: str):
    # get the page from the URL
    page = requests.get(URL)
    # scrape the html off the page
    soup = BeautifulSoup(page.content, "html.parser")
    # get the title tag
    
    # print(soup.prettify()[:5000])  
    
    # get the chapter content
    # story = soup.find(id="chapter-content")
    chapter_content = soup.find('div', {'id': 'chapter-content'})
    # print(story.prettify()[:5000])  
    # get the story in the chapter
    if not chapter_content:
        print("chp content not found")
        return
    
    # alr i got the chapter title
    chapter_title_tag = chapter_content.find('h3')
    if chapter_title_tag:
        chapter_title = chapter_title_tag.text.strip()
    else:
        chapter_title = "Unknown Title"
    
    print(f"Chapter title: {chapter_title}")


    chapter_text = ""
    for line in chapter_content.find_all('p'):
        # strip the useless stuff, and add 2 newlines
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
    URL2 = "https://novelfull.com/lord-of-the-mysteries/chapter-2-situation.html"
    get_story(URL2)
    # what page format does
    # is given a chapter link
    # it will save it to a txt file
    # now i want to be able to put all these txt files in a directory
        # create directory if not existing
        # save all txt file to directory
        

if __name__ == '__main__':
    main()
    
    

