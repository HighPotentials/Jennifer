import requests
import bs4
 


# Testje

r = requests.get("http://www.facebook.com/")
soup = bs4.BeautifulSoup(r.text)

print(soup.title.text)
    
