import ast
from functools import cmp_to_key


def solution(s):
    """튜플"""
    answer = []
    value = ast.literal_eval(s.replace("{", "[").replace("}", "]"))
    value = sorted(value, key=cmp_to_key(lambda x, y: -1 if len(x) <= len(y) else 1))

    temp = set({})
    for val in value:
        answer.append(list(set(val) - temp)[0])
        temp = set(val)

    return answer


if __name__ == "__main__":
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
