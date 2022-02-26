import math


def solution(n: int, k: int):
    """소수 개수 구하기"""
    # 진수 변환
    changed = []
    while True:
        if n < k:
            changed.append(str(n))
            break
        changed.append(str(n % k))
        n = n // k
    changed.reverse()

    # 소수 대상 추출
    part = "".join(changed).split("0")

    # 소수 여부 판단
    answer = 0
    for val in [val for val in part if (val != "1" and val != "")]:
        is_prime = True
        # n ** 0.5 까지 수열을 통해 소수여부 판단
        for idx in range(2, int(math.pow(int(val), 0.5)) + 1):
            if int(val) % idx == 0:
                is_prime = False
                break
        # 2는 항상 소수
        if is_prime or val == "2":
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(110011, 10))
