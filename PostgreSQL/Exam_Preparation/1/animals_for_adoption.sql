SELECT
	a.name,
	EXTRACT(YEAR FROM a.birthdate) AS birth_year,
	ant.animal_type
FROM
	animals AS a
JOIN
	animal_types AS ant
ON
	ant.id = a.animal_type_id
WHERE
	a.owner_id IS NULL
	AND
	ant.animal_type <>'Birds'
	AND
	a.birthdate > '01/01/2017'
ORDER BY
	a.name;