import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Tk = [0] * N
for i in range(N):
    Tk[i] = int(input())
Tk.sort()

# 이분탐색
st, ed = 0, 10 ** 18
ans = 10 ** 18
while st != ed:
    m = M
    mid = (st + ed) // 2
    j = 0
    while m > 0 and j < N:
        s = mid // Tk[j]
        m -= s
        j += 1

    # 성공 시 종료값 수정
    if m <= 0:
        ans = min(ans, mid)
        ed = mid
    # 실패 시 시작값 수정
    else:
        # 탐색 종료 조건
        if st == mid:
            break
        st = mid

print(ans)
