UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries(monastery_name, country_code)
VALUES
	(
	'Hanga Abbey',
	(SELECT
		country_code
	FROM
		countries
	WHERE
		country_name = 'Tanzania')
	),
	(
	'Myin-Tin-Daik',
	(SELECT
		country_code
	FROM
		countries
	WHERE
		country_name = 'Myanmar')
	);

SELECT
	con.continent_name,
	c.country_name,
	COUNT(m.country_code) AS monasteries_count
FROM
	countries AS c
JOIN
	continents AS con
USING
	(continent_code)
LEFT JOIN
	monasteries AS m
USING
	(country_code)
WHERE
	c.three_rivers IS NOT TRUE
GROUP BY
	c.country_name,
	con.continent_name
ORDER BY
	monasteries_count DESC,
	c.country_name;