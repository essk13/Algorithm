-- ANIMAL_INS 테이블에서 ANIMAL_ID, NAME, DATETIME 컬럼 선택
-- DATE_FORMAT() 함수로 '%Y-%m-%d' 형식으로 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') FROM ANIMAL_INS
-- ANIMAL_ID로 오름차순 정렬
ORDER BY ANIMAL_ID;

-- %Y = 연도 4자리 숫자
-- %y = 연도 2자리 숫자
-- %M = 영어 월
-- %m = 월 2자리 숫자
-- %D = 숫자 + 영어
-- %d = 일 2자리 숫자