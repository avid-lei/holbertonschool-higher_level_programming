-- MySQL script to list all cities of CA found in database
-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
USE hbtn_0d_usa;
SELECT * FROM cities
WHERE state_id = 1
ORDER BY id ASC;