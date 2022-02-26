def solution(n: int, k: int):
    """소수 개수 구하기"""
    # 진수 변환
    changed = ""
    while n:
        changed += str(n % k)
        n //= k

    changed = changed[::-1]

    # 소수 대상 추출
    part = [val for val in changed.split("0") if (val != "1" and val != "")]

    # 소수 여부 판단
    answer = 0
    for val in part:
        is_prime = True
        # n ** 0.5 까지 수열을 통해 소수여부 판단
        i = 2
        while i * i <= int(val):
            if int(val) % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(437674, 3))
