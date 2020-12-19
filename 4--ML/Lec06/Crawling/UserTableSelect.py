import pymysql
id , name , email, year = '','','',''
con = pymysql.connect(host='127.0.0.1', user='root',
     password='1234', db ='pythondb', charset='utf8')
cur = con.cursor()
cur.execute('select * from usertable')
while (True):
    row = cur.fetchone()
    if row== None: break
    id = row[0]
    name = row[1]
    email = row[2]
    year = row[3]
    print("%5s %5s %15s %d" % (id,name,email,year))

con.close()