from collections import deque
'''
첫 항목을 마지막으로 이동시키는 작업이 필요함으로 deque 사용
'''


def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    # 최초 순서를 기준으로 출력 순서 확인을 위한 check 배열 정의
    check = deque(list(range(len(priorities))))
    while q:
        # 우선순위가 가장 높은 문서와 현재 문서가 일치하는 경우 출력 실행
        if q[0] == max(q):
            q.popleft()
            now = check.popleft()
            answer += 1
            if now == location:
                return answer
        # 일치하지 않는 경우 맨 뒤로 이동
        else:
            priority = q.popleft()
            q.append(priority)
            now = check.popleft()
            check.append(now)


print(solution([2, 1, 3, 2], 2))
