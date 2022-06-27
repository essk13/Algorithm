import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def pre(i, j):
    visited = [0] * (N + 1)
    visited[j] = 1
    q = deque([j])
    while q:
        n = q.popleft()
        if n == i:
            return -1

        for t in res[n][0]:
            if visited[t]:
                continue
            visited[t] = 1
            q.append(t)
    return 0


def nxt(i, j):
    visited = [0] * (N + 1)
    visited[j] = 1
    q = deque([j])
    while q:
        n = q.popleft()
        if n == i:
            return 1

        for t in res[n][1]:
            if visited[t]:
                continue
            visited[t] = 1
            q.append(t)
    return 0


N, K = map(int, input().split())
res = [defaultdict(lambda: []) for _ in range(N + 1)]
for _ in range(K):
    a, b = map(int, input().split())
    res[a][1].append(b)
    res[b][0].append(a)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    ans = pre(a, b)
    if ans:
        print(ans)
        continue
    ans = nxt(a, b)
    print(ans)
