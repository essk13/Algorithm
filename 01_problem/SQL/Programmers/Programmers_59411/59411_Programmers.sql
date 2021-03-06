SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS AS INS
-- INS와 OUTS LEFT JOIN
LEFT JOIN ANIMAL_OUTS AS OUTS
-- JOIN 조건: INS와 OUTS의 ID
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
-- 조건: OUTS의 ID가 NULL이 아닌 것
WHERE OUTS.ANIMAL_ID IS NOT NULL
-- 보호 기간 기준으로 내림차순 정렬
-- ORDER BY OUTS.DATETIME - INS.DATETIME DESC
ORDER BY INS.DATETIME - OUTS.DATETIME
-- 제한: 2개
LIMIT 2;