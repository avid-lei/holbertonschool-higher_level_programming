-- lists all genres and display number of shows
-- cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_genres.name AS genre, 
COUNT(*) AS number_of_shows 
FROM tv_show_genres JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;