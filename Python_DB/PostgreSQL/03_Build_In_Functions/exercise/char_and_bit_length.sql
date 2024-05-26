SELECT
	CONCAT_WS(' ', mou.mountain_range, pea.peak_name) as mountain_information,
	CHAR_LENGTH(CONCAT_WS(' ', mou.mountain_range, pea.peak_name)) AS characters_length,
	BIT_LENGTH(CONCAT_WS(' ', mou.mountain_range, pea.peak_name)) AS bits_of_a_tring
FROM
	mountains AS mou,
	peaks AS pea
WHERE mou.id = pea.mountain_id;