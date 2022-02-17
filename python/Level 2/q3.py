def solution(p: str):
    """괄호 변환"""

    if p == "":
        return p

    [u, v] = step2(p)
    if check_right_text(u):
        return u + solution(v)
    else:
        return (
            "("
            + solution(v)
            + ")"
            + "".join(["(" if val == ")" else ")" for val in list(u[1:-1])])
        )


def step2(text: str):
    """split uv"""
    idx = 0
    count_left = 0
    count_right = 0
    for val in text:
        if val == "(":
            count_left += 1
        else:
            count_right += 1
        idx += 1
        if count_left == count_right:
            break
    return [text[:idx], text[idx:]]


def check_right_text(text: str):
    """올바른 괄호 문자열 체크"""
    idx = 0
    is_right = True
    for val in text:
        if val == "(":
            idx += 1
        else:
            idx -= 1
        if idx < 0:
            is_right = False
            break
    return is_right


if __name__ == "__main__":
    print(solution("()))((()"))

"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""
