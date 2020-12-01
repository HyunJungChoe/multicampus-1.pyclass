-- 부서별로 직원의 성별 인원수로 표시. 부서 이름도 함께 표시한다. 현재근무중
-- group by, count()
/*
  부서명    성별   직원수 
  Sales    M     ?
  Sales    F     ?
  ...
*/
SELECT * FROM dept_emp;
SELECT * FROM departments;     
SELECT * FROM employees;

-- 3개의 테이블 조인. 현재근무중 
SELECT *
      FROM dept_emp DE
      INNER JOIN employees E ON DE.emp_no = E.emp_no
        INNER JOIN departments D ON DE.dept_no = D.dept_no
        WHERE DE.to_date = '9999-01-01';
 
 
-- 부서별, 성별 인원수 그룹화
SELECT  D.dept_name AS '부서명', 
      E.gender AS '성별',
      count(*) AS '직원수'
      FROM dept_emp DE
      INNER JOIN employees E ON DE.emp_no = E.emp_no
        INNER JOIN departments D ON DE.dept_no = D.dept_no
        WHERE DE.to_date = '9999-01-01'
        GROUP BY D.dept_name, E.gender
        ORDER BY D.dept_name, E.gender;
        
 