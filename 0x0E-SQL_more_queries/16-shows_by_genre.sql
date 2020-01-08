-- list all shows and genres linked to show
-- cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres RIGHT JOIN  tv_shows
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;