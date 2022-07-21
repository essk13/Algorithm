# 풀이1: 아스키 코드

def check(s):
    res = s
    # 대문자인 경우
    if 97 <= s <= 122:
        res -= 32
    # 소문자인 경우
    elif 65 <= s <= 90:
        pass
    # 숫자 또는 특수 문자인 경우
    else:
        return 0
    return res


def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    # str1의 글자 쌍 저장
    for i in range(len(str1) - 1):
        a1, a2 = ord(str1[i]), ord(str1[i + 1])
        a1 = check(a1)
        a2 = check(a2)
        # 숫자나 특수 문자가 아닌 경우만 저장
        if a1 and a2:
            s1.append(str(a1) + str(a2))
    # str2의 글자 쌍 저장
    for j in range(len(str2) - 1):
        a1, a2 = ord(str2[j]), ord(str2[j + 1])
        a1 = check(a1)
        a2 = check(a2)
        # 숫자나 특수 문자가 아닌 경우만 저장
        if a1 and a2:
            s2.append(str(a1) + str(a2))

    # 교집합 수 계산
    used = [0] * len(s2)
    for i in range(len(s1)):
        pair = s1[i]
        for j in range(len(s2)):
            # 중복 처리 방지를 위한 used 배열 사용
            if used[j]:
                continue
            if pair == s2[j]:
                used[j] = 1
                answer += 1
                break

    # 합집합 수 계산
    union = len(s1) + len(s2) - answer
    if not union:
        return 65536

    answer /= union
    answer = int(answer * 65536)
    return answer


print(solution('FRANCE', 'french'))
