-- script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT ts.title, IFNULL(tg.name, 'NULL') AS name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title;
