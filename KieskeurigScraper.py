from bs4 import BeautifulSoup
import json
import requests

json_file = 'output.json'

# List of products to be scraped
products = [
    'http://www.kieskeurig.nl/mobiel/gsm/samsung/galaxy-s4-i9505-zwart/prijzen/1174247',
    'http://www.kieskeurig.nl/mobiel/gsm/samsung/galaxy-s4-i9505-zwart/prijzen/1174247',
    ]


with open(json_file, 'a', 1, encoding='utf8') as output_file:
    
    # Loop array
    for product in products:
        
        r=requests.get(product)
        pageHTML=r.text
        soup=BeautifulSoup("".join(pageHTML))
        sAll=soup.findAll("td", { "class" : "prijs" })

        
        # Scrape product name from title
        text = soup.title.text
        head, sep, tail = text.partition(' kopen?')

        print(head)
              
        # Output all prices
        for price in sAll:
                for child in price:
                    p = child.string
                    prijs = p[19:]

                    print(prijs)

