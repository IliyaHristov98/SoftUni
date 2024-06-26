SELECT
	b.booking_id,
	DATE(b.starts_at),
	b.apartment_id,
	CONCAT_WS(' ', first_name, last_name) AS customer_name
FROM
	bookings AS b
RIGHT JOIN
	customers AS c
USING
	(customer_id)
ORDER BY
	customer_name
LIMIT 10;