def solution(progresses, speeds):
    answer = []
    now, ed = 0, len(progresses) - 1
    date = 0
    while now <= ed:
        cnt = 1
        # 현재 작업이 완료될 때 까지 진행 (진행 시간 누적)
        while progresses[now] < 100:
            progresses[now] += speeds[now]
            date += 1

        # 현재까지 진행된 시간만큼 진행률 증가 후 완료여부 판단
        for n in range(now + 1, len(progresses)):
            progresses[n] += speeds[n] * date
            if progresses[n] >= 100:
                cnt += 1
            else:
                break

        answer.append(cnt)
        now += cnt
    return answer


pro = list(map(int, input().split()))
spd = list(map(int, input().split()))
print(solution(pro, spd))
