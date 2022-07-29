from collections import deque

N = int(input())
used = [0] * (10 ** 6)

q = deque([(N, [N], 0)])
while q:
    now, nums, total = q.popleft()
    # 1인 경우 계산 종료
    if now == 1:
        print('{}\n{}'.format(total, ' '.join(map(str, nums))))
        break
    # 3으로 나누어 떨어지면서 가장 적은 연산으로 만들어진 경우
    if not now % 3 and not used[now//3]:
        used[now//3] = 1
        q.append((now//3, nums + [now//3], total + 1))
    # 2로 나누어 떨어지면서 가장 적은 연산으로 만들어진 경우
    if not now % 2 and not used[now//2]:
        used[now//2] = 1
        q.append((now//2, nums + [now//2], total + 1))
    # 1을 뺀 결과가 0보다 크면서 가장 적은 연산으로 만들어진 경우
    if now - 1 > 0 and not used[now-1]:
        used[now-1] = 1
        q.append((now - 1, nums + [now-1], total + 1))
