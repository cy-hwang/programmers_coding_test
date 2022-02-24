from tabnanny import check


def solution(m, n, board):
    """t"""
    board = [list(val) for val in board]
    new_board = [list(x) for x in zip(*board)]
    print(new_board)

    check_match(m, n, new_board, 0)

    answer = 0

    return answer


def check_match(m, n, board: list, count: int):
    """일치 대상 제거"""
    # 일치대상 확인
    erase_target = []
    for col in range(m - 1):
        for row in range(n - 1):
            if set(board[col][row]) == set(
                [board[col + 1][row], board[col][row + 1], board[col + 1][row + 1]]
            ):
                erase_target.append((col, row))
                erase_target.append((col + 1, row))
                erase_target.append((col, row + 1))
                erase_target.append((col + 1, row + 1))

    erase_target = list(set(erase_target))
    if len(erase_target) == 0:
        return count

    # 일치 대상 제거
    for val in erase_target:
        board[val[0]][val[1]] = "0"

    for row in range(n):
        print(board)
        start_idx = -1
        end_idx = -1
        for col in range(m - 1, -1, -1):
            if board[col][row] == "0":
                start_idx = col
            else:
                end_idx = col

                if end_idx > start_idx:
                    temp = board[col][end_idx]
                    board[col][end_idx] = board[col][start_idx]
                    board[col][start_idx] = temp
                    start_idx = end_idx

    return check_match(m, n, board, count)


if __name__ == "__main__":
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
