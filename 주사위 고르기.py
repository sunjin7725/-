from itertools import combinations, product
from collections import Counter, defaultdict

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

win = 0
draw = 0
lose = 0

a_dices = [dice[0], dice[1]]
b_dices = [dice[2], dice[3]]

a_cases = sorted(Counter(list(map(sum, product(dice[0], dice[1])))).items(), key=lambda x: x[0])
b_cases = sorted(Counter(list(map(sum, product(dice[2], dice[3])))).items(), key=lambda x: x[0])

a_num, a_cnt = a_cases.pop(0)
b_num, b_cnt = b_cases.pop(0)
while a_cases and b_cases:
    if a_cnt == 0:
        a_num, a_cnt = a_cases.pop(0)
    if b_cnt == 0:
        b_num, b_cnt = b_cases.pop(0)

    if a_num > b_num:
        if a_cnt > b_cnt:
            win += b_cnt
            a_cnt -= b_cnt
            b_cnt = 0
        elif a_cnt < b_cnt:
            win += a_cnt
            b_cnt -= a_cnt
            a_cnt = 0
        else:
            win += a_cnt
            a_cnt = 0
            b_cnt = 0
    elif a_num < b_num:
        if a_cnt > b_cnt:
            lose += b_cnt
            a_cnt -= b_cnt
            b_cnt = 0
        elif a_cnt < b_cnt:
            lose += a_cnt
            b_cnt -= a_cnt
            a_cnt = 0
        else:
            lose += a_cnt
            a_cnt = 0
            b_cnt = 0
    else:
        if a_cnt > b_cnt:
            draw += b_cnt
            a_cnt -= b_cnt
            b_cnt = 0
        elif a_cnt < b_cnt:
            draw += a_cnt
            b_cnt -= a_cnt
            a_cnt = 0
        else:
            draw += a_cnt
            a_cnt = 0
            b_cnt = 0
