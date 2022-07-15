-- ANIMAL_INS 테이블의 NAME 컬럼과 NAME 컬럼 카운트
SELECT NAME, COUNT(*) FROM ANIMAL_INS
-- 조건: NAME이 NULL(빈값)이 아닌 것
WHERE NAME IS NOT NULL
-- NAME으로 그룹화
GROUP BY NAME
-- 그룹 조건: 카운트가 2 이상인 것
HAVING COUNT(NAME) >= 2
-- 이름 순으로 오름차순 정렬
ORDER BY NAME;