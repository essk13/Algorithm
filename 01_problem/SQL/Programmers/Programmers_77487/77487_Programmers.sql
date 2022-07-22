-- A라는 이름으로 PLACES 테이블의 모든 컬럼 선택
SELECT ID, NAME, HOST_ID FROM PLACES AS A
-- 조건: A와 B 테이블의 ID가 같으면서 HOST_ID가 1개 초과인 것
WHERE (SELECT COUNT(HOST_ID) AS CNT FROM PLACES AS B
      WHERE A.HOST_ID = B.HOST_ID) > 1
-- ID 기준으로 오름차순 정렬
ORDER BY ID;