# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
# 다음과 같은 수 분포가 있으면,
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 최빈수는 8이 된다.
# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# [제약 사항]
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
 
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

def mode_score():
    scores = list(map(int, input().split()))
    set_scores = set(scores)
    set_scores = list(scores)
    set_scores = sorted(set_scores)
    mode_score = 0
    cnt_score = 0
    for score in set_scores:
        if scores.count(score) >= cnt_score:
            cnt_score = scores.count(score)
            mode_score = score
            
    return mode_score

case_num = int(input())

for case in range(case_num):
    case_number = int(input())
    print(f'#{case_number} {mode_score()}')