import numpy as np
from collections import deque

info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
lion_case = [0,2,2,0,1,0,0,0,0,0,0]

def get_lion_point(lion_score_board, apeach_score_board):
    _sum = 0
    for idx, lion_score in enumerate(lion_score_board):
        if lion_score > apeach_score_board[idx]:
            _sum += 10-idx
        elif lion_score == 0 and apeach_score_board[idx] == 0:
            continue
        else:
            _sum -= 10-idx
    return _sum


def get_lion_win_case(info):
    lion_score_list = deque([(10, [])])
    win_list = []
    while lion_score_list:
        tmp_point, lion_case = lion_score_list.popleft()

        if sum(lion_case) == sum(info) or tmp_point == -1:
            if len(lion_case) != 11:
                lion_case += [0] * (11 - len(lion_case))

            lion_point = get_lion_point(lion_case, info)
            if lion_point > 0:
                win_list.append((lion_case, lion_point))

        else:
            case = lion_case.copy()
            if sum(case) + info[10-tmp_point] + 1 > sum(info):
                case.append(sum(info) - sum(case))
            else:
                case.append(info[10-tmp_point] + 1)
            lion_score_list.append((tmp_point - 1, case))

            case = lion_case.copy()
            case.append(0)
            lion_score_list.append((tmp_point - 1, case))
    return win_list

win_list = get_lion_win_case(info)
