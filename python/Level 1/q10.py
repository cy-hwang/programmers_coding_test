from functools import cmp_to_key


def solution(N: int, stages: list):
    """실패율 구하기"""
    # 각 스테이지 유저 수
    stage_user = [0] * (N + 1)
    for stage in stages:
        stage_user[stage - 1] += 1

    remaining_user = len(stages)
    # 실패율 계산
    failure = [[]] * N
    for stage in range(N):
        failure[stage] = (
            [stage + 1, 0]
            if remaining_user == 0
            else [stage + 1, stage_user[stage] / remaining_user]
        )
        remaining_user -= stage_user[stage]

    # 실패율 별 정렬
    return [val[0] for val in sorted(failure, key=cmp_to_key(sort_rule))]


def sort_rule(x, y):
    """실패율에 따른 정렬"""
    return 1 if x[1] <= y[1] else -1


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
