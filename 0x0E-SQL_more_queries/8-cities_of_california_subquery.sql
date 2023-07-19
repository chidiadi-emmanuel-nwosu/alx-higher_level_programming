-- script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa.
SELECT DISTINCT c.id, c.name
FROM cities c, states s
WHERE c.state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY c.id;
