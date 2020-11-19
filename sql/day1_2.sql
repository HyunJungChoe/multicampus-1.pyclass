
USE sqldb;

-- WHERE
-- 특정한 조건을 줘서 원하는 데이터만 보고 싶을 때 사용 한다.

SELECT * FROM usertbl WHERE name='김경호';

-- SELECT 컬러명1, 컬럼명2.. 또는 * FROM 테이블명 WHERE 조건절
-- 조건절 : 비교연산자 (>, <, <=, >=, =)

-- userTbl 테이블에서 name이 은지원인 레코드 보기 
SELECT * FROM userTbl WHERE name = '은지원';

-- userTbl 테이블에서 키(height)가 182 이상인 레코드 출력하기 
SELECT * FROM userTbl WHERE height >= 182;
SELECT * FROM userTbl WHERE height >= 182 AND birthYear >= 1970;  -- AND 연산자 
SELECT * FROM userTbl WHERE height >= 182 OR birthYear >= 1970;    -- OR 연산자 
SELECT * FROM userTbl WHERE 190 > height ANd height >= 170;  
SELECT * FROM userTbl WHERE height BETWEEN 170 AND 180;  -- BETWEEN _ AND _

-- IN 연산자 특정값 만족 
-- WHERE 컬럼명 IN (값1, 값2 ...)
-- userTbl 테이블에서 addr 컬럼값이 경남, 전남, 경북인 레코드에서 Name, addr 컬럼만 출력하기 
DESC userTbl;
-- OR, = 연산자 이용 

SELECT name, addr FROM userTbl
WHERE addr = '경남' OR addr = '전남' OR addr = '경북';

-- IN 연산자 이용         
SELECT name, addr FROM userTbl
WHERE addr IN ('경남','전남','경북');        

SELECT name, addr FROM userTbl
WHERE name LIKE '_종신';  

-- 서브쿼리로 합치기 
SELECT name, height FROM userTbl      
WHERE height >= (
				SELECT height FROM userTbl
				WHERE name = '김경호'
                  );
                        
-- 아래는 에러 발생 : 서브쿼리의 결과값이 여러개라서 
-- SELECT name, height FROM userTbl      
--       WHERE height >= (
--                      SELECT height FROM userTbl
--                      WHERE name = '김경호' OR name = '이승기'
--                   );

-- '경남' 의 키는 173, 170 반환 됨.
SELECT name, height FROM userTbl      
WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남' );
-- 결국 키가 170 보다 크거나 같은 사람 해당된다. 

SELECT name, height FROM userTbl      
WHERE height >= ALL (SELECT height FROM userTbl WHERE addr = '경남' );
-- 결국 키가 173 보다 크거나 같은 사람 해당된다. 

-- 정렬, 역정렬 
-- 결과가 출력되는 순서를 조절하는 구문 
-- 오름차순(ASCENDING) : ORDER BY 컬럼명
-- 내림차순(DESCENDING) : ORDER BY 컬럼명 DESC;
-- SELECT 필드명나열|* FROM 테이블명 
--                WHERE 조건절 
--                ORDER BY 컬럼명 (DESC)

-- mDate(가입일) 컬럼명 기준으로 레코드 정렬 
SELECT name, mDate FROM userTbl ORDER BY mdate;

-- mDate 컬럼명 기준으로 레코드 역정렬 
SELECT name, mDate FROM userTbl ORDER BY mdate DESC;


-- 정렬기준이 여러개인 경우          
-- SELECT 필드명나열|* FROM 테이블명 
--                WHERE 조건절 
--                ORDER BY 컬럼명1 (DESC|ASC), 컬럼명2 (DESC|ASC)
  
-- 2개의 컬럼명(height, name)으로 정렬. 키가 큰 순서로 정렬하되 
--   만약 키가 같다면 이름순으로 정렬             

-- 키는 오름차순, 이름은 내림차순  
SELECT * FROM userTbl ORDER BY height ASC, name DESC;

-- 고향(addr)은 내림차순, 이름은 오름차순
SELECT * FROM userTbl ORDER BY addr DESC, name ASC;


SELECT DISTINCT addr FROM usertbl;

-- LIMIT 시작인덱번호, 갯수 
USE employees;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 5;

SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 0,5;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 5 OFFSET 0;

-- 기존 테이블 복사해서 새로운 테이블 만들기 
-- 기본 테이블의 데이타도 함께 복사 
-- CREATE TABLE 새테이블명 (SELECT */컬럼명 FROM 테이블명);

-- userTbl 테이블에서 지역(addr)이 서울인 레코드만 
-- userTbl_seoul 테이블로 저장하여라 

-- 지역(addr)이 서울인 레코드
SELECT * FROM userTbl WHERE addr='서울';
CREATE TABLE userTbl_seoul (
                     SELECT * FROM userTbl WHERE addr='서울'
                        );
SHOW TABLES;
SELECT * FROM userTbl_seoul;

-- 5) buyTbl 테이블에서 groupName이 NULL인 레코드 출력하기 (IS NULL 이용)
DESC buyTbl;
SELECT groupName From buyTbl;
-- NULL은 비교연산자 사용불가 
-- WHERE 필드명 IS NULL  이용 
SELECT COUNT(*) From buyTbl WHERE groupName = NULL; -- 0

SELECT COUNT(*) From buyTbl WHERE groupName IS NULL; -- 3
SELECT * From buyTbl WHERE groupName IS NULL; 
