import sys
input = sys.stdin.readline


def dfs(x, y):
    if (x, y) == (N - 1, M - 1):
        return 1
    if dp[x][y] >= 0:
        return dp[x][y]

    dp[x][y] = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or MAP[nx][ny] >= MAP[x][y]:
            continue
        dp[x][y] += dfs(nx, ny)
    return dp[x][y]


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
print(dfs(0, 0))
