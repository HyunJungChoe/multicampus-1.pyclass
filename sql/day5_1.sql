-- INNER JOIN 을 뷰로 등록
USE sqldb;
SHOW TABLES;

-- buyTbl + userTbl 
SELECT * FROM buyTbl;
SELECT * FROM userTbl;

SELECT * 
	FROM buyTbl B 
    INNER JOIN userTbl U
    ON B.userID = U.userID;
    
SELECT B.*, name, addr 
	FROM buyTbl B 
    INNER JOIN userTbl U
    ON B.userID = U.userID;

-- 조인한 결과를 뷰로 등록 
CREATE VIEW v_buyUser
	AS
	SELECT B.*, name, addr 
	FROM buyTbl B 
    INNER JOIN userTbl U
    ON B.userID = U.userID;

SELECT * FROM v_buyUser;
SHOW FULL TABLES IN sqldb;
SHOW FULL TABLES IN sqldb WHERE Table_type='VIEW';

SELECT * FROM v_buyUser WHERE addr='서울';
SELECT userID, count(userID) FROM v_buyUser GROUP BY userID;


-- 퀴즈1 : SELF JOIN을 뷰로 등록하여 활용하기
-- empTbl 테이블을 이용해서 
-- 사원명, 사원구내번호, 직속상관, 직속상관 구내번호가 표시되도록 뷰를 등록하여라 
-- v_empTbl

SELECT * FROM empTbl;
SELECT * 
	FROM empTBL A
    INNER JOIN empTBL B
    ON A.manager = B.emp;
    
CREATE VIEW v_empTbl
	AS	
		SELECT 
			A.emp AS '사원명',
			A.empTel AS '사원구내번호',
			A.manager AS '상관',
			B.empTel AS '상관구내번호'
			FROM empTBL A
			INNER JOIN empTBL B
			ON A.manager = B.emp;
    
SELECT * FROM v_empTbl;  

 
-- 퀴즈2 : v_empTbl를 이용해서 '우대리'의 직속상관명과 직속상관의 구내번호를 
-- 출력하여 보세요 

SELECT * FROM v_empTbl WHERE 사원명='우대리';  
SELECT 상관, 상관구내번호 FROM v_empTbl WHERE 사원명='우대리';  






