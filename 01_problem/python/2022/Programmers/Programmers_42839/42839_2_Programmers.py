def combination(nums, lv, mx, n):
    global res
    # mx 만큼 숫자를 선택한 경우 소수 판별
    if lv == mx:
        if n == '':
            return
        res.add(int(n))
        return
    for i in range(len(nums)):
        if not used[i]:
            used[i] = 1
            combination(nums, lv + 1, mx, n + nums[i])
            used[i] = 0
    return


def check(num):
    if num < 2:
        return 0
    # 소수 판별
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(numbers):
    global used
    answer = 0
    # 선택할 숫자의 개수에 따라 소수 탐색
    for i in range(1, len(numbers) + 1):
        used = [0] * len(numbers)
        combination(numbers, 0, i, '')

    nums = list(res)
    for j in range(len(nums)):
        answer += check(nums[j])
    return answer


res = set()
used = []
print(solution('17'))
