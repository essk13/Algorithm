-- 풀이1: DISTINCT
-- ANIMAL_INS 테이블에서 NAME의 중복을 제거 후 카운트
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
-- 조건: NAME이 NULL이 아닌 것
-- WHERE NAME IS NOT NULL;
-- 추가: COUNT의 경우 NULL을 포함하지 않고 계산