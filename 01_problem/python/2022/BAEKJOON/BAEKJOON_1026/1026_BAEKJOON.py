N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 내림차순 B는 오름차순 정렬
A.sort(reverse=True)
B.sort()

answer = 0
# 함수 S 수행
for i in range(N):
    answer += A[i] * B[i]

print(answer)
