WITH sseries(filmid, maintitle) as
(SELECT seriesid, maintitle FROM series)
SELECT s.maintitle AS "TV-serie"
FROM sseries AS s JOIN filmrating as fr USING (filmid)
WHERE fr.rank = (SELECT max(rank) FROM filmrating WHERE votes > 1000)
GROUP BY s.maintitle, fr.rank, fr.votes HAVING fr.votes > 1000
ORDER BY fr.rank DESC;
