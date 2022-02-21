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
                    n["total"] = total

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

        answer.append(len([y for x in target for y in x if y >= int(grade)]))
        # answer.append(len([x.filter() x in target for y in x if y >= int(grade)]))
    return answer


def binary_search(arr, low, high, x):
    """이진 탐색 트리"""
    if x == 8:
        print("1")

    mid = (high + low) // 2  # ceiling

    if arr[mid] == x:
        return mid
    if low == mid:
        return low + 1 if arr[mid] < x else low

    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)

    else:
        return binary_search(arr, mid + 1, high, x)


if __name__ == "__main__":
    # print(
    #     solution(
    #         [
    #             "java backend junior pizza 180",
    #             "java backend junior pizza 160",
    #             "java backend junior pizza 170",
    #             "python frontend senior chicken 210",
    #             "python frontend senior chicken 150",
    #             "cpp backend senior pizza 260",
    #             "java backend junior chicken 80",
    #             "python backend senior chicken 50",
    #         ],
    #         [
    #             "cpp and - and senior and pizza 250",
    #             "- and backend and senior and - 150",
    #             "- and - and - and chicken 100",
    #             "- and - and - and - 150",
    #         ],
    #     )
    # )
    #       0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11
    test = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    for val in range(17):
        print(f"value: {val}  result: {binary_search(test, 0, len(test) - 1, val)}")
    # print(binary_search2(test, 9, 0, len(test) - 1))

"""
value: 0  result: 0
value: 1  result: 0
value: 2  result: 1
value: 3  result: 1
value: 4  result: 2
value: 5  result: 2
value: 6  result: 3
value: 7  result: 3
value: 8  result: 4 !
value: 9  result: 4
value: 10  result: 5
value: 11  result: 5
value: 12  result: 6
value: 13  result: 6
value: 14  result: 7
value: 15  result: 7
value: 16  result: 7
"""
