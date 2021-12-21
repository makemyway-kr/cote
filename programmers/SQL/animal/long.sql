--https://programmers.co.kr/learn/courses/30/lessons/59044
SELECT I.NAME,I.DATETIME from ANIMAL_INS as I where I.ANIMAL_ID not in (SELECT ANIMAL_ID from ANIMAL_OUTS) order by I.DATETIME asc LIMIT 3;
--https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT I.ANIMAL_ID,I.NAME from ANIMAL_INS as I join ANIMAL_OUTS as O on I.ANIMAL_ID=O.ANIMAL_ID where DATEDIFF(O.DATETIME,I.DATETIME)>0 order by DATEDIFF(O.DATETIME,I.DATETIME) desc LIMIT 2;