SELECT f.title AS "Tittel", fd.year AS "Produksjonsår"
FROM film as f JOIN filmgenre AS fg USING (filmid) JOIN filmdescription AS fd USING (filmid) JOIN filmgenre AS fg2 USING (filmid) 
GROUP BY fd.year, f.title, fg.genre, f.filmid, fg2.genre
HAVING fg.genre LIKE '%Film-Noir%' AND fg2.genre LIKE 'Comedy';

/* fant ut jeg kan fjerne filmdescription fordi film inneholder 
produksjonsår, gjør det hvis jeg rekker å finpusse*/
