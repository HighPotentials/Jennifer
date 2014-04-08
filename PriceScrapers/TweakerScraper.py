from bs4 import BeautifulSoup
import requests
import Google
import priceToDB



keywords = [
    'iphone 4s tweakers pricewatch',
    'htc one 32gb tweakers pricewatch'
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

print(itemList)
priceToDB.priceToDB(itemList)



                        


