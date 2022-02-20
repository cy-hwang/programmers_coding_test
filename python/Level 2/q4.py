def solution(places):
    """거리두기 확인하기"""
    answer = []
    for room in places:
        answer.append(check_room_status(room))

    return answer


def check_room_status(room: list):
    """거리두기 여부 체크"""

    # 응시자 위치 생성
    user_position = [
        (key, key2)
        for key, val in enumerate(room)
        for key2, val2 in enumerate(list(val))
        if val2 == "P"
    ]

    # 응시자 중 거리가 2 이하인 응시자들 확인
    near_user = []
    for idx, val in enumerate(user_position):
        for idx2 in range(idx + 1, len(user_position)):
            if is_close(user_position[idx], user_position[idx2]):
                near_user.append((user_position[idx], user_position[idx2]))

    if len(near_user) == 0:
        return 1

    for val in near_user:
        if abs(val[0][0] - val[1][0]) == 2:
            x = min(val[0][0], val[1][0]) + 1
            if room[x][val[0][1]] != "X":
                return 0
        elif abs(val[0][1] - val[1][1]) == 2:
            y = min(val[0][1], val[1][1]) + 1
            if room[val[0][0]][y] != "X":
                return 0
        else:
            if room[val[0][0]][val[1][1]] != "X" or room[val[1][0]][val[0][1]] != "X":
                return 0

    return 1


def is_close(loc1, loc2):
    """두 유저가 거리두기를 지키고 있는지 확인"""
    if (abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])) <= 2:
        return True
    return False


if __name__ == "__main__":
    print(
        solution(
            [
                ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
            ]
        )
    )

"""    
    0   0   1   0   0
    0   1   1   1   0
    1   1   x   1   1
    0   1   1   1   0
    0   0   1   0   0
"""
