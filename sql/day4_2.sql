-- 외부조인 (OUTER JOIN)
-- 조인의 조건에 만족되지 않는 행까지도 포함시킨다. 

-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      <LEFT/RIGHT/FULL> OUTER JOIN 테이블2
--         ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명 이용 
--            (서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

USE sqldb;
-- buytbl + usertbl 이너조인예 
-- 이너조인은 공통 필드(userID)를 제외한 나머지 레코드를 표시가 되지 않는다. 

SELECT * FROM buytbl;
SELECT * FROM usertbl;
SELECT userID FROM usertbl;
-- userTbl 테이블에서 구매경력이 있는 회원은? 5
SELECT count(userID) FROM usertbl; -- 10 
SELECT count(DISTINCT userID) FROM buytbl; -- 5
-- 이너조인의 경우 : userTbl에서 구매경력이 없는 회원의 레코드는 표시되지 않는다. 
SELECT * 
   FROM buytbl B
    INNER JOIN userTbl U
    ON B.userID = U.userID
    ORDER BY B.userID;


-- LEFT OUTER JOIN
-- 전체회원의 구매기록 확인하기.
-- 구매기록이 없는 회원도 모두 출력되어야 한다.
-- 왼쪽에 정의된 테이블 userTbl의 레코드가 모두 표시되어야한다. 
-- 구매경력이 없는 회원 레코드도 모두 출력 

SELECT * 
   FROM userTbl U
    LEFT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY B.userID;

-- 17 .. 12+5 
SELECT count(*)
   FROM userTbl U
    LEFT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY U.userID;

-- buyTbl에 userID가 없는 레코드만 표시 
-- 구매경력이 없는 레코드 
-- 이너조인시 출력되지 않는 레코드 
SELECT * 
   FROM userTbl U
    LEFT OUTER JOIN buytbl B
    ON U.userID = B.userID
   WHERE B.userID IS NULL
    ORDER BY U.userID;


-- RIGHT OUTER JOIN
-- 오른쪽에 해당하는 테이블의 레코드가 모두 표시된다. 

SELECT * 
   FROM userTbl U
    RIGHT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY B.userID;

SELECT count(*) -- 12
   FROM userTbl U
    RIGHT OUTER JOIN buytbl B
    ON U.userID = B.userID
    ORDER BY B.userID;

-- RIGHT 테이블은 userTbl
SELECT * 
   FROM buytbl B
    RIGHT OUTER JOIN userTbl U
    ON B.userID = U.userID
    ORDER BY B.userID;
    
    
SELECT count(*)
   FROM buytbl B
    RIGHT OUTER JOIN userTbl U
    ON B.userID = U.userID
    ORDER BY B.userID;

-- FULL OUTER JOIN
-- 왼쪽과 오른쪽에 해당하는 테이블의 레코드가 모두 표시된다. 
  
  
-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 학생을 기준으로 동아리 학생 목록을 LEFT OUTER JOIN을 이용하여 출력하여라. 
-- 이때 동아리에 가입하지 않은 학생 목록도 출력한다.
USE sqldb;
SHOW TABLES;

-- stdTbl : stdName, addr
SELECT * FROM stdTbl; 
-- clubtbl : clubName, roomNo
SELECT * FROM clubtbl; 
-- stdclubtbl : num, stdName, clubName
SELECT * FROM stdclubtbl; 

-- stdTbl + stdclubTbl + clubTbl 3개 테이블 이너 조인 
-- 전체 필드 
SELECT  * 
    FROM stdTbl S
   INNER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName
    INNER JOIN  clubTbl C
      ON SC.clubName = C.clubName;  

-- stdTbl + stdclubTbl
-- 이너조인 : 동아리에 가입한 학생 
SELECT  * 
    FROM stdTbl S
   INNER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName;  
        
SELECT count(*) -- 6 
    FROM stdTbl S
   INNER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName;     
        

-- 아우터 조인 : stdTbl        
-- 동아리에 가입하지 않은 학생 목록도 출력한다. 
SELECT  * 
    FROM stdTbl S
   LEFT OUTER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName;  

SELECT count(*) -- 7
    FROM stdTbl S
   LEFT OUTER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName;  

-- 동아리에 가입하지 않은 학생 레코드만 출력하여라
SELECT  * 
    FROM stdTbl S
   LEFT OUTER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName
        WHERE SC.stdName IS NULL;  


-- stdTbl + stdclubTbl + clubTbl 
-- 학생테이블(stdTbl)을 기준으로 아우터 조인 
SELECT  * 
    FROM stdTbl S
   LEFT OUTER JOIN  stdclubTbl SC
      ON S.stdName = SC.stdName
    LEFT OUTER JOIN  clubTbl C
      ON SC.clubName = C.clubName;  

SELECT  
   S.stdName AS '학생이름',  
    addr AS '지역',
    SC.clubName AS '동아리명',
    roomNo AS '동아리방번호'
      FROM stdTbl S
      LEFT OUTER JOIN  stdclubTbl SC
         ON S.stdName = SC.stdName
      LEFT OUTER JOIN  clubTbl C
         ON SC.clubName = C.clubName;  

-- 퀴즈 : stdTbl, clubtbl, stdclubtbl 테이블에서
-- 동아리를 기준으로 가입한 학생 목록을 OUTER JOIN을 이용하여 출력하여라.
-- 이때 가입학생이 아무도 없는 동아리 목록도 출력한다.
-- 동아리명  동아리번호  학생이름  지역 
--   ?       ?       ?     ?

-- clubTbl + stdclubTbl 아우터조인 
SELECT  *
      FROM clubTbl C
      LEFT OUTER JOIN  stdclubTbl SC
         ON SC.clubName = C.clubName;

SELECT  count(*) -- 7
      FROM clubTbl C
      LEFT OUTER JOIN  stdclubTbl SC
         ON SC.clubName = C.clubName;

-- 3개의 테이블을 아우터 조인             
SELECT  *
      FROM clubTbl C
      LEFT OUTER JOIN  stdclubTbl SC
         ON SC.clubName = C.clubName            
      LEFT OUTER JOIN  stdTbl S
         ON S.stdName = SC.stdName;

-- 3개의 테이블을 아우터 조인             
SELECT 
   C.clubName AS '동아리명', 
   C.roomNo AS '동아리방', 
   S.stdName AS '학생 이름', 
   S.addr AS '지역'
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        RIGHT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName
      ORDER BY C.clubName;            

-- 전체 아우터 조인 : FULL OUTER JOIN 
-- UNION 명령을 이용해서 조인한 모든 레코드 출력하기 
-- 동아리에 가입하지 않은 학생 
-- 학생이 한명도 없는 동아리 이름
/*
SELECT 조인 명령1 
   UNION
SELECT 조인 명령2; 
*/


SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
   C.clubName AS '동아리명', C.roomNo AS '동아리방'
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        LEFT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName 
UNION
SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
    C.clubName AS '동아리명', C.roomNo AS '동아리방' 
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        RIGHT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName;
            
 -- stdTbl 학생 테이블 기준 3개의 테이블 조인 
 SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
   C.clubName AS '동아리명', C.roomNo AS '동아리방'
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        LEFT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName; 
 
 -- clubtbl 모든 레코드 
 SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
    C.clubName AS '동아리명', C.roomNo AS '동아리방' 
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        RIGHT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName;
 
-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 학생을 기준으로 동아리 학생 목록을 OUTER JOIN을 이용하여 출력하여라. 
-- 이때 동아리에 가입하지 않은 학생 목록과 가입학생이 없는 동아리 목록도 함께 출력한다.
-- UNION 활용. SELECT 문에 컬럼명이 같아야 한다. 
 
 SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
   C.clubName AS '동아리명', C.roomNo AS '동아리방'
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        LEFT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName 
UNION
SELECT 
   S.stdName AS '이름', S.addr AS '지역', 
    C.clubName AS '동아리명', C.roomNo AS '동아리방' 
   FROM stdTbl S
      LEFT OUTER JOIN stdclubtbl SC
         ON S.stdName = SC.stdName
        RIGHT OUTER JOIN clubtbl C
         ON SC.clubName = C.clubName;
 
 
 -- 크로스 조인 (상호조인) 
-- 모든행이 반복됨 
-- 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행이 조인됨 => 카티션곱
-- SELECT * 또는 컬럼명
--    FROM 테이블1 
--      CROSS JOIN 테이블2;

-- buyTbl, userTbl 테이블에서 CROSS JOIN을 적용하여라. 
USE sqldb;
SELECT * FROM buyTbl;  -- 12
SELECT * FROM userTbl; -- 10 

SELECT * FROM buyTbl
   CROSS JOIN userTbl;
    
SELECT count(*) FROM buyTbl
   CROSS JOIN userTbl;  
   
-- sqlDB 안에 empTBL 테이블 생성 
USE sqlDB;

DROP TABLE IF EXISTS empTbl;
CREATE TABLE empTbl 
   (emp CHAR(4), manager CHAR(4), empTel VARCHAR(8));

INSERT INTO empTbl VALUES('나사장',NULL,'0000');
INSERT INTO empTbl VALUES('김재무','나사장','2222');
INSERT INTO empTbl VALUES('김부장','김재무','2222-1');
INSERT INTO empTbl VALUES('이부장','김재무','2222-2');
INSERT INTO empTbl VALUES('우대리','이부장','2222-2-1');
INSERT INTO empTbl VALUES('지사원','이부장','2222-2-2');
INSERT INTO empTbl VALUES('이영업','나사장','1111');
INSERT INTO empTbl VALUES('한과장','이영업','1111-1');
INSERT INTO empTbl VALUES('최정보','나사장','3333');
INSERT INTO empTbl VALUES('윤차장','최정보','3333-1');
INSERT INTO empTbl VALUES('이주임','윤차장','3333-1-1');

SELECT * FROM empTBL;
SELECT COUNT(*) FROM empTBL;

-- 셀프조인 
SELECT * FROM empTBL;

SELECT * 
   FROM empTBL A
    INNER JOIN empTBL B
    ON A.manager = B.emp;
    
SELECT 
   A.emp AS '사원명',
    A.manager AS '상관명',
    A.empTel AS '사원구내번호',
    B.manager AS '상관의 상관명',
    B.empTel AS '상관구내번호'
   FROM empTBL A
    INNER JOIN empTBL B
    ON A.manager = B.emp;
    
 SELECT A.emp AS '부하직원', B.emp AS '직속상관', B.empTel AS '직속상관 연락처'
   FROM empTBL A
    INNER JOIN empTBL B
    ON A.manager = B.emp
    WHERE A.emp = '우대리';

-- UNION / UNION ALL 
-- 쿼리의 결과를 합쳐서 보여준다. 


-- SELECT ... -- 쿼리1
-- UNION / UNION ALL
-- SELECT ... -- 쿼리2


SELECT * FROM clubtbl; -- 동아리정보 
SELECT * FROM stdtbl; -- 학생정보 
    
-- 동아리 이름     
SELECT clubName FROM clubtbl;
-- 학생 이름     
SELECT stdName FROM stdtbl;  

-- 동아리 이름     

SELECT clubName AS '결과' FROM clubtbl 
UNION
SELECT clubName FROM stdclubTbl; 


-- NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외 
-- IN : 두번째 쿼리의 결과만 조회 

-- SELECT 첫번째 쿼리 
--   WHERE ... [NOT IN / IN ] ( SELECT 두번째 쿼리 )

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 사용자중 전화가 없는 사람을 제외하고 싶다. NOT IN
-- 사용자중 전화가 없는 사람만 조회 IN

-- 전화가 없는 사람 제외 : NOT IN => 전화기가 있는 사람만 표시 

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl;

-- 전화가 없는 사람을 출력하여라 
SELECT name FROM userTbl 
    WHERE mobile1 IS NULL;

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 전화기가 있는 사람. 메인쿼리결과 - 서브쿼리결과 
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl
   WHERE name NOT IN
      (SELECT name FROM userTbl WHERE mobile1 IS NULL);

-- 전화기가 없는 사람. 메인쿼리결과와 서브쿼리결과의 교집합 
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl
   WHERE name IN
      (SELECT name FROM userTbl WHERE mobile1 IS NULL);
