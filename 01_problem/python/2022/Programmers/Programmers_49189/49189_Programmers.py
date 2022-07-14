from collections import deque


def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    # 간선 간 관계 그래프 정의
    for e in edge:
        adj[int(e[0])].append(int(e[1]))
        adj[int(e[1])].append(int(e[0]))

    visited = [20000] * (n + 1)
    visited[1] = 0
    q = deque([1])
    while q:
        now = q.popleft()
        for nxt in adj[now]:
            # 이동 거리가 더 짧은 경우만 이동
            if visited[now] + 1 < visited[nxt]:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

    mx = 0
    # 이동거리가 가장 긴 거리 확인
    for v in visited:
        if 20000 > v > mx:
            mx = v
    return visited.count(mx)


N = int(input())
line = input()
print(solution(N, line))
