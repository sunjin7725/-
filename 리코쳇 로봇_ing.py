def go_left(board, now_r_coord):
    x, y = now_r_coord
    while x - 1 > 0 and board[y][x-1] != 'D':
        x -= 1
    return x, y


def go_right(board, now_r_coord):
    x, y = now_r_coord
    while x + 1 < len(board) and board[y][x+1] != 'D':
        x += 1
    return x, y


def go_up(board, now_r_coord):
    x, y = now_r_coord
    while y - 1 > 0 and board[y-1][x] != 'D':
        y -= 1
    return x, y


def go_down(board, now_r_coord):
    x, y = now_r_coord
    while y + 1 < len(board) and board[y+1][x] != 'D':
        y += 1
    return x, y


def find_route(board, now_r_coord, now_g_coord, visited, cnt=0):
    if now_r_coord == now_g_coord:
        return cnt
    else:
        left_x, left_y = go_left(board, now_r_coord)
        right_x, right_y = go_right(board, now_r_coord)
        up_x, up_y = go_up(board, now_r_coord)
        down_x, down_y = go_down(board, now_r_coord)
        if not visited[left_x][left_y]:
            visited[left_x][left_y] = True
            cnt += 1
            cnt = find_route(board, (left_x, left_y), now_g_coord, visited, cnt)
        if not visited[right_x][right_y]:
            visited[right_x][right_y] = True
            cnt += 1
            cnt = find_route(board, (right_x, right_y), now_g_coord, visited, cnt)
        if not visited[up_x][up_y]:
            visited[up_y][up_x] = True
            cnt += 1
            cnt = find_route(board, (up_x, up_y), now_g_coord, visited, cnt)
        if not visited[down_x][down_y]:
            visited[down_y][down_x] = True
            cnt += 1
            cnt = find_route(board, (down_x, down_y), now_g_coord, visited, cnt)
        return cnt


if __name__ == '__main__':
    board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
    board = list(map(list, board))

    now_r_coord = None
    now_g_coord = None
    visited = [[False for i in range(len(board[0]))] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'R':
                now_r_coord = (x, y)
                visited[y][x] = True
            elif board[y][x] == 'G':
                now_g_coord = (x, y)
                visited[y][x] = True
            elif board[y][x] == 'D':
                visited[y][x] = True
        if now_r_coord and now_g_coord:
            break

    print(find_route(board, now_r_coord, now_g_coord, visited))