-- 한줄 주석

/* 
여러줄 
주석
*/

-- < 데이타베이스 사용하기 >
-- USE 데이타베이스명;
USE worlddb;

-- 현재 어떤 DB가 있는지 보기
-- SHOW 데이타베이스명;
show databases;


-- 테이블 정보 조회
SHOW TABLE STATUS;

-- 테이블 이름만 간단히 보기
SHOW TABLES; 

-- 테이블 구조 확인하기 
-- DESCRIBE(DESC) 테이블명;
DESCRIBE city;
DESC country;

-- 테이블 레코드 표시하기 : SELECT
-- SELECT * FROM 데이타베이스명.테이블명;
-- SELECT * FROM 테이블명;

-- titles 테이블의 모든 레코드 확인하기 
USE employees;
SELECT * FROM titles;
-- employees 테이블의 모든 레코드 확인하기 
SELECT * FROM employees;
-- employees 테이블의 모든 레코드 확인하기 
SELECT * FROM dept_emp;
SELECT * FROM employees.dept_emp;

SELECT * FROM 데이타베이스명.테이블명;
-- employees 접속상태인데 잠시 worlddb 데이타베이스의 city 테이블 확인 
USE employees;
SELECT * FROM worlddb.city;

-- 특정 테이블의 특정 컬럼만 출력하기 
-- SELECT 컬럼명1, 컬럼명2, ... FROM 테이블명; 
USE employees;
DESC employees; -- employees 테이블의 구조 확인하기 
-- employees 테이블에서 emp_no, first_name, last_name 필드만 출력 
SELECT * FROM employees;
SELECT emp_no, first_name, last_name FROM employees;

-- 실습 -------------------------------------------------------- 
drop database if exists sqldb;
create database sqldb;
use sqldb;

-- 회원 테이블
CREATE TABLE userTbl 
( userID     CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name       VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr        CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1   CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2   CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height       SMALLINT,  -- 키
  mDate       DATE  -- 회원 가입일
);
SHOW tables;

-- 회원 구매 테이블
CREATE TABLE buyTbl 
(  num       INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID     CHAR(8) NOT NULL, -- 아이디(FK)
   prodName    CHAR(6) NOT NULL, --  물품명
   groupName    CHAR(4)  , -- 분류
   price        INT  NOT NULL, -- 단가
   amount       SMALLINT  NOT NULL, -- 수량
-- usrTbl의 userID를 참조. 외래키로 정의 
   FOREIGN KEY (userID) REFERENCES userTbl(userID)
);
SHOW tables;
DESC buytbl;
SELECT * FROM buytbl; 

desc userTbl;
INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

SELECT * FROM usertbl;
-- 테이블의 레코드수 확인하기 
-- SELECT count(*) FROM 테이블명;
SELECT count(*) FROM usertbl;


INSERT INTO buyTbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
SELECT * FROM buyTbl;
SELECT count(*) FROM buyTbl;  



