def check(p):
    stack = []
    for i in range(len(p)):
        now = p[i]
        if now == '(':
            stack.append(now)
        else:
            if not stack:
                return 0
            if stack[-1] == '(':
                stack.pop()

    if stack:
        return 0
    else:
        return 1


def change(p):
    res = ''
    for i in range(1, len(p) - 1):
        now = p[i]
        if now == '(':
            res += ')'
        else:
            res += '('

    return res


def solution(p):
    # p가 ''인 경우 '' 반환
    if p == '':
        return ''

    answer = ''
    left = right = 0
    u = v = ''
    # 균형잡힌 괄호 문자열 u와 v로 분할
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left and left == right:
            u = ''.join(p[:left + right])
            v = ''.join(p[left + right:])
            break

    # u가 올바른 괄호 문자열인 경우 u에다 v의 재귀 결과 더하기
    if check(u):
        answer += u + solution(v)
    # u가 올바른 괄호 문자열이 아닌 경우
    # 1. 빈 문자열에 '(' 추가
    # 2. v의 재귀 결과 추가
    # 3. ')' 추가
    # 4. u의 처음과 끝 문자 제거 후 뒤집은 결과를 추가
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += change(u)
    return answer


print(solution('((()))'))
