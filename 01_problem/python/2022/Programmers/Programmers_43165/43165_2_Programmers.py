# BFS 풀이
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    while q:
        res, idx = q.popleft()
        if idx >= len(numbers):
            if res == target:
                answer += 1
            continue
        q.append((res + numbers[idx], idx + 1))
        q.append((res - numbers[idx], idx + 1))

    return answer


nums = list(map(int, input().split()))
tg = int(input())
print(solution(nums, tg))
