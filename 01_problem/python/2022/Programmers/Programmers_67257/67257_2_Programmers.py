def solution(expression):
    answer = 0
    operators = ['+', '-', '*']
    # 연산자 우선순위를 사전에 정의
    sequence = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
    for st, ed, th in sequence:
        nexp = []
        # 마지막으로 계산할 연산자를 기준으로 split하여 리스트 생성
        for exp in expression.split(operators[st]):
            # 위 리스트의 각 항목을 두번째로 계산할 연산자를 기준으로 split한 뒤 괄호로 묶어서 리스트 생성
            now = [f'({i})' for i in exp.split(operators[ed])]
            # 방금 만든 리스트를 두번째로 계산할 연산자로 join하여 문자열로 변환 후 괄호로 묶어서 nexp 배열에 추가
            nexp.append(f'({operators[ed].join(now)})')
        # nexp 배열을 마지막으로 계산할 연산자로 join하여 문자열로 변환 후 계산 및 max 비교
        # 먼저 계산할 연산자부터 괄호로 순차적으로 묶여있음으로 eval 계산 시 지정한 순서로 연산됨
        answer = max(abs(eval(operators[st].join(nexp))), answer)
    return answer


print(solution('100-200*300-500+20'))
