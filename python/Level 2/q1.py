def solution(record: list):
    """오픈채팅방"""
    answer = []
    user_id = {}

    for val in record:
        record_type = val.split(" ")
        if not record_type[1] in user_id:
            user_id[record_type[1]] = record_type[2]

        if record_type[0] == "Enter":
            answer.append([record_type[1], "님이 들어왔습니다."])
            user_id[record_type[1]] = record_type[2]
        elif record_type[0] == "Leave":
            answer.append([record_type[1], "님이 나갔습니다."])
        else:
            user_id[record_type[1]] = record_type[2]

    return [user_id[val[0]] + val[1] for val in answer]


if __name__ == "__main__":
    print(
        solution(
            [
                "Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan",
            ]
        )
    )
