import sys
input = sys.stdin.readline

N = int(input())
trees = [int(input().strip()) for _ in range(N)]
trees.sort()

# 가로수 사이의 간격 저장
distances = [0] * (N - 1)
for i in range(1, N):
    distances[i-1] = trees[i] - trees[i-1]

# 가장 좁은 거리에서 하나씩 줄여가며 가능한 최대 간격 계산
min_ = min(distances)
while 1:
    t = 0
    ans = 0
    nt = trees[t]
    while t < N:
        # 마지막 나무에 도착하면 반복문 종료
        if t == N - 1:
            t += 1
            continue

        nxt = nt + min_
        # 나무를 심은 곳이 다음 나무위치보다 크면 불가능 (종료)
        if nxt > trees[t+1]:
            break
        # 작거나 같으면 가능 (계속 진행)
        else:
            nt = nxt
            if nxt == trees[t+1]:
                t += 1
                continue
            ans += 1
    # 같은 거리로 만들면 정답 출력 및 종료
    else:
        print(ans)
        break
    # 실패하면 최소 거리 1 감소
    min_ -= 1
