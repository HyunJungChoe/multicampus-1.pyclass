
import pymysql
con, cur = None, None
con = pymysql.connect(host='127.0.0.1', user='root',
     password='1234', db ='pythondb', charset='utf8')
cur = con.cursor()
sql = 'insert into userTable values (%s,%s,%s,%s)'
id , name, email, year = '','','',''
while(True):
    id = input ("사용자 ID ==> ")
    if id == "": break
    name = input ("사용자 이름 ==> ")
    email = input ("사용자 이메일 ==> ")
    year = input ("사용자 출생년도 ==> ")
    cur.execute(sql, (id, name, email, year))

con.commit()
con.close()
