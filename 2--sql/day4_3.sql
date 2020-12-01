-- 뷰(View)란?
-- 테이블 자료의 일부만 보여주고자 할 때 사용하는 기능
-- 원본 데이터중에서 보는 사람에게 필요한 데이터만을 보여준다.
-- 장점
-- : 보안, 복잡한 쿼리의 단순화 등

-- 쇼핑몰 예) 
-- 메인 관리자 화면 - 매출액 , 상품목록, 주문목록
-- 부 관리자 화면 - 상품목록, 주문목록 


-- 뷰의 생성과 삭제
/*
DROP VIEW IF EXISTS 뷰이름;
CREATE VIEW 뷰이름
AS
   SELECT 구문
*/

-- 뷰 호출
-- 테이블처럼 호출
-- 뷰를 테이블이라고 생각해도 무방
/*
SELECT * FROM 뷰이름;
*/


USE sqldb;
-- buyTbl, userTbl  뷰 생성하기 

SELECT * FROM buyTbl;
-- num, userID, price, amount => v_buyTbl  뷰 생성 
CREATE VIEW v_buyTbl
   AS SELECT num, userID, price, amount FROM buyTbl;
-- 뷰의 레코드 확인     
SELECT * FROM v_buyTbl;   

-- 예제에 사용될 테이블 만들기 
-- userTbl = > userTbl_a
CREATE TABLE userTbl_a (
      SELECT * FROM userTbl
);
SHOW TABLES;
SELECT * FROM userTbl_a;
-- 필수 필드명 확인하기 userID, name, birthYear, addr
DESC userTbl_a;

-- userTbl_a 테이블에서 필수 항목으로 구성된 뷰 생성 
-- v_userTbl_a => userID, name, birthYear, addr
CREATE VIEW v_userTbl_a
   AS 
   SELECT userID, name, birthYear, addr 
      FROM userTbl_a;
      
SHOW FULL TABLES IN sqldb
   WHERE Table_type = 'VIEW';
   
-- 뷰를 이용한 레코드 데이타 삽입
-- 주의 사항 : 뷰에서 등록한 컬럼의 데이타만 삽입 가능
-- INSERT INTO 뷰이름 (컬럼명1, 컬럼명2 ... ) 
--          VALUES (값1, 값2 ... );
-- INSERT INTO 뷰이름 VALUES (값1, 값2 ... );

INSERT INTO v_userTbl_a (userID, name, birthYear, addr) VALUES ('KJK', '김종국', 1977, '안양');
SELECT * FROM v_userTbl_a;
SELECT * FROM userTbl_a;

INSERT INTO v_userTbl_a VALUES ('KKD', '고길동', 1960, '제주');
SELECT * FROM v_userTbl_a;
SELECT * FROM userTbl_a;


-- 전남 => 남원 
UPDATE v_userTbl_a 
      SET addr = '남원' 
        WHERE  addr = '전남'; 
SELECT * FROM v_userTbl_a;
SELECT * FROM userTbl_a;



