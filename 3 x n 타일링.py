"""
가로길이가 1일때, 경우의수는 0
가로길이가 2일때, 경우의수는 3
가로길이가 3일때, 경우의수는 0
가로길이가 4일때, 경우의수는 11
 f(n) = f(n-2) x 3 + f(n-4) x 2 + … + f(2) x 2 + 2
"""


def solution(n):
    if n % 2 != 0: return 0

    case_list = [0] * (n + 1)
    case_list[2] = 3

    for i in range(4, n + 1):
        if i % 2 == 1:
            case_list[i] = 0
            continue
        case_list[i] = (3 * case_list[i-2] + 2 * sum(case_list[:i-3]) + 2) % 1000000007
    return case_list[n]

print(solution(8))