N = int(input())
liquid = list(map(int, input().split()))

# 산성 용액 시작점 확인
acid = -1
for n in range(N):
    if liquid[n] > 0:
        acid = n
        break

ans = 20000000000
la = lb = 0
if 0 < acid <= N - 1:
    st = acid - 1
    ed = acid
    stop = True
    while stop:
        if (st, ed) == (0, N-1):
            stop = False
        res = liquid[st] + liquid[ed]
        if abs(res) < ans:
            ans = abs(res)
            la = liquid[st]
            lb = liquid[ed]
        if res > 0 and st > 0:
            st -= 1
        elif res < 0 and ed < N - 1:
            ed += 1
        elif st == 0 and ed < N - 1:
            ed += 1
        elif ed == N - 1 and st > 0:
            st -= 1
        elif res == 0:
            break

    else:
        if acid > 1:
            res = liquid[acid-1] + liquid[acid-2]
            if abs(res) < ans:
                ans = abs(res)
                la = liquid[acid-2]
                lb = liquid[acid-1]
        if acid < N - 1:
            res = liquid[acid] + liquid[acid+1]
            if abs(res) < ans:
                ans = abs(res)
                la = liquid[acid]
                lb = liquid[acid+1]

elif acid == 0:
    la, lb = liquid[0], liquid[1]
elif acid < 0:
    la, lb = liquid[-2], liquid[-1]

print('{} {}'.format(la, lb))
