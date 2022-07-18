-- 풀이1: IFNULL() 함수
-- ANIMAL_INS 테이블에서 ANIMAL_TYPE, NAME, SEX_UPON_INTAKE 선택
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS
-- ANIMAL_ID로 오름차순 정렬
ORDER BY ANIMAL_ID;

-- 풀이2: CASE문
SELECT ANIMAL_TYPE,
CASE WHEN NAME IS NULL THEN 'No name'
    ELSE NAME
END AS NAME,
SEX_UPON_INTAKE FROM ANIMAL_INS
ORDER BY ANIMAL_ID;