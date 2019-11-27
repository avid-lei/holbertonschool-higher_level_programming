-- list all comedy shows
-- cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_shows.title 
FROM tv_shows JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "comedy"
ORDER BY tv_shows.title;