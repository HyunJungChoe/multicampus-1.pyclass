-- 외래키(FOREIGN KEY)란?
-- 다른 테이블의 특정 필드의 값을 참조한다. 
-- 외래키 설정은?
-- 테이블 생성시 
-- FOREIGN KEY(외래키설정필드명) REFERENCES 외래키가있는테이블명(외래키필드명)

/* 샘플 
CREATE TABLE stdclubTbl
(  num int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   stdName    VARCHAR(10) NOT NULL,
   clubName    VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubTbl(clubName)
);
*/ 

USE sqldb;
SHOW TABLES;
DESC userTbl; -- userID 기본키 
DESC buyTbl; -- num 기본키 자동증감 , userID는 외래키

SELECT * FROM userTbl; 
SELECT * FROM buyTbl; 

-- 외래키 테스트 
-- demo_people (name, phone, pid(PK))
-- demo_property (spid(PK), pid(FK), selling)

use tableDB;
CREATE TABLE demo_people 
(
   pid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(10) NOT NULL,
    phone VARCHAR(16) NULL
);

DESC demo_people;

-- FOREIGN KEY(외래키설정필드명) REFERENCES 외래키가있는테이블명(외래키필드명)
CREATE TABLE demo_property 
(
   spid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
   pid int NOT NULL,
    selling VARCHAR(30) NOT NULL,
    FOREIGN KEY(pid) REFERENCES  demo_people(pid)
);

DESC demo_property;
SHOW TABLES;

-- 외래키가 있는 테이블에서 레코드 삽입 테스트 
-- demo_people , demo_property

INSERT INTO demo_people VALUES (NULL, '신짱구', '011-9090-9999');
SELECT * FROM demo_people;

INSERT INTO demo_property VALUES (NULL, 1, '야구공');
SELECT * FROM demo_property;

INSERT INTO demo_people VALUES 
      (NULL, '오짱구', '011-5555-1234'), (NULL, '박짱구', NULL);
SELECT * FROM demo_people;

-- 외래키가 설정된 테이블 
-- INSERT INTO demo_property VALUES (NULL, 5, '노트북');
INSERT INTO demo_property VALUES (NULL, 3, '노트북');
INSERT INTO demo_property VALUES (NULL, 2, '쇼파');
INSERT INTO demo_property VALUES (NULL, 2, '자동차');
SELECT * FROM demo_property;

-- 이너 조인 
SELECT * FROM demo_people D1
   INNER JOIN demo_property D2
    ON D1.pid = D2.pid;
    

use sqldb;

SELECT * FROM usertbl;