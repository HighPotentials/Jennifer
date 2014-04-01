import pymysql
conn = pymysql.connect(host='zario.nl', unix_socket='/tmp/mysql.sock', user='zario_bigdata', passwd='w90vs', db='zario_bigdata')
cur = conn.cursor()
cur.execute("SELECT * FROM popularity")
for response in cur:
    print(response)
cur.close()
conn.close()