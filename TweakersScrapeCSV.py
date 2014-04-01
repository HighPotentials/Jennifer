__author__ = 'Alexander'
from bs4 import BeautifulSoup
import csv
import requests


categories={"Mobile":"http://tweakers.net/categorie/215/mobiele-telefoons/producten/", "Tablets":
    "http://tweakers.net/categorie/822/tablets/producten/", "Laptops":
    "http://tweakers.net/categorie/496/laptops/producten/"}

popdata=open('popularity.csv', 'w', newline='')

popularitywriter=csv.writer(popdata, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)

popularitywriter.writerow([])

for category in categories.keys():
    popularitywriter.writerow([category])



#scrapes HTML from webpage
for key, url in categories.items():

    r=requests.get(url)
    pageHTML=r.text

    #defines soup function
    soup=BeautifulSoup(r.text)

    #finds product element on webpage
    products=soup.findAll('p', attrs= {'class': 'ellipsis'})


    #amount of products to include in list
    x=5
    #x is doubled due to website structure
    z=int(x*2)

    itemList = []

    #creates top x list of products
    def toplst_products():
        y=0
        #loops through list of products
        for product in products[0:z]:
            #finds <a> elements
            ps = product.findAll('a')
            #loops through <a> elements found in product element
            for link in ps:
                #ensures that 'none' titles are not included
                if link.get('title')==None:
                    break
                else:
                    # print(link.get('title'))
                    y+=1
                    itemList.append([link.get('title'), key, "Tweakers", y])


    #calls function
    toplst_products()
    print(itemList)
