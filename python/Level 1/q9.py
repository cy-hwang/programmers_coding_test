def solution(id_list: list, report: list, k: int):
    """신고 결과 받기"""
    # 유저 별 신고된 횟수 카운트
    reporter = {val: [] for val in id_list}
    report = list(set(report))
    for val in report:
        split = val.split(" ")
        reporter[split[1]].append(split[0])

    # 차단 대상 리스트업
    block_user = [key for key, val in reporter.items() if len(val) >= k]

    # 유저 별 신고횟수 수신
    answer = [0] * len(id_list)  # 유저 별 처리결과 횟수 리스트 초기화
    for val in block_user:
        for val2 in reporter[val]:
            answer[id_list.index(val2)] += 1

    return answer


if __name__ == "__main__":
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
