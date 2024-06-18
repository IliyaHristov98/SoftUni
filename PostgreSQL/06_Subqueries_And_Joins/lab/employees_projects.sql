SELECT
	e.employee_id,
	CONCAT_WS(' ', e.first_name, e.last_name),
	p.project_id,
	p.name AS project_name
FROM projects AS p
JOIN employees_projects AS ep
    ON p.project_id = ep.project_id
JOIN employees AS e
    ON e.employee_id = ep.employee_id
WHERE
	p.project_id = 1;