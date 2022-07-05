def solution(n):
    answer = ''
    nums = ['4', '1', '2']
    while n:
        remainder = n % 3
        if not remainder:
            n -= 1
        answer = nums[remainder] + answer
        n //= 3

    return answer


num = int(input())
print(solution(num))
