"""
직사각형 1개일때, 경우의수는 1
직사각형 2개일때, 경우의수는 2
직사각형 3개일때, 경우의수는 3
직사각형 4개일때, 경우의수는 5
"""


def solution(n):
    case_list = [0] * (n + 1)
    case_list[1] = 1
    case_list[2] = 2

    for i in range(3, n + 1):
        print(i)
        case_list[i] = case_list[i - 1] + case_list[i - 2]
    return case_list[n]

print(solution(11))