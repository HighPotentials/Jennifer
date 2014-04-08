import pymysql
conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs', db='zario_bigdata')
cur = conn.cursor()


def priceToDB(itemList):
    for item in itemList:
        # Invoeren records in DB
        cur.execute("INSERT INTO price VALUES (NULL ,  '" + item[0] + "',  '" + item[1] + "',  '" + item[2] + "',  '" + item[3] + "', '" + item[4] + "', CURDATE());");

#cur.close()
#conn.close()