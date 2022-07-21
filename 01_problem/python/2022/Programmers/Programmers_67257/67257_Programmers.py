def calculate(o, n1, n2):
    # 연산자 o에 따라 n1과 n2 연산
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    else:
        return n1 * n2


def step(exp, op):
    # 수삭 exp 중 연산자 op 만 수행한 뒤 새로운 연산자로 반환
    stack = []
    for j in range(len(exp)):
        if stack and stack[-1] == op:
            stack.pop()
            stack.append(calculate(op, stack.pop(), exp[j]))
        else:
            stack.append(exp[j])
    return stack


def solution(expression):
    answer = 0
    operators = ['+', '-', '*']
    exp = []
    num = ''
    # 연산자와 숫자로 분할
    for i in range(len(expression)):
        if expression[i] in operators:
            exp.append(int(num))
            exp.append(expression[i])
            num = ''
        else:
            num += expression[i]
    exp.append(int(num))

    # 연산자 우선 순위를 바꿔가며 절대값의 최대값 계산
    for st in range(3):
        edexp = step(exp, operators[st])
        for ed in range(3):
            if st == ed:
                continue
            thexp = step(edexp, operators[ed])
            for th in range(3):
                if th in (st, ed):
                    continue
                thexp = step(thexp, operators[th])
                answer = max(abs(thexp.pop()), answer)
    return answer


print(solution('100-200*300-500+20'))
