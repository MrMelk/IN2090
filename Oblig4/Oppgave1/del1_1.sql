SELECT filmcharacter, count(filmcharacter)
FROM filmcharacter GROUP BY filmcharacter
HAVING count(filmcharacter) > 2000
ORDER BY count(filmcharacter) DESC;
