__author__ = 'Alexander'
__author__ = 'Alexander'
from bs4 import BeautifulSoup
import requests
import popularityToDB



categories={"Mobile":"http://goo.gl/76aDcB", "Tablets":
    "http://goo.gl/tx2YPU", "Laptops":
    "http://goo.gl/H0lRH3"}

#scrapes HTML from webpage
for key, url in categories.items():

    r=requests.get(url)
    pageHTML=r.text

    #defines soup function
    soup=BeautifulSoup(r.text)

    #finds product element on webpage
    products=soup.findAll('h3', attrs= {'class': 'newaps'})
    print(products)


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

            y+=1
            itemList.append([(product.text), key, "Beslist",y])



    #calls function
    toplst_products()
    print(itemList)

    popularityToDB.importToDB(itemList)
