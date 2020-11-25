
#  파이참에서 프로젝트로 설정된 폴더안에
#  파이썬 파일 생성 - sqlPython_01.py

#  mysql 설치 확인
#  pymysql 파이썬 모듈 확인
#  파이참에서 [File]-[Settings] 클릭후 [Project] 에서 pymysql 목록 확인
#  레퍼런스 사이트  https://github.com/PyMySQL/PyMySQL/
#  [Terminal] 클릭하고 명령 직접 입력
#  pip list
#  pymysql 목록 확인
#  없으면 설치
#  pip install pymysql

# 모듈 임포트
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='****', # 루트계정 본인 비번
    db='worlddb',  # 접속하려는 데이터베이스 명
    charset='utf8'
)
# print(conn, type(conn))

cursor = conn.cursor()
# cursor.execute('SELECT * FROM city LIMIT 5;')

# result = cursor.fetchall()
# for item in result:
#     print(item)

# 변수명 = cursor.fetchall() / cursor.fetchone() / cursor.fetchmany(n)
# sql 명령의 결과 1개만 반환 cursor.fetchone() => 튜플
print('-'*30)
cursor.execute('SELECT Name, Population FROM city;')
result = cursor.fetchone()
print(result)

# sql 명령의 결과  cursor.fetchall() => 2차원 튜플구조
print('-'*30)
cursor.execute('SELECT Name, Population FROM city;')
result = cursor.fetchall()
print(len(result)) # 4079

# sql 명령의 결과  cursor.fetchmany(size) => 2차원 튜플구조
print('-'*30)
cursor.execute('SELECT Name, Population FROM city;')
result = cursor.fetchmany(5)
print(result)
print(len(result))
for item in result:
    print(item)


# 데이타베이스 종료
conn.close()