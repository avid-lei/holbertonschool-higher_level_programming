-- create table with unique ID
-- cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1,
name VARCHAR(256),
UNIQUE(id));