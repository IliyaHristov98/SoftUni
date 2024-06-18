ALTER TABLE countries
ADD COLUMN capital_code VARCHAR(5);

UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2);