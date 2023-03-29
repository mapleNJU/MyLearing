use maple;

CREATE UNIQUE INDEX idx_emp_no ON employees (emp_no);

CREATE INDEX idx_name ON employees (first_name, last_name);

CREATE INDEX idx_hash_hiredate USING HASH ON employees (hire_date);

SHOW INDEX FROM employees;

EXPLAIN SELECT * FROM employees WHERE hire_date='1990-01-01';