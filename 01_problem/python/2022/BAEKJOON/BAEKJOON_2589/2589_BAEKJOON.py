import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    '''
    현위치에서 가장 먼 'L' 지점까지의 거리를 측정하는 함수
    :param sr: 현위치 r 좌표
    :param sc: 현위치 c 좌표
    :return: 가장 먼 거리
    '''

    visited = [[0] * C for _ in range(R)]
    visited[sr][sc] = 1
    q = deque([[0, sr, sc]])
    mx = 0
    while q:
        t, r, c = q.popleft()
        # 최대값 확인
        mx = max(t, mx)

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # MAP을 벗어나는 경우 종료
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            # 방문한 곳 또는 'W'인 경우 종료
            if visited[nr][nc] or MAP[nr][nc] == 'W':
                continue

            visited[nr][nc] = 1
            q.append([t + 1, nr, nc])
    return mx


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

answer = 0
# MAP을 탐색하여 'L'인 경우 bfs 실행
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
