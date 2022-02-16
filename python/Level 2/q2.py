from itertools import combinations


def solution(orders: list, course: list):
    """메뉴 리뉴얼 -> 메뉴의 조합으로 풀이"""

    menu_combination = {}

    # orders의 조합 별 등장 횟수
    for order in orders:
        temp = list(order)
        for count in course:
            for val in list(combinations(temp, count)):
                combination = "".join(sorted(val))
                if not combination in menu_combination:
                    menu_combination[combination] = 0
                menu_combination[combination] += 1

    # 메뉴 개수(2, 3, 4) 별 선택 조합 주문
    menu = {}
    for key, val in menu_combination.items():
        # 중복 주문이 아니면 제거
        if val == 1:
            continue
        # 만들고자 하는 개수가 아니면 제거
        if len(key) not in course:
            continue
        
        if len(key) not in menu:
            menu[len(key)] = [val, [key]]
            continue
        
        if val > menu[len(key)][0]:
            menu[len(key)] = [val, [key]]
        elif val == menu[len(key)][0]:
            menu[len(key)][1].append(key)
    
    result = []
    for val in menu.values():
        result += val[1]

    return sorted(result)

if __name__ == "__main__":
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
