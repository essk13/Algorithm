def solution(alp, cop, problems):
    '''
    :param alp: 알고력
    :param cop: 코딩력
    :param problems: 문제 리스트
    :return: 모든 문제를 풀 수 있는 알고력과 코딩력을 기르는데 걸리는 최소시간
    '''

    # 목표 apl와 cop 확인
    max_alp = max_cop = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    # 현재 alp와 cop가 최대값보다 작거나 같도록 설정
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # 시작 dp 0으로 설정
    dp = [[151] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 1시간을 사용하여 alp 또는 cop를 1 올리는 경우
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            # 문제 풀이를 통해서 alp, cop를 올리는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                nxt_alp, nxt_cop = i + alp_rwd, j + cop_rwd

                # 다음 alp와 cop가 최대치를 넘어서는 경우 최대값으로 설정
                if nxt_alp > max_alp:
                    nxt_alp = max_alp
                if nxt_cop > max_cop:
                    nxt_cop = max_cop

                dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j] + cost)

    return dp[-1][-1]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
