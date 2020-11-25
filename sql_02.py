import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='****', # 루트계정 본인 비번
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
# 특정행의 특정열 : 튜플명[행][열]
print(result[0][2])

for i in range(0, len(result)-1):
    print(result[i][1])

# 퀴즈 2:
# buyTbl에서 마지막행만 출력하기

# 퀴즈 3:
# buyTbl에서 3행 3열의 값 출력하기

# 퀴즈 4:
# userTbl에서 지역(addr)값이 '서울'인 레코드만 표시하기
print('-'*30)
cursor.execute('SELECT * FROM userTbl WHERE addr = "서울";')
result = cursor.fetchall()
for item in result:
    print(item)


# 퀴즈 5:
# buyTbl에서 아이디(uesrID)값이 'KBS'인 레코드만 표시하기
print('-'*30)
cursor.execute('SELECT * FROM userTbl WHERE userID = "KBS";')
result = cursor.fetchall()
for item in result:
    print(item)

# 데이타베이스 종료
conn.close()