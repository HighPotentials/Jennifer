from bs4 import BeautifulSoup
import requests
import Google
import priceToDB


keywords = [
    'iphone 5s kieskeurig',
    'htc one zilver kieskeurig'
]

products = []
for keyword in keywords:
    link = Google.getLink(keyword)
    products.append(link)



itemList = []
    
# Loop array
for product in products:

    r=requests.get(product)
    pageHTML=r.text
    soup=BeautifulSoup("".join(pageHTML))
    sAll=soup.findAll("td", { "class" : "prijs" })


    # Scrape product name from title
    text = soup.title.text
    head, sep, tail = text.partition(' kopen?')


    prijsArr = [head]

    # Output all prices
    for price in sAll:
            for child in price:
                p = child.string
                prijs = p[19:]

                # Convert strings to price only
                if prijs.find(',') > 0:
                    end = prijs.find(',')+3
                    prijsInt= prijs[:end]

                    prijsArr.append(prijsInt)

    priceList = prijsArr[0:4]

    if len(priceList) is 3:
        priceList.append('0');

    priceList.append('Kieskeurig')

    itemList.append(priceList)

priceToDB.priceToDB(itemList)



                        


