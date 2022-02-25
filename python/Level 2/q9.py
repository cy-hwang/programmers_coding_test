def solution(m, n, board):
    """프렌즈4블록"""
    board = [list(val) for val in board]
    n_board = [list(x) for x in zip(*board)]

    answer = 0

    while True:
        # 일치대상 확인
        erase_target = []
        for col in range(n - 1):
            for row in range(m - 1):
                if n_board[col][row] != "0" and set(n_board[col][row]) == set(
                    [
                        n_board[col + 1][row],
                        n_board[col][row + 1],
                        n_board[col + 1][row + 1],
                    ]
                ):
                    erase_target += [
                        (col, row),
                        (col + 1, row),
                        (col, row + 1),
                        (col + 1, row + 1),
                    ]

        erase_target = list(set(erase_target))
        if len(erase_target) == 0:
            break

        answer += len(erase_target)

        # 일치 대상 제거
        for val in erase_target:
            n_board[val[0]][val[1]] = "0"

        # 빈칸 채우기
        for key, col in enumerate(n_board):
            non_zero = [val for val in col if val != "0"]
            n_board[key] = ["0"] * (len(col) - len(non_zero)) + non_zero

    return answer


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
