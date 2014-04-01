import pymysql
conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs', db='zario_bigdata')
cur = conn.cursor()



def importToDB(itemList):
    # Invoeren van records


    for item in itemList:
        # Invoeren records in DB
        cur.execute("INSERT INTO price VALUES (NULL ,  '" + item[0] + "',  '" + item[1] + "',  '" + item[2] + "',  '" + item[3] + "', '" + item[4] + "', CURDATE());");


def show():
    #Ophalen van records
    cur.execute("SELECT * FROM popularity")
    for r in cur.fetchall():
        print(r)

cur.close()
conn.close()