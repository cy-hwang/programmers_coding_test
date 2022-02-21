import re
from itertools import permutations


def solution(expression):
    """t"""
    # 1
    op = [x for x in ["*", "+", "-"] if x in expression]
    ex = re.split(r"(\D)", expression)

    # 2
    a = []
    for x in [list(y) for y in permutations(op)]:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp - 1] = calculate(_ex[tmp], _ex[tmp - 1], _ex[tmp + 1])
                _ex = _ex[:tmp] + _ex[tmp + 2 :]
        a.append(_ex[-1])

    # 3
    return max(abs(int(x)) for x in a)


def calculate(operation: str, val1: str, val2: str) -> str:
    """operation에 따른 계산"""
    if operation == "+":
        return str(int(val1) + int(val2))
    if operation == "-":
        return str(int(val1) - int(val2))
    return str(int(val1) * int(val2))


if __name__ == "__main__":
    print(
        solution(
            "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
        )
    )
