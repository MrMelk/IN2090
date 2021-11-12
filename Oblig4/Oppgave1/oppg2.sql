SELECT country, count(country) AS "antall forekomster"
FROM filmcountry
GROUP BY country HAVING count(country) = 1;
