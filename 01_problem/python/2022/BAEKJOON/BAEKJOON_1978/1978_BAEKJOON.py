N = int(input())
nums = list(map(int, input().split()))
ans = 0

for n in nums:
    if n == 1:
        continue

    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            break
    else:
        ans += 1

print(ans)
