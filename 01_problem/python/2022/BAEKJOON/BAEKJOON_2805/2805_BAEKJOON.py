import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 중앙값 정의를 위한 시작, 종료 값
st = 0
ed = max(trees)

ans = 0
while 1:
    mid = (st + ed) // 2

    # 종료 조건
    if st == ed or mid == ans:
        break

    res = 0
    for t in trees:
        if t > mid:
            res += (t - mid)
        if res >= M:
            ans = max(mid, ans)
            st = mid
            break
    
    # 가능한 경우 더 큰 중앙값 정의 / 불가능한 경우 더 작은 중앙값 정의
    else:
        ed = mid

print(ans)
