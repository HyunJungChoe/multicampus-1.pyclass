import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='9999', # 루트계정 본인 비번
    db='sqldb',  # 접속하려는 데이터베이스 명
    charset='utf8'
)

cursor = conn.cursor()

# 퀴즈 1:
# buyTbl에서 2열만 출력하기
print('-'*30)
cursor.execute('select * from buyTbl;')
result = cursor.fetchall()
# print(result)
# 한행씩 레코드 출력
for item in result:
    print(item)

