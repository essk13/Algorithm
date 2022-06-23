import sys, heapq
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

# 누적 방문을 허용하기 위한 heapq 사용
q = [(0, 0)]
while q:
    x, y = heapq.heappop(q)
    n = MAP[x][y]
    # 이동 횟수가 존재하는 경우
    if n:
        nx, ny = x + n, y + n
        # 아래로 이동
        if 0 <= nx < N:
            # 한 번도 방문한 적 없는 경우
            if visited[nx][y] == 0:
                heapq.heappush(q, (nx, y))
            # 방문 이력이 있는 경우
            visited[nx][y] += visited[x][y]

        # 우로 이동
        if 0 <= ny < N:
            # 한 번도 방문한 적 없는 경우
            if visited[x][ny] == 0:
                heapq.heappush(q, (x, ny))
            # 방문 이력이 있는 경우
            visited[x][ny] += visited[x][y]

print(visited[N-1][N-1])
