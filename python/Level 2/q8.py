from itertools import combinations


def solution(relation):
    """후보키"""
    user_count = len(relation)
    attribute_list = [list(x) for x in zip(*relation)]
    candidate = list(range(0, len(attribute_list)))
    return calc(candidate, attribute_list, 1, 0, user_count)


def calc(candidate: list, user: list, count: int, counter: int, user_count: int):
    """재귀적 계산식"""
    comb = list(combinations(candidate, count))
    erase_target = []
    for val in comb:

        new_list = user[val[0]]
        for idx in range(1, len(val)):
            new_list = list(map(str.__add__, new_list, user[val[idx]]))

        if len(set(new_list)) == user_count:
            counter += 1
            erase_target += val

    if count >= len(candidate):
        return counter

    candidate = [val for val in candidate if val not in set(erase_target)]

    return calc(candidate, user, count + 1, counter, user_count)


if __name__ == "__main__":
    # A = [[1, 2, 3], [4, 5, 6]]
    # B = [list(x) for x in zip(*A)]  # without map
    # print(B)
    print(
        solution(
            [
                ["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"],
            ]
        )
    )
