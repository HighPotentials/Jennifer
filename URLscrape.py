__author__ = 'Alexander'

from bs4 import BeautifulSoup
import json
import requests

r=requests.get('http://www.reddit.com')
pageHTML=r.text
soup=BeautifulSoup("".join(pageHTML))
sAll=soup.findAll("a")

for href in sAll:
    print(href)