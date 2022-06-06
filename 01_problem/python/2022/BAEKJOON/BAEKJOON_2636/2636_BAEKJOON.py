import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

air = deque([[0, 0]])
q = deque()

visited = [[0] * C for _ in range(R)]
visited[0][0] = 1

# 처음부터 공기에 노출된 치즈 표면 저장
while air:
    ar, ac = air.popleft()
    for d in range(4):
        nar, nac = ar + dr[d], ac + dc[d]
        # 범위를 벗어나는 경우
        if nar < 0 or nar >= R or nac < 0 or nac >= C:
            continue
        # 방문한 적이 있는 경우
        if visited[nar][nac]:
            continue
        visited[nar][nac] = 1
        # 공기에 노출된 치즈 표면
        if MAP[nar][nac]:
            q.append([nar, nac])
        # 공기
        else:
            air.append([nar, nac])

t = 1
cheese = len(q)
nq = deque()
# 치즈가 녹는 과정
while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 범위를 벗어나는 경우
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        # 방문한 적이 있는 경우
        if visited[nr][nc]:
            continue
        visited[nr][nc] = 1
        # 다음에 녹을 치즈
        if MAP[nr][nc]:
            nq.append([nr, nc])
        # 구멍에 의한 추가 공기
        else:
            q.append([nr, nc])
    # 다음에 더 녹을 치즈 존재여부 확인
    if len(q) == 0 and len(nq):
        t += 1
        q = nq
        cheese = len(q)
        nq = deque()

print('{}\n{}'.format(t, cheese))
