from itertools import combinations


def solution(relation):
    """후보키"""
    # [[100, 200, ...], [ryan, apeach, ...], ...]
    attribute_list = [list(x) for x in zip(*relation)]

    # 후보키 조합 리스트업
    combination = []
    attribute_length = len(attribute_list)
    for val in range(1, attribute_length + 1):
        combination.extend(list(combinations(range(attribute_length), val)))

    return check_candidate(combination, attribute_list, 0, len(relation))


def check_candidate(candidate: list, user: list, count: int, num_key: int):
    """재귀적 계산식"""
    check_all = True
    candidate_key = tuple()
    for val in candidate:
        # [('a', '1'), ('b', '1'), ...]
        new_list = [tuple([user[j][i] for j in val]) for i in range(num_key)]

        # 후보키여부 확인
        if len(set(new_list)) == num_key:
            check_all = False
            candidate_key = val
            break

    if not check_all:
        count += 1
        # 후보키가 포함된 조합 제거
        candidate = [
            val for val in candidate if not set(candidate_key).issubset(set(val))
        ]
        return check_candidate(candidate, user, count, num_key)

    return count


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
