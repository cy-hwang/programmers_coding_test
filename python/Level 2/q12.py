from datetime import datetime, timedelta
from math import ceil


def solution(fees: list, records: list):
    """주차요금 계산"""
    parking_time = []
    record = {}
    MAX_TIME = datetime.strptime("23:59", "%H:%M")

    # 사용자 별 데이터 형성
    for val in records:
        [time, num, _] = val.split(" ")
        if not num in record:
            record[num] = [time]
        else:
            record[num].append(time)

    # 사용자 별 주차시간 측정
    for user in sorted(record.keys()):
        timestamp = record[user]
        acc_time = 0
        for idx in range(0, len(timestamp), 2):
            out_time = (
                MAX_TIME
                if idx + 1 == len(timestamp)
                else datetime.strptime(timestamp[idx + 1], "%H:%M")
            )
            acc_time += int(
                (out_time - datetime.strptime(timestamp[idx], "%H:%M"))
                / timedelta(minutes=1)
            )
        parking_time.append(acc_time)

    # 사용자 별 주차요금 계산
    return [
        ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
        if time > fees[0]
        else fees[1]
        for time in parking_time
    ]


if __name__ == "__main__":
    print(
        solution(
            [180, 5000, 10, 600],
            [
                "05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT",
            ],
        )
    )
