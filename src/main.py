from get_links import get_chapters
from page_format import get_story

def write_stories(URL: str):
    """should write down the 50 txt files, given a link such as below"""
    chapter_links = get_chapters(URL)
    for chapter in chapter_links:
        get_story(chapter)
    



def main():
    chapter_url = "https://novelfull.com/lord-of-the-mysteries.html"
    write_stories(chapter_url)
    

if __name__ == '__main__':
    main()