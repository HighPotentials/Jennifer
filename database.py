import pymysql
conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs', db='zario_bigdata')
cur = conn.cursor()

#Ophalen van records
cur.execute("SELECT * FROM popularity")
for r in cur.fetchall():
    print(r)

# Invoeren van records
cur.execute("INSERT INTO popularity VALUES (NULL ,  'Philips 1',  'tv',  'bol',  '1');");
cur.close()
conn.close()