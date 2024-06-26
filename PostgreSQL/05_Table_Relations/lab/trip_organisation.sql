SELECT
	v.driver_id,
	v.vehicle_type,
	CONCAT_WS(' ', c.first_name, c.last_name) AS driver_name
FROM vehicles as v
    JOIN campers as c
        ON c.id = v.driver_id;