n = 4

def cross_line_check(now_x, queen_list):
    for idx, value in enumerate(queen_list):
        if abs(idx - len(queen_list)) == abs(value - now_x):
            return False
    return True


def solution(n):
    result = []
    available_x = set(range(n))

    def dfs(queen_list=[]):
        if len(queen_list) == n:
            result.append(queen_list.copy())
        for x in list(available_x - set(queen_list)):
            if cross_line_check(x, queen_list):
                queen_list.append(x)
                dfs(queen_list)
                queen_list.pop()
    dfs()
    return len(result)
print(solution(12))


""" 시간초과 
def cross_line_check(coord, queen_list):
    for i in queen_list:
        if abs(i[0] - coord[0]) == abs(i[1] - coord[1]):
            return False
    return True


def solution(n):
    result = []

    def dfs(now_queen=[]):
        if len(now_queen) == n:
            result.append(now_queen.copy())

        if len(now_queen) == 0:
            start_y = 0
            available_x = list(set(range(0, n)))
        else:
            start_y = now_queen[-1][1] + 1
            available_x = list(set(range(0, n)) - set([i[0] for i in now_queen] +
                                                      [now_queen[-1][0] + 1, now_queen[-1][0] - 1]))
        if len(now_queen) >= 2:
            if abs(now_queen[-2][1] - now_queen[-1][1]) > 1: return
        for j in range(start_y, n):
            for i in available_x:
                if cross_line_check((i, j), now_queen):
                    now_queen.append((i, j))
                    dfs(now_queen)
                    now_queen.pop()
    dfs()
    return len(result)

print(solution(10))
"""