-- ANIMAL_INS 테이블에서 ANIML_ID, NAME, SEX_UPON_INTAKE 컬럼을 조회
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
-- 조건: NAME이 'Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty' 안에 있는 로우
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
-- ANIMAL_ID를 기준으로 정렬
ORDER BY ANIMAL_ID;