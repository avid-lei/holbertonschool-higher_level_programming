-- MySQL script to list all shows contained in database 
-- cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows 
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;