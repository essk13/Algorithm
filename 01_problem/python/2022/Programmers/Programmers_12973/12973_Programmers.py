def solution(s):
    stack = []
    for alphabet in s:
        if not stack or stack[-1] != alphabet:
            stack.append(alphabet)
        elif stack[-1] == alphabet:
            stack.pop()

    answer = 1
    if stack:
        answer = 0

    return answer


S = input()
print(solution(S))
