import requests
from bs4 import BeautifulSoup
import os
import subprocess

def scrape(URL: str) -> str:
    """:returns: html content from page"""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def get_title(header: str) -> str:
    chapter_title_tag = header.find('h3')
    if chapter_title_tag:
        chapter_title = chapter_title_tag.text.strip()
    else:
        chapter_title = "Unknown Title"
    return chapter_title

def convert_txt_to_epub(txt_file: str, epub_file: str) -> None:
    """converts txt files in chapters to epub""" 
    # i think we can call this function in write to chapters
    cmd = ["pandoc", txt_file, "-o", epub_file]
    subprocess.run(cmd, check=True)
    print("Conversion successful")

def write_to_chapters_dir(page: str) -> None:
    """creates a txt file within the chapters directory and writes to the txt file."""
    directory = "chapters"
    directory_epub = "chapters-epub"
    chapter_title = page.partition('\n')[0] # make this receive an integer as a function
    
    # there is no directory make as this or file..

    # this checks to see if there is a directory, and if not, creates one.
    os.makedirs(directory, exist_ok=True)
    
    with open(f"{directory}/{chapter_title}.txt", 'w') as writer:
        writer.write(page)
    os.makedirs(directory_epub, exist_ok=True)
    convert_txt_to_epub(f"{directory}/{chapter_title}.txt", f"{directory_epub}/{chapter_title}.epub")

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
    # write to a txt file
    write_to_chapters_dir(chapter_text)






def main():
    # URLS for testing
    URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
    URL4 = "https://novelfull.com/lord-of-the-mysteries/chapter-4-divination.html"
    URL2 = "https://novelfull.com/lord-of-the-mysteries/chapter-2-situation.html"
    get_story(URL2)
    
if __name__ == '__main__':
    main()
    
    

