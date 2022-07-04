def greatestCommonFactor(w, h):
    l, s = max(w, h), min(w, h)
    while 1:
        r = l % s
        if not r:
            return s
        l = s
        s = r
    return

# 프로그래머스
# def solution(w,h):
#     gcf = greatestCommonFactor(w, h)
#     answer = w * h - w - h + gcf
#     return answer

w, h = map(int, input())
gcf = greatestCommonFactor(w, h)
# 삭제된 정사각형의 수 = w + h - 최대공약수
ans = w * h - w - h + gcf
print(ans)
