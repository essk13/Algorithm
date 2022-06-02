# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

# [제약 사항]
# N 과 M은 3 이상 20 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 제공된 N, M개의 숫자를 이용하여 Ai, Bj를 생성하는 함수 제작
# 짧은 숫자열의 빈 자리는 'none' 추가
def row():
    row_size = list(map(int, input().split()))
    number_i = list(map(int, input().split()))
    number_j = list(map(int, input().split()))
    Ai = []
    Bj = []
    if row_size[0] > row_size[1]:
        for x in range(row_size[0]):
            Ai.append('none')
            Bj.append('none')
    else:
        for y in range(row_size[1]):
            Ai.append('none')
            Bj.append('none')

    for i in range(row_size[0]):
        Ai[i] = number_i[i]
    for j in range(row_size[1]):
        Bj[j] = number_j[j]
    
    return Ai, Bj
# 두 숫자열 중 짧은 숫자열을 이동시키며 각 자릿수의 곱의 합이 가장 큰 값을 추출하는 함수 제작
def max_multiply(rows):
    Ai = rows[0]
    Bj = rows[1]

    max_sum = 0
    sum_multiply = 0
    Ai_2 = ['none']
    Bj_2 = ['none']
    for num in range(len(Ai)):
        for n in range(len(Ai)):
            # 짧은 숫자열의 값이 'none'인 경우는 계산 미실시
            if type(Ai[n]) == str or type(Bj[n]) == str:
                pass
            else:
                sum_multiply += (Ai[n] * Bj[n])
        if sum_multiply > max_sum:
            max_sum = sum_multiply

        Ai_2 = ['none']
        Bj_2 = ['none']
        # 짧은 숫자열의 숫자값 위치 한칸 이동
        sum_multiply = 0
        if Ai[-1] == 'none':
            Ai.pop(-1)
            for i in Ai:
                Ai_2.append(i)
            Ai = Ai_2
        elif Bj[-1] == 'none':
            Bj.pop(-1)
            for j in Bj:
                Bj_2.append(j)
            Bj = Bj_2
        else:
            break

    return max_sum
# 곱의 합 최대값을 전달하는 함수 제작
def print_maxmultiply():
    rows = row()
    ret_max = max_multiply(rows)
    return ret_max

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {print_maxmultiply()}')