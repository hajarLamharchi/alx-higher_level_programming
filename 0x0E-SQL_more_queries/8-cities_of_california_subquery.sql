-- list all the cities of california that can be found in the database hbtn_0d_usa
SELECT id, name
FROM cities
WHERE id = (SELECT id FROM states WHERE name = 'California')
