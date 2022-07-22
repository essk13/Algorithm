from collections import defaultdict


def combination(nums, used, lv, mx, n):
    # mx 만큼 숫자를 선택한 경우 소수 판별
    if lv == mx:
        if n == '':
            return 0
        return check(int(n))
    result = 0
    for i in range(len(nums)):
        if not used[i]:
            used[i] = 1
            result += combination(nums, used, lv + 1, mx, n + nums[i])
            used[i] = 0
    return result


def check(num):
    # 판별한 적 있는 숫자 제외
    if res[num]:
        return 0
    res[num] = 1
    if num < 2:
        return 0
    # 소수 판별
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    # 선택할 숫자의 개수에 따라 소수 탐색
    for i in range(1, len(numbers) + 1):
        answer += combination(numbers, [0] * len(numbers), 0, i, '')
    return answer


res = defaultdict(lambda: 0)
print(solution('17'))
