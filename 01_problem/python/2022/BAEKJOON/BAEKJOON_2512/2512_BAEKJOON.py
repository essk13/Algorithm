import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budget = int(input())

st, ed = 0, max(requests)
ans = 0
# 이분탐색을 통한 최대 예산 측정
while st <= ed:
    res = 0
    mid = (st + ed) // 2
    for i in range(N):
        if mid >= requests[i]:
            res += requests[i]
        else:
            res += mid

        if res > budget:
            # 실패한 경우 최대값 감소
            ed = mid - 1
            break

    else:
        # 성공한 경우 최소값 증가
        ans = mid
        st = mid + 1

print(ans)
