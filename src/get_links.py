import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from page_format import get_story

# global constant
BASE_URL = "https://novelfull.com"
## so this gets all the links on the first page. 

def scrape(URL: str):
    """:returns: html content from page"""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup
    

def get_links(chapters_page_url: str) -> list[str]:
    # TODO replace with maybe this function being called multiple times or smth
    # auto mate somehow
    
    # get the page
    # page = requests.get(chapters_page_url)
    # parse the content to get the html
    # soup = BeautifulSoup(page.content, "html.parser")
    soup = scrape(chapters_page_url)
    # get the chapter links
    container = soup.find(id="list-chapter")
    # get the specific links within the content
    links = container.find_all("a")
    # define base url
    
    # attach the base url to the relative chapter links using URL join
    href_values = [urljoin(BASE_URL, link.get('href')) for link in links]
    return href_values
    


def get_last_page_num(url: str):
    """:returns: the range of which we will be searching using the links"""
    # after we return the upper bound, the link can be changed dynamically within the range loop
    # find the anchor tag with the title
    soup = scrape(url)
    # well we could look for li last class
    # and then get the link inside the anchor tag 
    
    
    last_page = soup.find(class_="last")
    link = last_page.find("a")
    return (int(link['data-page']) + 1) # returns the last page on which the chapters can be found

def get_chapters(url: str) -> list[str]:
    """:returns: a list of chapters available on the page"""
    links = get_links(url)
    chapter_links = links[0:50]
    return chapter_links

def get_book(last_page_num: int):
    # we need last page
    # we also need main page url?
    # "https://novelfull.com/lord-of-the-mysteries.html?page={last_page_num}"
    # loop over rnage(last_page_num)
        # get page content
        # store it
        # continue
    book = []
    for _ in range(1, last_page_num+1):
        curr_url = "https://novelfull.com/lord-of-the-mysteries.html?page={last_page_num}"
        chapters = get_chapters(curr_url)
        # get chapters gets all the absolute chapter links
        # which returns a list
        for chapter in chapters:
            # so for each link/to chapter in chapters
            chapter_page = get_story(chapter)
            # we call get story
            # which scrapes the story from it
            # however get story doesnt actually reutnr anything so wtf are we appending
            book.append(chapter_page)

            
    return book





def main():
    URL = "https://novelfull.com/lord-of-the-mysteries.html"
    URL2 = "https://novelfull.com/lord-of-the-mysteries.html?page=2"
    # get_book(get_last_page_num(URL))
    foo = get_chapters(URL2)
    for bar in foo:
        print(bar, end="\n\n")

if __name__ == '__main__':
    main()
# current what page format does
# is that given a link


# TODO: need to get the function to work such that it passes me two varaibles
# it should pass me a list of all links, wheres its chapters 1-50
# and then it should pass me a link of the next page
# ^^ think about how to implement the second functionality
# format:  https://novelfull.com/lord-of-the-mysteries.html?page=29

# TODO: 
# this project should be given a link of the main chapter page and be able to scrape all of them
# to do this, shold be able to take the anchor tag which has a title of last
# and be able to scrape that link
# the last number of the link, will be the range of data we want to dry scraping
# with the dynamic link "https://novelfull.com/lord-of-the-mysteries.html?page=x" where x is a number from 1 to last
# afterwoulds it calls the normal scrape function which doesnt get the range // or rather only during the first call
# will we call the range fucntion
# then we could enter a range loop
# scraping the html and parsing it
# hmm and then im thinking what do we do with the data we want
# is we convert to epub using a library
# how should we store the data thoo.
# ig we'll fix that later


# TODO: current -> fix the scraping function when given the main link page
# TODO: i want a few functions:
# TASK 1 -> function that gets the range of main page links we want to scrape. 
# so it looks for anchor tag with title of last
# and uses "https://novelfull.com/lord-of-the-mysteries.html?page=x"
# function find_range()

#TODO: 
# TASK 2 -> function that purely gets the chapters from the pages we feed it, and nothing else
# i think this can take our implemeneted get_links, and stop at 50
# fn get_chapters

#TODO: 
# Task 3 -> function that calls function find_range
# and then calls get chapters on each page
# and stores all chapter links of the book in a list


#TODO 
# Task 4 -> function that calls page_format function, on all chapter links

#TODO: 
# Task 5 -> we want earlier to pass back the text as txt?

#TODO:
# Task 6 -> convert txt to epub



