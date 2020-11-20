USE sqldb;
SHOW TABLES;
DESCRIBE buytbl;
DESCRIBE usertbl;

-- GROUP BY
-- 그룹을 묶어주는 역할. 집계함수와 함께 사용 
-- SELECT .. FROM 테이블명 GROUP BY 컬럼명;

-- 합계 구하기 SUM(컬럼명)
-- 평균 구하기 AVG(컬럼명)
SELECT * FROM buytbl;

-- buytbl 테이블에서 price의 전체 합계와 평균구하기 
SELECT userID ,SUM(price) as '합계', AVG(price) as '평균' FROM buytbl GROUP BY userID;

-- 각 userID별로 구매한 개수를 합쳐서 출력 
SELECT userID, SUM(amount) FROM buytbl GROUP BY userID;
-- 별칭을 사용하여 보기 편하게 하기 
SELECT userID, SUM(amount) AS '총 구매 개수'FROM buytbl GROUP BY userID;

-- SELECT .. FROM 테이블명 GROUP BY 컬럼명 ORDER BY 컬럼명 ASC/DESC LIMIT 숫자1, 숫자2;
-- 각 종목(groupName)의 가격 합계, 평균를 groupName을 기준으로 정렬하여 표시하기 

-- groupName 필드의 값 확인 
SELECT DISTINCT groupName FROM buytbl;

SELECT groupName, SUM(price) , AVG(price) FROM buytbl
      GROUP BY groupName;

        
SELECT groupName, SUM(price) , AVG(price) FROM buytbl
      GROUP BY groupName ORDER BY groupName;        

SELECT groupName, SUM(price) , AVG(price) FROM buytbl
      GROUP BY groupName ORDER BY groupName DESC;        

-- AS 별칭이름;
-- 컬럼명을 대신하는 별칭 이름 표시
-- SELECT 컬럼명 AS 별칭명 FROM 테이블명;
-- 아이디(userID), 상품명(prodName), 가격(price) 별칭으로 출력하기 
SELECT * FROM buyTbl;
SELECT userID AS '아이디', prodName AS '상품명', price AS '가격' FROM buyTbl LIMIT 5;

-- buytbl 테이블에서 각 사용자별로 물건을 몇개 사는지 평균 구하기 
-- GROUP BY, AVG() 
SELECT * FROM buytbl;
SELECT userId AS '회원 아이디', AVG(amount) '평균구매횟수' 
            FROM buyTbl 
                GROUP BY userId
                ORDER BY AVG(amount) DESC; 
                
-- 가장 큰 키와 작은 키를 출력하는 쿼리 
SELECT name, height
	FROM usertbl 
	WHERE height = (SELECT MAX(height) FROM usertbl)
    OR height = (SELECT  MIN(height) FROM usertbl);
    
    
-- WHERE와 비슷하게 조건 제한. 
-- 주로 집계함수에 대해서 조건을 제한할때 사용 
-- 순서 주의 
-- SELECT .. FROM 테이블명 
-- GROUP BY 컬럼명 HAVING 조건 
-- ORDER BY 컬럼명 LIMIT 숫자;

-- buyTbl 테이블에서 총구매액이 
-- 1000 이상 조건으로 사용자(userID)별 총 구매액 표시 
-- GROUP BY 기준 : 사용자(userID)
-- 구매액 : SUM(price*amount) 

-- 에러 발생 . group by 절에서 where 절을 사용할 수 없다. 
/*
SELECT userId AS '회원 아이디', SUM(price*amount) '총구매액' 
            FROM buyTbl 
                WHERE  SUM(price*amount) >= 1000
                GROUP BY userId; 
*/

-- HAVING 절 이용 
SELECT userId AS '회원 아이디', SUM(price*amount) '총구매액' 
            FROM buyTbl 
                GROUP BY userId
                HAVING  SUM(price*amount) >= 1000
                ORDER BY SUM(price*amount); 

--  WITH ROLLUP
--  중간 합계 
-- 순서 주의 
-- SELECT .. FROM 테이블명 
-- GROUP BY 컬럼명 HAVING 조건 
-- WITH ROLLUP
-- ORDER BY 컬럼명 LIMIT 숫자;

-- buytbl 테이블에서 종목(groupName) 별로 구매액 SUM(price*amount)  및 총합 구하기 

-- 그룹바이 기준이 종목(groupName)
SELECT num, groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName;

-- 그룹바이 기준이 종목(groupName), 주문번호(num)
SELECT num, groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName, num;

-- WITH ROLLUP 이용 
-- 종목별 합계가 함께 표시 : NULL 행 삽입 
-- 그룹바이 기준이 종목(groupName), 주문번호(num)
-- 맨 하단 NULL, NULL 행은 총합 
SELECT num, groupName AS '종목', SUM(price*amount) AS '비용'
   FROM buytbl 
    GROUP BY groupName, num
    WITH ROLLUP;


SELECT groupName AS '종목', SUM(price*amount) AS '구매액'
   FROM buytbl 
    GROUP BY groupName
    WITH ROLLUP;
    
-- CRUD 명령어 
-- DML(Data Manupulation Language)

-- 기존 테이블 복사해서 새로운 테이블 만들기 
-- 기본 테이블의 데이타도 함께 복사 
-- CREATE TABLE 새테이블명 (SELECT */컬럼명 FROM 테이블명);
use sqldb;
CREATE TABLE buyTbl2 
      (SELECT * FROM buyTbl);
SELECT COUNT(*) FROM  buyTbl2;       

-- 레코드 삽입 1
-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2... ) VALUES(값1, 값2 .. )
-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
DESC buyTbl;

-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
INSERT INTO buyTbl2 VALUE (13, 'TTT', '손난로', '디지털', 20000, 3);

-- buyTbl3 테이블 생성 후 buyTbl 테이블에서 '전자' groupName 레코드 삽입하기 
-- buyTbl3 테이블 생성
CREATE TABLE buyTbl3 
(  num       INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID     CHAR(8) NOT NULL, -- 아이디(FK)
   prodName    CHAR(6) NOT NULL, --  물품명
   groupName    CHAR(4)  , -- 분류
   price        INT  NOT NULL, -- 단가
   amount       SMALLINT  NOT NULL -- 수량
);

SHOW TABLES;
SELECT COUNT(*) FROM buytbl3;
-- buyTbl 테이블에서 groupName이 '전자'인 레코드 삽입하기 
SELECT * FROM buyTbl WHERE groupName = '전자';

-- INSERT INTO 테이블명 (컬럼명1, 컬러명2 ... ) SELECT 문 
INSERT INTO buytbl3 (userID, prodName, groupName, price, amount)
      SELECT userID, prodName, groupName, price, amount FROM buyTbl 
            WHERE groupName = '전자';   

SELECT COUNT(*) FROM buytbl3;    
SELECT * FROM buytbl3; 

-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
USE sqldb;
CREATE TABLE testTbl (id int, name char(3), age int);
INSERT INTO testTbl VALUE (1, '홍길동', 25);
SELECT * FROM testTbl; 

-- 나이를 빼고 입력하고 싶을 때 
INSERT INTO testTbl(id, name) VALUE (1, '홍길동');

-- 대량의 데이터 입력 할 때 
INSERT INTO testTbl(id, name) VALUE (1, '홍길동'), (2,'이순신');

-- 레코드 수정과 삭제  
-- UPDATE 테이블명 SET 컬럼명=값 WHERE 절;
SELECT * FROM buytbl3; 

-- 수정이 적용되게 MySQL 환경 설정하기 
-- [Edit]-[Preferences] 클릭 후 
-- SQL Editor 클릭후 맨 아래 Safe ~ 선택을 해제한다. 
-- 워크벤치 재실행 

-- buytbl3 테이블에서 상품명이 노트북인 레코드의 수량을 10으로 수정하여라. 
USE sqlDB;
UPDATE buytbl3 SET amount=10 WHERE prodName='노트북';
SELECT * FROM buytbl3; 

-- buytbl3 테이블에서 종목 값을 모두 디지털로 수정하여라 
UPDATE buytbl3 SET groupName = '디지털';
SELECT * FROM buytbl3; 

USE sqlDB;
UPDATE buytbl SET price = price*1.5;


-- 테이블 삭제 
-- DROP TABLE 테이블명;
-- 테이블 구조 제외 레코드만 삭제 
-- TRUNCATE TABLE 테이블명;

-- buyTbl을 이용해 3개의 테이블 생성 
CREATE TABLE IF NOT EXISTS buytbl_a
   (SELECT userID, prodName, price FROM buytbl);
CREATE TABLE IF NOT EXISTS buytbl_b
   (SELECT userID, prodName, price FROM buyTbl);   
CREATE TABLE IF NOT EXISTS buytbl_c
   (SELECT userID, prodName, price FROM buyTbl);   

-- WHERE절이 없는 DELETE FROM 명령 실행 => 모든레코드 삭제 

SELECT * FROM buytbl_a;
DELETE FROM buytbl_a;


USE sqlDB;
UPDATE buytbl_a SET price = price*1.5;
DELETE FROM buytbl_a WHERE userID = 'BBK';

-- 변수 생성과 출력 
-- SET @변수명 = 초기값;
-- SELECT @변수명;

USE sqldb;
SET @a = 5;
SET @b = 3.14;
SET @c = 'Hello MYSQL';
SELECT @a, @b, @c;
SELECT @a, @b, @a+@b AS '더한 값', @a*@b AS '곱합 값';

-- CAST ( .. AS 데이터형식)
-- CONVERT ( .. , 데이터형식)
-- 데이터형식 :
--  BINARY, CHAR(), DATE , TIME, 
--  SIGNED INTEGER, UNSIGNED INTEGER
-- amount 평균 구매횟수 => 정수
SELECT CONVERT(AVG(amount), SIGNED INTEGER) FROM buyTbl;
SELECT CAST(AVG(amount) AS SIGNED INTEGER) FROM buyTbl;

-- 실수형숫자 => 문자 
-- 숫자문자 => 양의 정수 
SELECT CAST(3.14 AS CHAR(10)), CAST('23Python5667' AS SIGNED INTEGER); 
SELECT CONVERT(3.14 , CHAR(10)), CONVERT('23Python5667' , SIGNED INTEGER); 

-- 제어흐름함수 
-- IF(조건식, 값1, 값2)
-- 조건식이 True 이면 값1, False 이면 값2 반환 

SELECT IF(100<500, '크다', '작다');
 IF(100>500, '크다', '작다');

SELECT IFNULL(NULL, '널값이다'), IFNULL(500, '널값이다');

-- buytbl 테이블에서 groupName 컬럼값이 NULL 이면 '준비중..'으로 표시하여라 
SELECT * FROM buyTbl; 
SELECT prodName AS '상품명',
      IFNULL(groupName, '준비중..') AS '종목', 
        price AS '가격' 
        FROM buyTbl;
        
-- 다중분기 
-- CASE 값1 
--     WHEN 값2 THEN 결과값1 
--     WHEN 값3 THEN 결과값2
--     ELSE 결과값n 
--     END;

SET @age = 11;
SELECT CASE @age 
      WHEN 1 THEN '일' 
      WHEN 10 THEN '십'
      ELSE '...모름'
      END AS 'RESULT';

/* CONCAT()이용해서 하나의 컬럼에 2개의 컬럼값 표시  */
-- 단가  X  수량 = 입금액 
SELECT * FROM buyTbl;
SELECT prodName, price, amount, price*amount 
      FROM buyTbl LIMIT 3;

-- CONCAT()이용해서 하나의 컬럼에 2개의 컬럼값 표시         
SELECT prodName, 
      concat(price,' X', amount, ' = ', price*amount ) AS '가격*수량'
      FROM buyTbl LIMIT 3;

SELECT CONCAT_WS('/','2025','01','10');

/* 퀴즈 - CONCAT() 활용 
 usertbl 테이블에서 키가 175 넘는 레코드만 추출한 후 아래와 같은 형태로 출력하여라.  
        이름          키   
 가수이름 => 김경호   ?  cm
 가수이름 => 이승기   ?  cm 
 
 */      
SELECT CONCAT('가수이름 => ',name) AS '이름', 
	CONCAT(height,' cm') AS '키' 
    FROM usertbl 
    WHERE height > 175;
    
SELECT
   CONCAT("가수이름 => ", name) AS "이름", 
   CONCAT(height, "cm") AS "키" 
   FROM usertbl 
   WHERE height > 175;
   
   
-- 소숫점 자리 표시         
-- FORMAT(숫자, 소숫점 자릿수)    
SELECT FORMAT(123.456789, 2);
-- 123.46

SET @X = 123.456789;
SELECT @X, FORMAT(@X, 1), FORMAT(@X, 3);

-- 각 종목의 평균 가격을 groupName을 기준으로 정렬하여 표시하기 
SELECT    groupName AS '종목', 
      FORMAT(AVG(price),2) AS '평균 가격' 
         FROM buytbl 
         GROUP BY groupName ORDER BY groupName;

SELECT INSERT('010-1234-5678', 5, 4, '****') AS 'result';
 
SELECT REPLACE('010-1234-5678', 1234, '****') AS 'result';
