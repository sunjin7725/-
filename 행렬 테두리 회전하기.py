from copy import deepcopy


def rotate(array):
    max_x = len(array[0]) - 1
    max_y = len(array) - 1
    result = deepcopy(array)
    min_num = float('inf')

    result[0][1:] = array[0][0:-1]
    min_num = min(min_num, min(array[0][0:-1]))

    for i in range(max_y):
        result[i + 1][max_x] = array[i][max_x]
        min_num = min(min_num, array[i][max_x])

    result[max_y][0:-1] = array[max_y][1:]
    min_num = min(min_num, min(array[max_y][1:]))

    for i in range(max_y):
        result[i][0] = array[i + 1][0]
        min_num = min(min_num, array[i + 1][0])

    return result, min_num


if __name__ == '__main__':
    import numpy as np

    rows = 6
    columns = 6
    queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

    answer = []
    cnt = 0
    board = np.zeros((rows, columns))
    for y in range(rows):
        for x in range(columns):
            cnt += 1
            board[y][x] = cnt

    for x1, y1, x2, y2 in queries:
        test = board[x1-1:x2, y1-1:y2]
        board[x1-1:x2, y1-1:y2], min_num = rotate(board[x1-1:x2, y1-1:y2])
        answer.append(min_num)
