from itertools import combinations


def solution(relation):
    """후보키"""
    # [[100, 200, ...], [ryan, apeach, ...], ...]
    attribute_list = [list(x) for x in zip(*relation)]

    return calc(list(range(len(attribute_list))), attribute_list, 1, 0, len(relation))


def calc(candidate: list, user: list, count: int, counter: int, user_count: int):
    """재귀적 계산식"""
    # candidate에 대해 count 개수에 해당하는 조합 리스트
    comb = list(combinations(candidate, count))
    erase_target = []
    for val in comb:

        new_list = user[val[0]]
        for idx in range(1, len(val)):
            new_list = list(map(str.__add__, new_list, user[val[idx]]))

        if len(set(new_list)) == user_count:
            print(val)
            counter += 1
            erase_target += val

    if count >= len(candidate):
        return counter

    candidate = [val for val in candidate if val not in set(erase_target)]

    return calc(candidate, user, count + 1, counter, user_count)


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
