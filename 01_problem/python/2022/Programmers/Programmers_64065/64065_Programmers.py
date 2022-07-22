from collections import defaultdict


def change(s):
    # '{'와 '}'를 제거한 뒤 ','단위로 잘라 리스트 반환
    s = s.lstrip('{')
    s = s.rstrip('}')
    return s.split(',')


def solution(s):
    answer = []
    # 중복 방지를 위한 used dict
    used = defaultdict(lambda: 0)
    # s를 '},'단위로 잘라 리스트로 변환 후 각 항목 마다 change 실행
    ns = list(map(change, s.split('},')))
    # 길이 순서로 오름차순 정렬
    # ns.sort(key=len)
    ns.sort(key=lambda x: len(x))

    # 순서에 맞춰 answer 배열에 값 추가
    for t in ns:
        for i in range(len(t)):
            if used[t[i]]:
                continue
            used[t[i]] = 1
            answer.append(int(t[i]))

    return answer


print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))
