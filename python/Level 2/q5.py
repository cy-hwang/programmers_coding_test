import itertools
from typing import List


def solution(statement):
    """수식 최대화"""
    number = []
    expression = []
    expression_type = ("+", "-", "*")
    idx = 0
    # 데이터 분할
    for key, value in enumerate(statement):
        if value in expression_type:
            number.append(int(statement[idx:key]))
            expression.append(statement[key : key + 1])
            idx = key + 1
    number.append(int(statement[idx:]))

    answer = 0
    for val in itertools.permutations(set(expression), len(set(expression))):
        answer = max(answer, abs(calc_statement(number, expression, val)))

    return answer


def calc_statement(number: List[int], expression: List[str], order: tuple) -> int:
    """연산자 우선순위에 따른 수식 계산"""
    temp_expression = expression
    temp_number = number
    for val in order:
        [temp_number, temp_expression] = calc_operation(
            temp_number, temp_expression, val
        )

    return temp_number[0]


def calc_operation(number: List[int], expression: List[str], operation: str) -> list:
    """특정 연산자에 따른 계산"""
    result = [[], []]
    temp = ""
    for key, val in enumerate(expression):
        if val == operation:
            temp = calculate(val, number[key] if temp == "" else temp, number[key + 1])
        else:
            result[0].append(number[key] if temp == "" else temp)
            result[1].append(val)
            temp = ""
    result[0].append(number[-1] if temp == "" else temp)

    return result


def calculate(operation: str, val1: int, val2: int) -> int:
    """operation에 따른 계산"""
    if operation == "+":
        return val1 + val2
    if operation == "-":
        return val1 - val2
    return val1 * val2


if __name__ == "__main__":
    print(
        solution(
            "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
        )
    )
