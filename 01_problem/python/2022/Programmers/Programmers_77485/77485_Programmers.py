def solution(rows, columns, queries):
    answer = []
    # 숫자 배열 정의 (1행 부터 시작하는 배열을 위해 0으로 구성된 배열 사전 생성
    table = [[0] * (columns + 1)]
    st, ed = 1, columns
    # 길이에 맞춰 1열 부터 시작하도록 하기 위해 0으로 시작하는 숫자 배열 생성 및 table 배열에 추가
    while ed <= rows * columns:
        table.append([0] + list(range(st, ed + 1)))
        st = ed + 1
        ed += columns

    # 회전 횟수 만큼 진행
    for x1, y1, x2, y2 in queries:
        nx, ny = x1, y1
        # 회전 사이즈 측정
        r, c = x2 - x1, y2 - y1

        mi = rows * columns
        previous = 0
        cnt = 1
        # 한 바퀴 회전해서 시작점에 도착할 때 까지 반복문 수행
        while cnt <= r * 2 + c * 2 + 1:
            now = table[nx][ny]
            mi = min(mi, now)
            # 이전 값이 존재하는 경우 현재 위치 숫자 변경
            if previous:
                table[nx][ny] = previous
            previous = now

            # 구간 별 회전 방향 설정
            if cnt <= c:
                ny += 1
            elif c < cnt <= c + r:
                nx += 1
            elif c + r < cnt <= c * 2 + r:
                ny -= 1
            else:
                nx -= 1

            cnt += 1

        answer.append(mi)
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
