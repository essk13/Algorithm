import sys
from collections import deque
input = sys.stdin.readline

# 나이트가 이동 가능한 모든 방향
dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [1, -1, 2, -2, 2, -2, 1, -1]

for testcase in range(int(input())):
    N = int(input())
    now_r, now_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    # 재방문 방지를 위한 visited 배열 정의
    visited = [[0] * N for _ in range(N)]
    visited[now_r][now_c] = 1
    q = deque([[0, now_r, now_c]])
    while q:
        cnt, r, c = q.popleft()
        # 목표 지점에 도착한 경우 종료
        if [r, c] == [target_r, target_c]:
            print(cnt)
            break

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            # 체스 판을 벗어나는 경우 종료
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 방문한 적이 있는 경우 종료
            if visited[nr][nc]:
                continue

            # 방문처리 및 q배열에 추가
            visited[nr][nc] = 1
            q.append([cnt + 1, nr, nc])
