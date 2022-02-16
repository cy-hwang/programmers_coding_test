def solution(s: str):
    """
    - 1 ≤ s의 길이 ≤ 50
    - s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
    - return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
    """
    mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for key, val in mapping.items():
        s = s.replace(key, str(val))
    answer = s
    return int(answer)
