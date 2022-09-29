"""
1 -> 1
2 -> 2
3 -> 3
4 -> 5 = 3칸뛸경우 + 2칸뛸경우
"""

import numpy as np


def solution(n):
    if n < 3:
        return n
    d = [0]*(n+1)
    d [1] = 1
    d [2] = 2
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567

print(solution(1))




def jump(n):
    result = []

    def bfs(n, _result=[]):
        if n == 0:
            result.append(_result.copy())
        elif n > 0:
            for i in [1, 2]:
                _result.append(i)
                bfs(n - i, _result)
                _result.pop()
    bfs(n)
    return result
