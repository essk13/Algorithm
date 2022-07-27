from collections import deque


def melt(i, j):
    q = deque([(i, j)])
    while q:
        y, x = q.popleft()
        for d in range(4):
            nr, nc = y + dr[d], x + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc]:
                continue

            if MAP[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
            elif MAP[y][x]:
                MAP[y][x] -= 1
    return


def year(y):
    global keep
    res = y
    iceberg = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c] and not visited[r][c]:
                if iceberg > 0:
                    keep = False
                    return res
                visited[r][c] = 1
                melt(r, c)
                iceberg += 1

    if not iceberg:
        keep = False
        return 0

    return res + 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

ans = 0
keep = True
while keep:
    visited = [[0] * M for _ in range(N)]
    ans = year(ans)

print(ans)
