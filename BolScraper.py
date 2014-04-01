__author__ = 'Wesley'
from bs4 import BeautifulSoup
import requests
import popularityToDB



categories={"Mobile":"http://goo.gl/BnN2Oh", "Tablets":
    "http://goo.gl/uf8OEt", "Laptops":
    "http://goo.gl/V2d0IN"}

#scrapes HTML from webpage
for key, url in categories.items():

    r=requests.get(url)
    pageHTML=r.text

    #defines soup function
    soup=BeautifulSoup(r.text)

    #finds product element on webpage
    products=soup.findAll('div', attrs= {'class': 'product_line'})


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
                    itemList.append([link.get('title'), key, "Bol", y])


    #calls function
    toplst_products()
    print(itemList)

    popularityToDB.importToDB(itemList)