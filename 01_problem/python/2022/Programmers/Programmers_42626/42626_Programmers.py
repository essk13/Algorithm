import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        answer += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + (s2 * 2))
        if scoville[0] >= K:
            break
    else:
        answer = -1

    return answer


s = list(map(int, input().split()))
k = int(input())
print(solution(s, k))
