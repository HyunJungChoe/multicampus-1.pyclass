-- #########################
-- 데이타베이스 관련 명령어
-- DROP DATABASE  IF EXISTS 데이타베이스명;
-- CREATE DATABASE IF NOT EXISTS  데이타베이스명;
-- SHOW DATABASES; 모든 데이타베이스 표시 
-- USE 데이타베이스명; 데이타베이스 변경 

DROP DATABASE IF EXISTS tableDB;
CREATE DATABASE IF NOT EXISTS  tableDB;
SHOW DATABASES;
USE tableDB;

-- #########################
-- 테이블 생성과 삭제 관련 명령어
-- DROP/DELETE TABLE  <IF EXISTS> 테이블명; -- 테이블 삭제 

-- CREATE TABLE 테이블명 (필드명 자료형 옵션);
-- 옵션 : NULL/ NOT NULL / AUTO INCREMENT 
-- PRIMARY KEY / FOREIGN KEY(필드명) REFERENCES 테이블명(필드명)

-- SHOW TABLES; -- 테이블 목록 표시 
-- DESC 테이블명; -- 테이블 구조 표시 

SHOW TABLES;
-- CREATE TABLE 테이블명 (필드명 자료형 옵션);
-- 옵션 : NULL/ NOT NULL / AUTO INCREMENT (자동증감)
-- PRIMARY KEY / FOREIGN KEY(필드명) REFERENCES 테이블명(필드명)

-- MYSQL의 자료형 :
-- 숫자형 (정수, 실수...) smallint, int, float, decimal ... 
-- 문자형 char(n), varchar(n), binary(n), text, longtext,  blob...
-- 날짜형 ????-??-?? ??:??:?? date, time, datetime ...
-- 기타  lob, json ... 

-- 회원가입테이블 userTbl
-- 이름 userName -- char(5) not  null 
-- 아이디 userId -- char(8) not   null  PRIMARY KEY 
-- 연락처 mobile -- varchar(16)   not null 
-- 이메일 email -- varchar(20)    null
-- 생년월일 birth -- date          null 

CREATE TABLE IF NOT EXISTS userTbl (											
                        userName char(5) not null, 
                        userId char(8) not null PRIMARY KEY, 
                        mobile VARCHAR(16) not null, 
                        email VARCHAR(20) null, 
                        birth date
						);
SHOW TABLES;
DESC userTbl;

-- 레코드 삽입 테스트 
-- INSERT INTO 테이블명 VALUES (..,..,..,..);
-- INSERT INTO 테이블명 (필드명....)VALUES (..,..,..,..);
-- INSERT INTO 테이블명 VALUES (...), (...), (...), ....;

INSERT INTO userTbl 
	VALUES ('박지민','PJM','010-1234-5678','abc@naver.com','1995-08-31');
    
INSERT INTO userTbl 
	VALUES ('박지민','BJM','011-2345-5678',NULL, NULL);

INSERT INTO userTbl 
	VALUES 
		('이지민','LJM','010-5678-7777','ccc@naver.com','1998-05-31'), 
        ('황지민','HJM','011-1567-7890','dddd@naver.com','1994-11-30'),
        ('최지민','CJM','없음',NULL, NULL);

SELECT * FROM userTbl;

-- 테이블 구조 변경 ALTER TABLE 
-- 컬럼 추가, 컬럼 수정, 컬럼 삭제 

-- ALTER TABLE 테이블명
-- 	ADD 컬럼명 데이터형( CHAR(), INT, VARCHAR(), DATE, DATETIME ... )
-- 		[DEFAULT 디폴트값] -- 기본값 설정 
-- 		[NULL/NOT NULL]; -- Null 허용함

-- userTbl 테이블에서 homepage varchar(30) 컬럼 추가 
ALTER TABLE userTbl
	ADD homepage VARCHAR(30)  -- 컬럼 추가 
		DEFAULT 'http://google.com' -- 디폴트값
		NULL; -- Null 허용함

DESC userTbl;
SELECT * FROM userTbl;

-- 테이블 구조 변경후에 레코드 삽입 테스트
INSERT INTO userTbl 
	VALUES ('김철수','KCS','019-2345-5678',NULL, NULL, NULL);
    
INSERT INTO userTbl (userName, userId, mobile)
	VALUES ('윤철수','LCS','011-9999-5678');
    
SELECT * FROM userTbl;

-- userTbl 테이블에서 addr varchar(50) 컬럼 추가 
ALTER TABLE userTbl
	ADD addr VARCHAR(50);
DESC userTbl;

SELECT * FROM userTbl;

-- 컬럼 삭제 
-- 외래키나 기본키가 설정되어 있지 않은 경우 
-- ALTER TABLE 테이블명
-- 			DROP COLUMN 컬럼명;
DESC userTbl;
ALTER TABLE userTbl
	DROP COLUMN addr;
DESC userTbl;
SELECT * FROM userTbl;    

-- 데이타가 있는 컬럼 삭제 
ALTER TABLE userTbl
	DROP COLUMN email;
DESC userTbl;
SELECT * FROM userTbl;   

--  NOT NULL 속성의 컬럼 삭제 가능 ?
ALTER TABLE userTbl
	DROP COLUMN mobile;
DESC userTbl;
SELECT * FROM userTbl; 

--  기본키로 설정된 컬럼 삭제 가능 
ALTER TABLE userTbl
	DROP COLUMN userId;
DESC userTbl;
SELECT * FROM userTbl; 

-- 컬럼 수정 
-- 컬럼명1을 컬럼명2로 수정 
-- ALTER TABLE 테이블명 
-- 	CHANGE COLUMN 컬럼명1 컬럼명2 데이타형 [NULL 또는 NOT NULL] ;
DESC userTbl;

-- homepage => url 
ALTER TABLE userTbl
	CHANGE COLUMN homepage url VARCHAR(50) NULL;
DESC userTbl;
SELECT * FROM userTbl; 

-- birth => birth_date int ?
-- date => int 자료형 가능 
ALTER TABLE userTbl
	CHANGE COLUMN birth birth_date int null;
DESC userTbl;
SELECT * FROM userTbl; 


