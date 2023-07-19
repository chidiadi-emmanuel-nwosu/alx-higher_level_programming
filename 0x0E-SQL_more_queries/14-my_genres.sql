-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
WHERE tsg.show_id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
)
ORDER BY name;
