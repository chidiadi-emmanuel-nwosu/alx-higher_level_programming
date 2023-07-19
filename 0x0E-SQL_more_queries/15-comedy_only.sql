-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id = (
	SELECT id
	FROM tv_genres
	WHERE name = 'Comedy'
)
ORDER BY title;
