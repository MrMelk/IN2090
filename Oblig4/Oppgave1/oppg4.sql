SELECT f.filmid AS "filmid", fg.genre AS "genre", fd.year AS "year", f.title AS "title"
FROM film as f JOIN filmgenre AS fg USING (filmid) JOIN filmdescription AS fd USING (filmid) JOIN filmgenre AS fg2 USING (filmid) 
GROUP BY fd.year, f.title, fg.genre, f.filmid, fg2.genre
HAVING fg.genre LIKE '%Film-Noir%' AND fg2.genre LIKE 'Comedy';
