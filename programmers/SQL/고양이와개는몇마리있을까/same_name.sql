SELECT NAME,COUNT(NAME) as cntname from ANIMAL_INS GROUP BY NAME HAVING cntname>1 ORDER BY NAME;
/*HAVING 절->GROUP BY 에서 조건을 달아줌.*/
/*보호소에 동물이 몇마리가 들어왔을까*/
SELECT COUNT(NAME) as cnt from ANIMAL_INS;
/*중복제거하기 : DISTINCT를 사용하면 중복을 제거할 수 있다!!!*/
SELECT COUNT(DISTINCT NAME)from ANIMAL_INS WHERE NAME is not NULL