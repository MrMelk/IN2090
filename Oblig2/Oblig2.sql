--Oblig2
--2a)
SELECT * FROM timelistelinje WHERE timelistelinje.timelistenr = 3;
--2b)
SELECT DISTINCT count(timelistenr) FROM timeliste;

--2c)
SELECT timelistenr FROM timeliste
WHERE timeliste.status NOT LIKE '%utbetalt%';
--2d)
SELECT count(*) AS "antall timelister",
       count(timelistelinje.pause) AS "har pause"
FROM timelistelinje;
--2e)
SELECT * FROM timelistelinje
WHERE timelistelinje.pause IS NULL;
--3a)
SELECT sum(nt.varighet)/60 AS "Utbetalte Timer"
FROM (SELECT * FROM (timeliste join  varighet on timeliste.timelistenr = varighet.timelistenr)
AS  "t" WHERE t.status NOT LIKE '%utbetalt%') AS nt;
--3b)
SELECT DISTINCT t.timelistenr as "Linjer med test/Test"
FROM timelistelinje as t
WHERE (t.beskrivelse LIKE '%test%' OR t.beskrivelse LIKE '%Test%');
--3c)
SELECT sum(nt.varighet)/60*200 AS "Utbetalte Timer"
FROM (SELECT * FROM (timeliste join  varighet on timeliste.timelistenr = varighet.timelistenr)
AS  "t" WHERE t.status LIKE '%utbetalt%') AS nt;
/*
Oppgave 4.a)
For spørring 1: timeliste og timelistelinje har timelistenr og beskrivelse til felles så ved NATURAL JOIN
vil de joines på timelistenr OG beksrivelse som en INNER JOIN. Derfor får vi kun ut at count(*) blir 1
fordi det er bare en rad med lik timelistenr og beskrivelse. Med spørring 2 joiner man tabellene
spesifikt på kolonnene timelistenr.

Oppgave 4.b)
Her får vi samme svar fordi NATURAL JOIN kun har et kolonnenavn til felles så det blir det samme
som en INNER JOIN på timelistenr kollonnene.

 */




