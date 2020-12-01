-- 문자열함수 
-- 변수명 지정 
-- SET @변수명 = 값;
SET @userPhone1 = '010-1234-5678';
SET @userPhone2 = '010-9876-4321';
SELECT @userPhone1, @userPhone2; 

-- CONCAT(변수|필드명|문자열)
SELECT CONCAT('***', @userPhone1, '***',@userPhone2) AS '결과'; 

-- 필드에 적용 
USE sqldb;
SHOW TABLES;

SELECT * FROM usertbl;
SELECT name AS '회원명',
      CONCAT(mobile1,'-',mobile2) AS '연락처'
        FROM usertbl;

-- 특정 부분만 표시하기 
-- LEFT(문자열, 길이), RIGHT(문자열, 길이) : 
-- 왼쪽이나 오른쪽을 기준으로 길이만큼 잘라서 표시 
-- SUBSTRING(문자열, 시작위치, 길이) : 
-- 시작위치에서 길이만큼 잘라서 표시한다. 
-- LENGTH(문자열) : 문자열 길이반환 

SET @sample = 'abcdefgghjk';
SELECT    @sample, 
      LEFT(@sample, 3), 
        RIGHT(@sample, 3), 
        SUBSTRING(@sample, 3, 4), 
        LENGTH(@sample);


SELECT LTRIM('    공백제거'), RTRIM('공백제거     ');
SELECT REPEAT('반복', 3);









