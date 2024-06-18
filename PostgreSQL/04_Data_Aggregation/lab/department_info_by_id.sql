SELECT
	department_id,
	count(employees)
FROM employees
GROUP BY department_id
ORDER BY department_id;