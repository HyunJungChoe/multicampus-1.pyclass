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


# 데이타베이스 생성 : 권장하지 않음.
'''
DROP DATABASE IF EXISTS 데이타베이스명;
CREATE DATABASE 데이타베이스명;
'''

cursor.execute('DROP DATABASE IF EXISTS sqldb2;')
cursor.execute('CREATE DATABASE sqldb2;')



# 테이블 생성
cursor.execute('USE sqldb2;')
cursor.execute('''
                create table movieTbl
                (
                    movieNum int PRIMARY KEY not null AUTO_INCREMENT, -- 번호(PK)
                    movieName varchar(30) not null, -- 무비명 
                    kind varchar(30), -- 장르명
                    price int not null, -- 대여 가격
                    period int not null -- 대여 기간
                );
                ''')


# 데이타베이스 종료
conn.close()

