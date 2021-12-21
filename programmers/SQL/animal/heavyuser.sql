SELECT * FROM PLACES WHERE HOST_ID in (SELECT HOST_ID from PLACES group by HOST_ID having count(HOST_ID)>1);
--https://programmers.co.kr/learn/courses/30/lessons/77487