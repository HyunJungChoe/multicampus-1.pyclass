

import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='****', # 루트계정 본인 비번
    db='sqldb2',  # 접속하려는 데이터베이스 명
    charset='utf8'
)

# 작업변수 커서 생성
cursor = conn.cursor()

# MySQL 워크벤치에서 샘플테이블 생성 후 테스트
'''
DROP TABLE IF EXISTS buytbl_sample;
CREATE TABLE buytbl_sample
(
   SELECT * FROM buytbl
);
SELECT * FROM buytbl_sample;

'''

# 샘플 테이블 확인
# cursor.execute('SELECT * FROM buytbl_sample')
# result = cursor.fetchall()
# for item in result:
#     print(item)

# ----------------------------
# 레코드 수정
#  UPDATE 테이블명 SET 컬럼명1 = 값1  WHERE 컬럼명2 = 값2

# sql변수 = '''  UPDATE 테이블명
#               SET 컬럼명1 = %s  WHERE 컬럼명2 = %s; '''
# cursor.execute(sql변수, (값1, ... ))

# buytbl_sample 테이블에서 1번 레코드의 상품명(prodName)을 수정하여라
sql = '''  UPDATE buytbl_sample  
              SET prodname = %s  WHERE num = %s; '''
cursor.execute(sql, ('백팩', 1))
conn.commit()


cursor.execute('SELECT * FROM buytbl_sample')
result = cursor.fetchall()
for item in result:
    print(item)


# ----------------------------
# 레코드 삭제
#  DELETE FROM 테이블명  WHERE 컬럼명 = 값

# sql변수 = '''  DELETE FROM 테이블명
#               WHERE 컬럼명 = = %s; '''
# cursor.execute(sql변수, (값))

sql = '''
        DELETE FROM buytbl_sample
            WHERE num = %s
      '''

# cursor.execute(sql, (3))
try:
    cursor.execute(sql, (3))
except Exception:
    print('오류발생')

conn.commit()

cursor.execute('SELECT * FROM buytbl_sample')
result = cursor.fetchall()
for item in result:
    print(item)


# 데이타베이스 종료
conn.close()

