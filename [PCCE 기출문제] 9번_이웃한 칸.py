def solution(board, h, w):
    answer = 0
    if h - 1 >= 0 and board[h - 1][w] == board[h][w]:
        answer += 1

    if h + 1 < len(board) and board[h + 1][w] == board[h][w]:
        answer += 1

    if w - 1 >= 0 and board[h][w - 1] == board[h][w]:
        answer += 1

    if w + 1 < len(board[0]) and board[h][w + 1] == board[h][w]:
        answer += 1

    return answer
