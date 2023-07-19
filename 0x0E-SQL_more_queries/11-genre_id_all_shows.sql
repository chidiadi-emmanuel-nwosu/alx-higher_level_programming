-- script that lists all shows contained in
-- hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.title, IFNULL(tsg.genre_id, 'NULL') AS genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg on ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
