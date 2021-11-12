SELECT f.title AS "Filmtittel", fp.parttype AS "Deltagertype", count(fp.personid) AS "#deltagere"
FROM filmitem AS fi JOIN film AS f USING (filmid) JOIN filmparticipation AS fp USING (filmid)
GROUP BY fi.filmtype, f.title, fp.parttype
HAVING f.title LIKE '%Lord of the Rings%' AND fi.filmtype = 'C'; 
