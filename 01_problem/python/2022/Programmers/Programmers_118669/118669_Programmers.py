import sys, heapq
sys.setrecursionlimit(50000)


def move(now, intensity):
    '''
    재귀를 통해 가장 적은 intensity를 확인하는 함수
    :param now: 현재 지점
    :param intensity: 최대 intensity
    :return: 최대 intensity
    '''
    if now in points:
        return intensity

    res = 0
    for t, ed in adj[now]:
        if res and t > res:
            continue

        if ed not in tops and visited[ed] == 0:
            visited[ed] = 1
            res = move(ed, max(intensity, t))
            visited[ed] = 0

    return res


def solution(n, paths, gates, summits):
    '''
    :param n: 지점 수
    :param paths: 등산로 정보
    :param gates: 출입구 지점
    :param summits: 봉우리 지점
    :return: 최소의 intensity, 해당 경로의 봉우리
    '''

    global adj, points, tops, visited

    answer = []
    set_adj = [[] for _ in range(n + 1)]
    for i in range(len(paths)):
        a, b, w = paths[i]
        heapq.heappush(set_adj[a], [w, b])
        heapq.heappush(set_adj[b], [w, a])

    adj = set_adj
    points = gates
    tops = summits
    visited = [0] * (n + 1)

    mn = 500000000000
    for j in range(len(summits)):
        ret = move(summits[j], 0)
        if ret < mn:
            mn = ret
            answer = [summits[j], ret]

    return answer


adj = []
points = []
tops = []
visited = []
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
