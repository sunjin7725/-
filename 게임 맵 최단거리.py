import numpy as np
from collections import deque

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]


def solution(maps):
    m, n = np.array(maps).shape
    path = np.zeros((m, n))
    path[0][0] = 1
    visited_list = deque([(0, 0, 1)])

    while visited_list:
        if path[m-1][n-1] != 0: break
        now_x, now_y, now_cnt = visited_list.popleft()
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if not abs(i + j) == 1: continue
                if now_x + i < 0 or now_x + i >= m or now_y + j < 0 or now_y + j >= n:
                    continue
                if path[now_x + i][now_y + j] != 0: continue
                if maps[now_x + i][now_y + j] == 1:
                    path[now_x + i][now_y + j] = now_cnt + 1
                    visited_list.append((now_x + i, now_y + j, now_cnt + 1))
    if path[m-1][n-1] == 0: return -1
    return path[m-1][n-1]









min_path_count = float('inf')


# 시간초과당함
def find_map(maps):
    m, n = np.array(maps).shape
    path = np.zeros((m, n))
    path[0][0] = 1
    m -= 1
    n -= 1

    def dfs(now=(0, 0), path_count=1):
        global min_path_count
        if now == (m, n):
            min_path_count = path_count
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if not abs(i + j) == 1: continue
                if now[0] + i < 0 or now[0] + i > m or now[1] + j < 0 or now[1] + j > n:
                    continue
                if path[now[0] + i][now[1] + j] == 1: continue
                if path_count + 1 > min_path_count: continue
                if maps[now[0] + i][now[1] + j] == 1:
                    path[now[0] + i][now[1] + j] = 1
                    path_count += 1
                    dfs((now[0] + i, now[1] + j), path_count)
                    path[now[0] + i][now[1] + j] = 0
                    path_count -= 1
    dfs()
    return min_path_count
