from collections import deque


def check(p, now):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0] * 5 for _ in range(5)]
    visited[now[0]][now[1]] = 1

    q = deque([now])
    while q:
        r, c, l = q.popleft()
        # 거리두기 규칙을 넘어가면 확인 X
        if l == 2:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            # 방문 지점 또는 벽을 만나면 진행 X
            if visited[nr][nc] or p[nr][nc] == 'X':
                continue
            # 사람을 만나는 경우 True 반환
            if p[nr][nc] == 'P':
                return True

            visited[nr][nc] = 1
            q.append((nr, nc, l + 1))

    return False


def solution(places):
    answer = []
    for place in places:
        stop = False
        for r in range(5):
            if stop:
                break
            for c in range(5):
                if place[r][c] == 'P':
                    # 거리두기를 지키지 않은 사람이 존재하는 경우 0 추가 및 반복 종료
                    if check(place, (r, c, 0)):
                        answer.append(0)
                        stop = True
                        break
        # 반복이 종료된 경우가 아니면 1 추가
        if not stop:
            answer.append(1)
    return answer


print(solution([]))
