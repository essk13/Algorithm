from collections import defaultdict


def solution(clothes):
    '''
    옷의 개수에 따른 조합 식
    ex) 4가지 종류와 각각 a, b, c, d개의 의상인 경우
    (a + b + c + d) + (ab + ac + ad + bc + bd + cd) + (abc + abd + acd + bcd) + (abcd)
    =>  (x + a) * (x + b) * (x + c) * (x + d)
        = x^4 + (a + b + c + d)x^3 + (ab + ac + ad + bc + bd + cd)x^2 + (abc + abd + acd + bcd)x + (abcd)
        <x = 1 인 경우>
        1 + (a + b + c + d) + (ab + ac + ad + bc + bd + cd) + (abc + abd + acd + bcd) + (abcd)
    즉, (1 + a) * (1 + b) * (1 + c) * (1 + d) - 1 로 정의 가능
    '''
    answer = 1
    clist = defaultdict(lambda: 0)
    for c in clothes:
        clist[c[1]] += 1

    for c in clist:
        answer *= clist[c] + 1

    return answer - 1
