def solution(lottos, win_nums):
    """solution

    Args:
        lottos ( list ): 사용자 선택 번호
        win_nums (list): 정답 번호

    Returns:
        _type_: 당첨 순위[최대, 최소]
    """
    unknown_value = lottos.count(0)
    right_count = 0
    for val in set(lottos):
        if val in win_nums:
            right_count += 1
    min_rank = 7 - right_count if right_count >= 2 else 6
    max_rank = 0
    if right_count == 0:
        if unknown_value == 0:
            max_rank = min_rank
        else:
            max_rank = min_rank - unknown_value + 1
    else:
        max_rank = min_rank - unknown_value

    answer = [max_rank, min_rank]
    return answer
