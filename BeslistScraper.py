__author__ = 'Alexander'
from bs4 import BeautifulSoup
import requests
import popularityToDB



categories={"Mobile":"http://www.beslist.nl/products/elektronica/elek_mobiele_telefoons/?sortby=popularity", "Tablets":
    "http://www.beslist.nl/products/computers/comp_tablets/?sortby=popularity", "Laptops":
    "http://www.beslist.nl/products/computers/comp_laptopsnotebooks/?sortby=popularity"}

#scrapes HTML from webpage
for key, url in categories.items():

    r=requests.get(url)
    pageHTML=r.text

    #defines soup function
    soup=BeautifulSoup(r.text)

    #finds product element on webpage
    products=soup.findAll('a', attrs= {'class': 'bc_title'})
   

    #amount of products to include in list
    x=5
    #x is doubled due to website structure
    z=int(x)

    itemList = []

    #creates top x list of products
    def toplst_products():
        y=0
        #loops through list of products
        for product in products[0:z]:

            y+=1
            itemList.append([(product.text), key, "Beslist",y])



    #calls function
    toplst_products()
    print(itemList)

    popularityToDB.importToDB(itemList)
