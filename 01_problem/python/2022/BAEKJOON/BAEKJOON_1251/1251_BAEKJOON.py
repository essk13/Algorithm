def change(result, t, min_ord):
    '''
    :param result: 지금까지 결과
    :param t: 나눠진 단어 수
    :param min_ord: 남은 알파벳 중 가장 작은 ord
    '''

    # 3개의 단어가 된 경우 최종 결과가 가장 작은 값인지 판별
    if t == 3:
        result += my_reverse(word[len(result):])
        if result < answer[0]:
            answer[0] = result
        return

    # 반복문을 이용하여 단어 자르기
    # [최종 3개가 될 수 있도록 고려하여 마지막 부분의 알파벳 남겨두기]
    for j in range(len(result), len(word) - 3 + t):
        if ord(word[j]) == min_ord:
            change(result + my_reverse(word[len(result):j+1]), t + 1, min(ords[j+1:len(word)-2+t]))
    return


def my_reverse(alphabets):
    # .reverse()와 같은 기능
    result = ''
    stack = []
    for a in range(len(alphabets)):
        stack.append(alphabets[a])
    while stack:
        result += stack.pop()
    return result


word = input()
answer = ['']
ords = [0] * len(word)
for i in range(len(word)):
    ords[i] = ord(word[i])
    answer[0] += 'z'

change('', 1, min(ords[:len(word)-2]))
print(answer[0])
