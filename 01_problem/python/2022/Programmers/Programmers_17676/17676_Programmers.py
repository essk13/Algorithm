def getTime(T):
    h, m, s = T[0], T[1], T[2]
    m += h * 60
    s += m * 60
    return s


def solution(lines):
    end = []
    res = [0] * len(lines)
    for idx in range(len(lines)):
        line = lines[idx].split()
        ed = getTime(list(map(float, line[1].split(':'))))
        st = round(ed - float(line[2].strip('s')) + 0.001, 4)
        end.append(ed)
        for i in range(len(end)):
            if st < end[i] + 1 and end[i] <= ed:
                res[i] += 1

    answer = max(res)
    return answer


l = input().split(',')
print(solution(l))
