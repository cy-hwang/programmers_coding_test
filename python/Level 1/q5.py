def solution(board, moves):
    """
    크레인 인형뽑기 문제
    """
    # 보드를 라인별로 재정렬
    transpose_board = [list(x) for x in zip(*board)]

    stack = []
    answer = 0
    for move in moves:
        for idx, val in enumerate(transpose_board[move - 1]):
            if val != 0:
                # 인형 옮기기
                transpose_board[move - 1][idx] = 0
                stack.append(val)

                # 인형이 같으면 터뜨리기
                if len(stack) >= 2 and stack[-2:-1] == stack[-1:]:
                    stack = stack[0:-2]
                    answer += 2
                break

    return answer


if __name__ == "__main__":
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
