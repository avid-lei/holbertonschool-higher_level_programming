-- MySQL script to list al cities contained in database
-- echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT cities.id, cities.name, states.name 
FROM cities JOIN states
ON cities.state_id = states.id;