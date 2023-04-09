use maple;

CREATE VIEW V_EMP_DEPT(EMP_NO, DEPT_NO, DEPT_NAME) 
AS 
	SELECT
	    de.emp_no,
	    d.dept_no,
	    d.dept_name
	FROM
	    dept_emp de,
	    departments d
	WHERE de.dept_no = d.d
DEPT_NO; 

CREATE VIEW V_FINANCE_EMPLOYEES AS 
	SELECT e.*
	FROM
	    employees e,
	    v_emp_dept ved
	WHERE
	    e.emp_no = ved.emp_no
	    AND ved.dept_name = 'Finance'
	WITH CHECK
OPTION; 

CREATE VIEW V_FINANCE_SALARIES AS 
	SELECT s.*
	FROM
	    salaries s,
	    v_emp_dept ved
	WHERE
	    s.emp_no = ved.emp_no
	    AND ved.dept_name = 'Finance'
	WITH CHECK
OPTION; 

CREATE VIEW V_FINANCE_DEPT_EMP AS 
	SELECT de.*
	FROM
	    dept_emp de,
	    v_emp_dept ved
	WHERE
	    de.emp_no = ved.emp_no
	    AND ved.dept_name = 'Finance'
	WITH CHECK
OPTION; 

CREATE VIEW V_FINANCE_TITLES AS 
	SELECT t.*
	FROM titles t, v_emp_dept ved
	WHERE
	    t.emp_no = ved.emp_no
	    AND ved.dept_name = 'Finance'
	WITH CHECK
OPTION; 

CREATE ROLE role_finance_manager, role_finance_staff;

GRANT
    ALL ON employees.v_finance_employees TO role_finance_manager
WITH
GRANT OPTION;

GRANT
    ALL ON employees.v_finance_salaries TO role_finance_manager
WITH
GRANT OPTION;

GRANT
    ALL ON employees.v_finance_dept_emp TO role_finance_manager
WITH
GRANT OPTION;

GRANT
    ALL ON employees.v_finance_titles TO role_finance_manager
WITH
GRANT OPTION;

GRANT SELECT ON employees.* TO role_finance_manager;

GRANT SELECT,INSERT ON v_finance_employees TO role_finance_staff;

GRANT SELECT, INSERT ON v_finance_salaries TO role_finance_staff;

GRANT SELECT, INSERT ON v_finance_dept_emp TO role_finance_staff;

GRANT SELECT, INSERT ON v_finance_titles TO role_finance_staff;

CREATE USER user_manager IDENTIFIED BY '123456';

CREATE USER user_staff IDENTIFIED BY '123456';

GRANT role_finance_manager TO user_manager;

GRANT role_finance_staff TO user_staff;

SHOW GRANTS FOR role_finance_manager;

SHOW GRANTS FOR role_finance_staff;

SHOW GRANTS FOR user_manager;

SHOW GRANTS FOR user_staff;