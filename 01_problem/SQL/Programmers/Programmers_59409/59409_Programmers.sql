-- ANIMAL_INS 테이블에서 ANIMAL_ID, NAME, SEX_UPON_INTAKE 컬럼 선택
SELECT ANIMAL_ID, NAME,
-- SEX_UPON_INSAKE가 'Neutered' 또는 'Spayed' 포함시 'O'으로 나머지는 'X'로 대체
CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%'
    OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
    ELSE 'X'
    END AS 중성화
FROM ANIMAL_INS
-- ANIMAL_ID로 오름차순 정렬
ORDER BY ANIMAL_ID