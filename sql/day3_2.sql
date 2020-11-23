
USE sqldb;
SELECT * FROM userTbl;
DESC userTbl;
SELECT * FROM buyTbl;
DESC buyTbl;

-- 조인이란? 
-- 2개이상 테이블에서 조건을 기준으로 출력하는 기능 

-- INNER JOIN 1 --
-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      INNER JOIN 테이블2
--         ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명 이용 
--            (서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

-- 이너조인 buyTbl + userTbl
-- 공통 필드(컬럼) 이 있는지 확인 : userId 

SELECT * 
   FROM buyTbl
     INNER JOIN userTbl
        ON buyTbl.userID = userTbl.userID
        ORDER BY buyTbl.userID;

-- 12
SELECT count(*) 
   FROM buyTbl
     INNER JOIN userTbl
        ON buyTbl.userID = userTbl.userID;        

-- 이너조인 userTbl + buyTbl
-- 공통 필드(컬럼) 이 있는지 확인 : userId     
USE sqldb;   
SELECT * 
   FROM userTbl
     INNER JOIN buyTbl
        ON userTbl.userID = buyTbl.userID
        ORDER BY userTbl.userID;
        
/* 퀴즈 
-- 아래와 같이 2개의 테이블(usertbl, buytbl)을 조인한 후  
-- 표시되게 만들어 보세요 

구매금액 = 수량*가격 

아이디       이름      지역       상품명       수량      가격   구매금액
   ?         ?      ?           ?         ?       ?        ?
 */

SELECT U.userID AS '아이디', U.name AS '이름', U.addr AS '지역',
 B.prodName AS '상품명',  B.amount AS '수량', B.price AS '가격',
 format(B.price * B.amount, 0) AS '구매금액' 
	FROM userTbl U
	INNER JOIN buyTbl B
	ON U.userId = B.userId;
    
    
    -- employees 데이타베이스에서 테이블 조인하기 
USE employees;
SHOW TABLES;
-- emp_no, birth_date, first_name, last_name, gender, hire_date
SELECT * FROM employees LIMIT 5; 

-- emp_no, dept_no(부서번호), from_date(부서근무시작일), 
-- to_date(부서근무마지막날짜) 9999-01-01 이면 현재근무중 
SELECT * FROM dept_emp LIMIT 5;

-- emp_no, title(부서명) , from_date(부서근무시작일), 
-- to_date(부서근무마지막날짜) 9999-01-01 이면 현재근무중 
SELECT * FROM titles LIMIT 5;

-- employees + dept_emp 테이블 조인하기 
SELECT * 
   FROM employees E
    INNER JOIN dept_emp D
    ON E.emp_no = D.emp_no
      LIMIT 10;
      
-- 퀴즈 - employees + titles 테이블 조인하기        
-- 사원번호, 이름, title(부서명), 성별, 입사일 
-- 사원이름이 'S'로 시작하는 레코드만 10개 출력
-- 정렬기준은 사원이름 

SELECT 
      E.emp_no AS '사원번호',
      concat(E.first_name, ' ', E.last_name) AS '이름',
        T.title AS '부서명',
      E.gender AS '성별',
      E.hire_date AS '입사일'        
   FROM employees E
   INNER JOIN titles T
   ON E.emp_no = T.emp_no 
      WHERE E.first_name like 'S%' 
      ORDER BY concat(E.first_name, ' ', E.last_name)
      LIMIT 10;

USE sqldb; 

-- 학생(stdTbl) 테이블 생성 - 이름:VARCHAR(10), 지역:CHAR(4) 
DROP TABLE IF EXISTS stdTbl;
CREATE TABLE stdTbl 
( stdName  VARCHAR(10) NOT NULL PRIMARY KEY,
  addr   CHAR(4) NOT NULL
);

DESC stdTbl;

-- 동아리(clubTbl) 테이블 생성
-- 동아리명(clubName):VARCHAR(10), 동아리방(roomNo):CHAR(4)
DROP TABLE IF EXISTS clubTbl;
CREATE TABLE clubTbl 
( clubName  VARCHAR(10) NOT NULL PRIMARY KEY,
  roomNo  CHAR(4) NOT NULL
);
DESC clubTbl;

-- 학생동아리(stdclubTbl) 테이블 생성 
-- num(num):int,  stdName(이름):VARCHAR(10), 
-- clubName(동아리명):VARCHAR(10) 
-- 외래키 2개 설정 
-- stdTbl(stdName), clubTbl(clubName)
-- FOREIGN KEY(컬럼명) REFERENCES 외부테이블명(컬럼명)

DROP TABLE IF EXISTS stdclubTbl;
CREATE TABLE stdclubTbl
(  num int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   stdName    VARCHAR(10) NOT NULL,
   clubName    VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubTbl(clubName)
);
DESC stdclubTbl;


-- stdTbl: 데이타 입력 후 테이블 확인 
-- 복수개의 레코드 삽입하기 
-- INSERT INTO 테이블명 VALUES (값1, 값2...), (값1, 값2...) ....;

INSERT INTO stdTbl 
   VALUES 
      ('김범수','경남'), 
        ('성시경','서울'), 
        ('조용필','경기'), 
        ('은지원','경북'),
        ('바비킴','서울');

SELECT * FROM stdTbl;  

-- clubTbl: 데이타 입력 후 테이블 확인 
INSERT INTO clubTbl 
   VALUES 
      ('수영','101호'), ('바둑','102호'), 
      ('축구','103호'), ('봉사','104호');

SELECT * FROM clubTbl; 

-- stdclubTbl: 데이타 입력 후 테이블 확인 
-- num 필드가 자동증감, 기본키 
INSERT INTO stdclubTbl 
   VALUES 
      (NULL, '김범수','바둑'), (NULL,'김범수','축구'), 
        (NULL,'조용필','축구'), (NULL,'은지원','축구'), 
        (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');
SELECT * FROM stdclubTbl; 
-- stdTbl + stdclubTbl
SELECT  * 
    FROM stdTbl S
   INNER JOIN  stdclubTbl SC
    ON S.stdName = SC.stdName;

-- clubTbl + stdclubTbl
SELECT  * 
    FROM stdclubTbl SC
   INNER JOIN  clubTbl C
    ON SC.clubName = C.clubName;
    -- stdTbl + stdclubTbl + clubTbl
SELECT  * 
    FROM stdTbl S
   INNER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName
    INNER JOIN  clubTbl C
      ON SC.clubName = C.clubName; 
