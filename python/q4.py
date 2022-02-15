LOCATION = {
    "1": [0, 3],
    "2": [1, 3],
    "3": [2, 3],
    "4": [0, 2],
    "5": [1, 2],
    "6": [2, 2],
    "7": [0, 1],
    "8": [1, 1],
    "9": [2, 1],
    "*": [0, 0],
    "0": [1, 0],
    "#": [2, 0],
}

LEFT_ONLY = ("1", "4", "7")
RIGHT_ONLY = ("3", "6", "9")


def cal_distance(num1: str, num2: str):
    """_summary_"""
    pos1 = LOCATION[num1]
    pos2 = LOCATION[num2]
    # 유클리드 거리로 계산 시 문제 발생
    # return pow(pow(pos1[0] - pos2[0], 2) + pow(pos1[1] - pos2[1], 2), 0.5)

    # 맨하탄 거리로 계산해야 함
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def solution(numbers, hand):
    """_summary_

    Args:
        numbers (_type_): _description_
        hand (_type_): _description_

    Returns:
        _type_: _description_
    """
    cur_left = "*"
    cur_right = "#"
    answer = ""

    for val in numbers:
        val = str(val)
        if val in LEFT_ONLY:
            cur_left = val
            answer += "L"
        elif val in RIGHT_ONLY:
            cur_right = val
            answer += "R"
        else:
            distance_left = cal_distance(val, cur_left)
            distance_right = cal_distance(val, cur_right)
            if distance_left < distance_right:
                cur_left = val
                answer += "L"
            elif distance_left > distance_right:
                cur_right = val
                answer += "R"
            else:
                if hand == "left":
                    cur_left = val
                    answer += "L"
                else:
                    cur_right = val
                    answer += "R"

    return answer


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
