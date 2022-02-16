from itertools import combinations


def solution(orders: list, course: list):
    """메뉴 리뉴얼"""
    ordered = {key: [] for key in course}
    menu_combination = {}

    for order in orders:
        temp = list(order)
        for count in course:
            for val in list(combinations(temp, count)):
                if not val in menu_combination:
                    menu_combination[val] = 0
                menu_combination[val] += 1
            # ordered[count] += list(combinations(temp, count))

    result = [key for key, val in menu_combination.items() if val >= 2]
    return result


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
