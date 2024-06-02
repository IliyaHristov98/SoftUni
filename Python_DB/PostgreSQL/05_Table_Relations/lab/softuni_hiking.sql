SELECT
	r.start_point,
	r.end_point,
	c.id,
	CONCAT_WS(' ', c.first_name, c.last_name)
FROM routes AS r
	JOIN campers as c
		ON c.id = r.leader_id;