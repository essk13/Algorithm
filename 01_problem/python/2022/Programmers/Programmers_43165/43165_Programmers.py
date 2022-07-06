# DFS 풀이
def targeting(now, res, ns, t):
    # 마지막 번호까지 계산 후 타겟넘버와 일치하면 1을 리턴
    if now >= len(ns):
        if res == t:
            return 1
        return 0
    ans = 0
    # +와 -의 경우를 재귀함수로 확인
    ans += targeting(now + 1, res + ns[now], ns, t)
    ans += targeting(now + 1, res - ns[now], ns, t)
    return ans


def solution(numbers, target):
    answer = targeting(0, 0, numbers, target)
    return answer


nums = list(map(int, input().split()))
tg = int(input())
print(solution(nums, tg))
