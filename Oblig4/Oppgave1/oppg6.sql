WITH beanfilms as (SELECT DISTINCT(title), filmid 
FROM film as f JOIN filmparticipation USING (filmid) JOIN filmcharacter USING (partid) 
WHERE filmcharacter LIKE '%Mr. Bean%')
SELECT DISTINCT(title), COUNT(language) as "Antall språk" 
FROM beanfilms LEFT JOIN filmlanguage ON (beanfilms.filmid = filmlanguage.filmid) 
GROUP BY title, language;
