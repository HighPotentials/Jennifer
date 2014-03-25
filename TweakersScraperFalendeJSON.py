__author__ = 'Alexander'
from bs4 import BeautifulSoup
import json
import requests


categories=["http://tweakers.net/categorie/215/mobiele-telefoons/producten/",
            "http://tweakers.net/categorie/822/tablets/producten/",
            "http://tweakers.net/categorie/496/laptops/producten/"]


#scrapes HTML from webpage
for category in categories:
    json_file='output_'+str(category) +".json"

    r=requests.get(category)
    pageHTML=r.text

    #defines soup function
    soup=BeautifulSoup(r.text)

    #finds product element on webpage
    products=soup.findAll('p', attrs= {'class': 'ellipsis'})


    #amount of products to include in list
    x=5
    #x is doubled due to website structure
    z=int(x*2)

    #creates top x list of products
    def toplst_products():
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
                    print(link.get('title'))
                    json.dump(link.get('title'), json_file, ensure_ascii=False)
                    json_file.write('\n')
    #calls function
    toplst_products()
