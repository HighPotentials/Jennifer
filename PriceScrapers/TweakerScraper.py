from bs4 import BeautifulSoup
import requests

from PriceScrapers import priceToDB


json_file = 'output.json'

# List of products to be scraped
products = [
    'http://tweakers.net/pricewatch/325799/samsung-galaxy-s4-16gb-zwart.html',
    'http://tweakers.net/pricewatch/355003/motorola-moto-g-8gb-zwart.html'
    ]


itemList = []

with open(json_file, 'a', 1, encoding='utf8') as output_file:
    
    # Loop array
    for product in products:
        
        r=requests.get(product)
        pageHTML=r.text
        soup=BeautifulSoup("".join(pageHTML))
        sAll=soup.findAll("tr", { "class" : "total" })

        
        # Scrape product name from title
        text = soup.title.text
        head, sep, tail = text.partition('&euro;')


        prijsArr = [head]
              
        # Output all prices
        for price in sAll:

            price = str(price)
            price = price[48:]
            price = price.split("<")[0]
            price = price.replace(",-", "")
            price = price.replace(",", ".")

            prijsArr.append(price)

        priceList = prijsArr[0:4]
        priceList.append('Tweakers')

        # print(priceList)

        itemList.append(priceList)

    priceToDB.priceToDB(itemList)



                        


