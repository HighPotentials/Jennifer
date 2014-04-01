__author__ = 'Alexander'

import pymysql
from difflib import get_close_matches as gcm

conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs',
db='zario_bigdata')

cur = conn.cursor()

databaselst=[]

cur.execute("SELECT * FROM popularity")

databaselst=list(cur.fetchall())
print(databaselst)


"""
def laptop_compare():
    for lst in databaselst:
        if lst[2]=='Laptops':
            for x in lst[1:2]:
                print(gcm(x, lst[1:2], 2))"""
#code voor list comparisons
for lst in databaselst:
    if lst[2]=='Laptops':
        list1 = lst
        list2 = lst
        results = {}
        for i in list1:
            results[i] = list2.count(i)
        print(results)


#difflib.get_close_matches(word, possibilities[, n][, cutoff])




