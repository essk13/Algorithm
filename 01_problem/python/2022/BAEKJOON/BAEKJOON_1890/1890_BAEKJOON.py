import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

q = deque([(0, 0)])
ans = 0
while q:
    x, y = q.popleft()
    # 목적지 도착 시 종료
    if MAP[x][y] == 0:
        ans += 1
        continue

    nx, ny = x + MAP[x][y], y + MAP[x][y]
    # 아래로 점프
    if 0 <= nx < N:
        if MAP[nx][y] == 0:
            ans += 1
            continue
        mx, my = nx + MAP[nx][y], y + MAP[nx][y]
        # 점프 후 이동
        if 0 <= mx < N:
            q.append((mx, y))
        if 0 <= my < N:
            q.append((nx, my))

    # 오른쪽으로 점프
    if 0 <= ny < N:
        if MAP[x][ny] == 0:
            ans += 1
            continue
        mx, my = x + MAP[x][ny], ny + MAP[x][ny]
        # 점프 후 이동
        if 0 <= mx < N:
            q.append((mx, ny))
        if 0 <= my < N:
            q.append((x, my))

print(ans)
