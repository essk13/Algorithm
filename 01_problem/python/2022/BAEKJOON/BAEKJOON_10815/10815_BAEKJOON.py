import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 소유한 카드 숫자를 저장
card_list = defaultdict(lambda: 0)
for c in cards:
    card_list[c] = 1

# 소유한 카드인 경우 1로 변경
ans = [0] * M
for i in range(M):
    if card_list[nums[i]]:
        ans[i] = 1

print(' '.join(map(str, ans)))
