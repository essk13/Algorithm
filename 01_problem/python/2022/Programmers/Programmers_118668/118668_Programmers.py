from heapq import heappop, heappush
# Fail _ heapq (효율성 실패)


def solution(alp, cop, problems):
    '''
    :param alp: 알고력
    :param cop: 코딩력
    :param problems: 문제 리스트
    :return: 모든 문제를 풀 수 있는 알고력과 코딩력을 기르는데 걸리는 최소시간
    '''

    max_alp = max_cop = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    heap = [[0, alp, cop]]
    while heap:
        now_cost, now_alp, now_cop = heappop(heap)
        if now_alp >= max_alp and now_cop >= max_cop:
            return now_cost

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if now_alp < alp_req or now_cop < cop_req:
                continue
            if alp_rwd + cop_rwd <= cost:
                continue

            heappush(heap, [now_cost + cost, now_alp + alp_rwd, now_cop + cop_rwd])

        heappush(heap, [now_cost + 1, now_alp + 1, now_cop])
        heappush(heap, [now_cost + 1, now_alp, now_cop + 1])

    return


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
