from collections import deque
from itertools import combinations


def solution(relation):
    """후보키"""
    n_row = len(relation)
    n_col = len(relation[0])

    # 후보키 대상 조합 추출
    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    # 대상 중 후보키 추출
    for keys in candidates:
        # [('a', '1'), ('b', '1'), ...]
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    # 후보키 중 부분집합이 존재하는 대상 제거
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)


if __name__ == "__main__":
    print(
        solution(
            [
                ["a", "1", "aaa", "c", "ng"],
                ["b", "1", "bbb", "c", "g"],
                ["c", "1", "aaa", "d", "ng"],
                ["d", "2", "bbb", "d", "ng"],
            ]
        )
    )
