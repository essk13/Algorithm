import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

# 체크리스트 생성
checkList = defaultdict(lambda: 0)
for n in nums:
    checkList[n] = 1

# 체크리스트에 값이 존재하면 1 출력 / 존재하지 않으면 0 출력
for a in arr:
    if checkList[a]:
        print(1)
    else:
        print(0)
