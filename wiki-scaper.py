import requests
from bs4 import BeautifulSoup, NavigableString
import os

def between(cur, end):
    while cur and cur != end:
        if isinstance(cur, NavigableString):
            text = cur.strip()
            if len(text) and not text.startswith('.'):
                yield text
        cur = cur.next_element

response = requests.get(
	url="https://en.wikipedia.org/wiki/Electromagnetism",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading").text

subpages = soup.find_all("span", {"class": "mw-headline"})

os.makedirs(f'{title}/content', exist_ok=True)

with open(f"{title}/ocw.json", "w") as f:
	f.write(''' {
  "title": "'''
  + title+ '''",
  "authors": [
    "Tarushii Goel"
  ],
  "thumbnail": "",
  "description": "this is cool",
  "tags": [] 
  }
		''')

print("herefjdklafkds")

def doStuff(i):
	p1 = subpages[i]
	p2 = subpages[i+1]
	text = ' '.join(text for text in between(p1, p2))
	with open(f"{title}/content/{i+1}_{p1.text}.md", "w") as f:
		f.write(text)

#doStuff(0)

for i in range(len(subpages)-1):#
	doStuff(i)

