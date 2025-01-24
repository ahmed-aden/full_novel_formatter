Web scraper for fullnovel

Setup 

Create a virtual environment
```
python3 -m venv myenv
```

Activate your virtual environment
```
source myenv/bin/activate
```
Install dependencies
```
pip install requests
pip install beautifulsoup4

```
Run script

- Input a link from fullnovel.com via the command line, eg "https://novelfull.com/lord-of-the-mysteries.html?page=1"
- Files in txt & epub format will downloaded in chapters and chapters-epub directories

```
python3 main.py
```

