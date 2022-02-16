def solution(n, lost, reserve):
    """t"""
    # 전체 학생
    gym_suit_list = [1] * n

    # 체육복 잃어버린 학생 제외
    for val in lost:
        gym_suit_list[val - 1] -= 1

    # 여벌 체육복 고려
    for val in reserve:
        gym_suit_list[val - 1] += 1

    # 앞에서부터 순환
    for key, val in enumerate(gym_suit_list):
        if val == 2:
            if key == 0:
                borrow_gym_suit(gym_suit_list, 1, key)

            elif key == len(gym_suit_list) - 1:
                borrow_gym_suit(gym_suit_list, -1, key)
            else:
                # 왼쪽에 안 빌려줬으면 오른쪽도 확인하라
                if not borrow_gym_suit(gym_suit_list, -1, key):
                    borrow_gym_suit(gym_suit_list, 1, key)

    answer = gym_suit_list.count(1) + gym_suit_list.count(2)
    return answer


def borrow_gym_suit(instance: list, receiver: int, donator: int):
    """보유하고 있는 체육복이 없다면 빌린다"""
    if instance[donator + receiver] == 0:
        instance[donator + receiver] += 1
        instance[donator] -= 1
        return True
    return False


if __name__ == "__main__":
    solution(5, [2, 4], [1, 3, 5])
