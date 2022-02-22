def solution(info, query):
    """문제풀이"""
    language = ("cpp", "java", "python")
    part = ("backend", "frontend")
    career = ("junior", "senior")
    soul_food = ("chicken", "pizza")

    # Dict 객체 초기화
    user = {}
    for lang in language:
        user[lang] = {}
        for par in part:
            user[lang][par] = {}
            for car in career:
                user[lang][par][car] = {}
                for soul in soul_food:
                    user[lang][par][car][soul] = []

    # Dict 값 세팅
    for val in info:
        val = val.split(" ")
        user[val[0]][val[1]][val[2]][val[3]].append(int(val[4]))

    # Dict 정렬
    for l in user.values():
        for m in l.values():
            for n in m.values():
                for key, o in n.items():
                    o.sort()
                    total = len(o)
                    n[key] = {val: o.index(val) for val in o} if len(o) >= 1 else {}
                    n[key]["total"] = total

    # Dict 유저수 찾기
    answer = []
    for val in query:
        val = val.split(" and ")
        option = val[:-1] + [val[-1].split(" ")[0]]
        grade = val[-1].split(" ")[1]
        target = [user]
        for val2 in option:
            if val2 == "-":
                target = [y for x in target for key2, y in x.items()]
            else:
                target = [x[val2] for x in target]

        # 이진탐색트리를 통한 순위찾기
        temp = 0
        for val2 in target:
            grade_list = list(val2.keys())
            grade_list.remove("total")
            if len(grade_list) == 0:
                continue
            idx = binary_search(grade_list, 0, len(grade_list) - 1, int(grade))
            if idx >= len(grade_list):
                continue
            temp += val2["total"] - val2[grade_list[idx]]

        answer.append(temp)
    return answer


def binary_search(arr, low, high, x):
    """이진 탐색 트리"""
    mid = (high + low) // 2

    if arr[mid] == x:
        return mid

    if high == mid:
        return low + 1 if arr[mid] < x else low

    if arr[mid] > x:
        return binary_search(arr, low, max(mid - 1, low), x)

    return binary_search(arr, mid + 1, high, x)


if __name__ == "__main__":
    print(
        solution(
            [
                "java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50",
            ],
            [
                "java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150",
            ],
        )
    )
