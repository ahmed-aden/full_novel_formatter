from bs4 import BeautifulSoup
import requests


URL = "https://novelfull.com/lord-of-the-mysteries/chapter-1-crimson.html"
URL2 = "https://novelfull.com/lord-of-the-mysteries/chapter-2-situation.html"
def main():
    response = requests.get(URL2)
    
    html_content = response.text
    print(html_content)
    
    


if __name__ == '__main__':
    main()