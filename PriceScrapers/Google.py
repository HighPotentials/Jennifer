__author__ = 'python'

from GoogleSearch import search

def getLink(keyword):
    urlList = []
    for url in search(keyword, tld='nl', lang='nl', stop=1):
        urlList.append(url)

    return(urlList[0])