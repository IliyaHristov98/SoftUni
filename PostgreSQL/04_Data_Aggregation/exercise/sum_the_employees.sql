SELECT
	COUNT(CASE department_id WHEN 1 THEN 1 END) AS "Engineering",
	COUNT(CASE department_id WHEN 2 THEN 2 END) AS "Tool Design",
	COUNT(CASE department_id WHEN 3 THEN 3 END) AS "Sales",
	COUNT(CASE department_id WHEN 4 THEN 4 END) AS "Marketing",
	COUNT(CASE department_id WHEN 5 THEN 5 END) AS "Purchasing",
	COUNT(CASE department_id WHEN 6 THEN 6 END) AS "Research and Development",
	COUNT(CASE department_id WHEN 7 THEN 7 END) AS "Production"
FROM employees;