-- MySQL script to list all cities of CA found in database
-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT `id`, `name` FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California");