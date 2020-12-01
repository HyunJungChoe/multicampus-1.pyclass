

import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306, # mysql포트
    user='root',  # 접속 계정
    password='9999', # 루트계정 본인 비번
    db='sqldb2',  # 접속하려는 데이터베이스 명
    charset='utf8'
)
cursor = conn.cursor()

# sqlsb2 데이타베이스의 bookTbl 테이블이 있는지 확인
# 테이블이 없다면 sql 실행
# cursor.execute('drop table if exists bookTbl;')
# cursor.execute('''
#                 create table if not exists bookTbl
#                 (
#                     id int PRIMARY KEY not null AUTO_INCREMENT,
#                     title text not null,
#                     writer varchar(30) not null,
#                     page int not null,
#                     price int not null
#                 );
#                 ''')
# cursor.execute(''' INSERT INTO bookTbl
#                         VALUES(NULL, '점프투파이썬', '박응용', 500, 30000);
#                 ''')
# conn.commit()

def showBook():
    # pass
    print('-'*20)
    print(' 책 목록 보기')
    print('-' * 20)
    cursor.execute('SELECT * FROM bookTbl;')
    result = cursor.fetchall()
    for row in result:
        print(row)
    print()


def insertBook():
    # pass
    print('-' * 20)
    print('레코드 삽입하기')
    print('-' * 20)
    title = input(" 책 이름 => ")
    writer = input(" 저자 => ")
    page = input(" 페이지 수 => ")
    price = input(" 가격 => ")
    sql = '''
            INSERT INTO bookTBL(title, writer, page, price)
                VALUES(%s, %s, %s, %s)
          '''
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()
    print('레코드가 삽입되었습니다.\n')


# 수정과 삭제 함수 완성후 테스트
#

def updateBook():
    pass

def deleteBook():
    pass


# 메인 메뉴 표시
while(True):
    choice = int(input('1.목록보기 2.추가 3. 수정 4. 삭제  0. 종료 \n => ' ).strip())
    if choice == 1:
        showBook()
    elif choice == 2:
        insertBook()
    elif choice == 3:
        updateBook()
    elif choice == 4:
        deleteBook()
    elif choice == 0:
        print('프로그램 종료')
        # 데이타베이스 종료
        conn.close()
        break


# 데이타베이스 종료
conn.close()

