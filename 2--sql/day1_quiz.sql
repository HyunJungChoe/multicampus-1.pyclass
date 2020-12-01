--  퀴즈 - 
USE sqldb;

-- 1) buyTbl 테이블의 구조 확인하기 


-- 2) buyTbl 테이블에서 userID, prodName 컬럼만 출력하기 
 
-- 3) buyTbl 테이블에서 userID가 'KBS'인 레코드 출력하기 

-- 4) buyTbl 테이블에서 prodName 컬럼을 중복없이 출력하기 
SELECT prodName From buytbl;
SELECT DISTINCT prodName From buytbl;
-- 갯수 확인 
SELECT COUNT(DISTINCT prodName) From buytbl;

-- 5) buyTbl 테이블에서 groupName이 NULL인 레코드 출력하기 (IS NULL 이용)
DESC buyTbl;
SELECT groupName From buyTbl;
-- NULL은 비교연산자 사용불가 
-- WHERE 필드명 IS NULL  이용 
SELECT COUNT(*) From buyTbl WHERE groupName = NULL; -- 0

SELECT COUNT(*) From buyTbl WHERE groupName IS NULL; -- 3
SELECT * From buyTbl WHERE groupName IS NULL; 



-- 6) buyTbl 테이블에서 amount가 5보다 큰 레코드 출력하기 

-- 7) buyTbl 테이블에서 prodName 컬럼이 '청바지' 이거나 '운동화'인 레코드 출력구문을 2가지로 방법으로 작성하기 
-- (OR, IN 사용)

-- 8) buyTbl 테이블에서 price 컬럼값이 30~80인 레코드 출력구문을 2가지 방법으로 작성하기 
-- (AND 구문, BETWEEN .. AND 구문 이용)


-- 9) buyTbl 테이블에서 userID에 'K'로 시작하는 레코드 출력하기 (LIKE 이용)
SELECT * FROM buytbl;
SELECT * FROM buytbl WHERE userID LIKE 'K%';
SELECT * FROM buytbl WHERE userID LIKE 'K__';

-- 10) buyTbl 테이블에서 prodName이 ??화로 끝나는 레코드 출력하기 (LIKE 이용)
SELECT * FROM buytbl WHERE prodName LIKE '__화';


-- 11) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 price 컬럼값 보다 큰 레코드 출력하기
-- (서브쿼리 이용)
select price from buytbl where userID = 'JYP';

SELECT * FROM buytbl WHERE price > ( select 
                              price from buytbl 
                                    where userID = 'JYP'
                           );
    
-- 12) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 amount 컬럼값과 같은 레코드 출력하기 
-- (서브쿼리 이용)
select * from buytbl where amount = (
                     select amount from buytbl where userID = 'JYP'
                           );


-- 13) buyTbl 테이블에서 price 컬럼값이 큰 순서대로 5개만 출력하기 
-- (ORDER BY, LIMIT) 이용
select * from buytbl order by price desc limit 5;

-- 14) buyTbl 테이블에서 userID 컬럼값이 'KBS'인 레코드 목록 중 price 컬럼값이 
--  가장 작은 레코드 출력하기 
-- (WHERE, ORDER BY, LIMIT) 이용

select * from buytbl where userID = 'KBS' 
      order by price limit 1;


-- 15) userTbl 테이블에서 addr 컬럼값이 '서울'인 레코드만 복사해서 새로운 테이블 userTbl1 생성하기 
-- (CREATE TABLE ~) 이용
create table userTbl1 (
                  select * from usertbl where addr = '서울'
                  );
show tables;

-- 16) userTbl 테이블에서 name 컬럼값이 '은지원'인 레코드의 height 컬럼값보다 
--  큰 레코드만 height 값을 기준으로 정렬하여 복사해서 새로운 테이블 userTbl2 생성하기. 
-- (CREATE TABLE ~) 이용

select height from usertbl where name = '은지원';

select * from usertbl where height > (
            select height from usertbl where name = '은지원')
                order by height;

CREATE TABLE usertbl2  (
                  select * from usertbl where height > (
                        select height from usertbl where name = '은지원')
                     order by height);               

show tables;
SELECT * FROM usertbl2;
