import pymysql
conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs', db='zario_bigdata')
cur = conn.cursor()



def importToDB(itemList):

    # Invoeren van records
    for item in itemList:
        # Invoeren records in DB
        cur.execute("INSERT INTO popularity VALUES (NULL ,  '" + item[0] + "',  '" + item[1] + "',  '" + item[2] + "',  " + str(item[3]) + ", CURDATE());");


def show():
    #Ophalen van records
    arr = [];
    cur.execute("SELECT * FROM popularity")
    for r in cur.fetchall():
        arr.append(r)

    return(arr)

def query(query):
    #Ophalen van records
    arr = [];
    cur.execute(query)
    for r in cur.fetchall():
        arr.append(r)

    return(arr)



#cur.close()
#conn.close()