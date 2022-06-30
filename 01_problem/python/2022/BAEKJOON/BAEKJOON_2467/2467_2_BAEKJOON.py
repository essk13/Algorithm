N = int(input())
liquid = list(map(int, input().split()))

res = 2000000000
ans = []
la, lb = 0, N - 1
while la < lb:
    result = liquid[la] + liquid[lb]
    # 혼합물 절대값이 더 작은 경우 결과 초기화
    if abs(result) < res:
        res = abs(result)
        ans = [liquid[la], liquid[lb]]

    # 혼합물이 0이된 경우 종료
    if result == 0:
        break
    # 혼합물이 양수인 경우 b용액 번호 감소
    elif result > 0:
        lb -= 1
    # 혼합물이 음수인 경우 a용액 번호 증가
    else:
        la += 1

print(*ans)
