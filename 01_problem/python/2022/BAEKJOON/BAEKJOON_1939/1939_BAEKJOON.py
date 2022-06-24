import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [defaultdict(lambda: 0) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = max(adj[a][b], c)
    adj[b][a] = max(adj[b][a], c)

s, e = map(int, input().split())

q = deque([s])
st, ed = 1, 1000000000
ans = 0
while st <= ed:
    mid = (st + ed) // 2
    visited = [s]
    while q:
        n = q.popleft()
        if n == e:
            ans = mid
            st = mid + 1
            break

        for i in adj[n]:
            if adj[n][i] >= mid and i not in visited:
                visited.append(i)
                q.append(i)
    else:
        ed = mid - 1

    q = deque([s])
    visited = []

print(ans)
