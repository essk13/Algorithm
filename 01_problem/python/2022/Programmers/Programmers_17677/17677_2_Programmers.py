def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    # str1의 글자 쌍 저장 (소문자로 변환)
    for i in range(len(str1) - 1):
        a1, a2 = str1[i], str1[i + 1]
        # 알파벳인 경우만 저장
        if (65 <= ord(a1) <= 90 or 97 <= ord(a1) <= 122) \
                and (65 <= ord(a2) <= 90 or 97 <= ord(a2) <= 122):
            s1.append(a1.lower() + a2.lower())
    # str2의 글자 쌍 저장 (소문자로 변환)
    for i in range(len(str2) - 1):
        a1, a2 = str2[i], str2[i + 1]
        # 알파벳인 경우만 저장
        if (65 <= ord(a1) <= 90 or 97 <= ord(a1) <= 122) \
                and (65 <= ord(a2) <= 90 or 97 <= ord(a2) <= 122):
            s2.append(a1.lower() + a2.lower())

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

    answer = int(answer / union * 65536)
    return answer


print(solution('FRANCE', 'french'))
