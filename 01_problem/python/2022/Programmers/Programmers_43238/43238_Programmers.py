def solution(n, times):
    answer = n * max(times)
    times.sort(reverse=True)
    st, ed = 0, answer
    while st <= ed:
        mid = (st + ed) // 2
        res = 0
        for i in range(len(times)):
            res += mid // times[i]
            if res >= n:
                ed = mid - 1
                answer = min(answer, mid)
                break
        else:
            st = mid + 1

    return answer


N = int(input())
T = list(map(int, input().split()))
print(solution(N, T))
