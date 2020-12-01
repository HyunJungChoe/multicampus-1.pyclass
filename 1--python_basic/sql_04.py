
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='****', # 루트계정 본인 비번
    db='sqldb2',  # 접속하려는 데이터베이스 명
    charset='utf8'
)


# 연결한 데이타베이스에 새 테이블 생성
# bookTbl 테이블
# id int auto_increment primary key  책아이디
# title text 책제목
# writer text 저자
# page int 페이지수
# price int 가격

cur = conn.cursor()


# sql 실행
# cur.execute('''
#                 create table if not exists bookTbl
#                 (
#                     id int PRIMARY KEY not null AUTO_INCREMENT,
#                     title text not null,
#                     writer varchar(30),
#                     page int not null,
#                     price int not null
#                 );
#                 ''')

# 레코드 삽입 1 : 필드명 지정 X
#  INSERT INTO 테이블명 VALUES(..,..,...);
# cur.execute(''' INSERT INTO bookTbl
#                         VALUES(NULL, '점프투파이썬', '박응용', 500, 30000);
#                 ''')
# conn.commit()



# 레코드 삽입 2 : 필드명 지정 O
#  INSERT INTO 테이블명 (필드명1,...)
#                       VALUES(값1,..,...);
# sql변수 = '''  INSERT INTO 테이블명 (필드명1,...)
#                   VALUES(%s, .... ); '''
# cursor.execute(sql변수, (값1, ... ))

# sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
# cur.execute(sql, ('이것이 MySQL이다','우재남',800,40000))


# 레코드 삽입 3 : 필드명 지정 O, 다중 레코드 삽입 방식

#  INSERT INTO 테이블명 (필드명1,...)
#                       VALUES(값1,..,...);

# sql변수 = '''  INSERT INTO 테이블명 (필드명1,...)
#                   VALUES(%s, .... ); '''

# 레코드 데이타를 2차원 튜플로 저장
# data = ( (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...) ...)

# cursor.executemany( sql변수, data )

sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
data = (    ('이것이 C','김C',800, 70000),
            ('이것이 ORACLE','윤오라클',800, 6000),
            ('머신러닝 핸드북','송머신',500, 55000)  )
cur.executemany(sql, data)


# 데이터 베이스 반영
conn.commit()


# 결과 확인
cur.execute('SELECt * FROM bookTbl;')
result = cur.fetchall()
print(result)
print('-'*30)



# 데이타베이스 종료
conn.close()


