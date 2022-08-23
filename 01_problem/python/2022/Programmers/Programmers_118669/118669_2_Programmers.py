import heapq


def solution(n, paths, gates, summits):
    '''
    가장 적은 intensity를 지닌 등산 경로의 봉우리와 intensity를 찾는 함수
    :param n: 지점 수
    :param paths: 등산로 정보
    :param gates: 출입구 지점
    :param summits: 봉우리 지점
    :return: [최소의 intensity, 해당 경로의 봉우리]
    '''

    answer = []
    mn = 10000001

    # 지점 간 연결 정보
    adj = [[] for _ in range(n+1)]
    for a, b, w in paths:
        adj[a].append([w, b])
        adj[b].append([w, a])

    # 봉우리에서 출발하여 출입구로 향하는 길 탐색 (작은 번호의 봉우리부터 탐색)
    summits.sort()
    for st in summits:
        visited = [10000001] * (n + 1)
        visited[st] = 0

        heap = [[0, st]]
        while heap:
            intensity, now = heapq.heappop(heap)
            # 최소값보다 크거나 같으면 탐색 종료
            if intensity >= mn:
                break

            # 다른 봉우리에 도착한 경우 탐색 X
            if now != st and now in summits:
                continue

            # 출입구에 도착한 경우 탐색 종료
            if now in gates:
                if mn > intensity:
                    mn = intensity
                    answer = [st, intensity]
                break

            # 현재 지점과 연결된 지점 탐색
            for w, ed in adj[now]:
                nxt = max(intensity, w)
                # 방문하려는 지점의 intensity보다 크거나 같은 경우 탐색 X
                if visited[ed] <= nxt:
                    continue
                visited[ed] = nxt
                heapq.heappush(heap, [nxt, ed])

    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
