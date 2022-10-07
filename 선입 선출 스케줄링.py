n = 6
cores = [1, 2, 3]


def solution(n, cores):
    n -= len(cores)
    left = min(cores)
    right = max(cores) * n
    time = 0
    while left <= right:
        mid = (left + right) // 2
        cores_cnt = sum(list(map(lambda x: mid//x, cores)))
        if cores_cnt >= n:
            time = mid
            right = mid - 1
        elif cores_cnt < n:
            left = mid + 1
    n -= sum(list(map(lambda x: (time-1)//x, cores)))
    for idx, core in enumerate(cores):
        if time % core == 0:
            n -= 1
            if n == 0:
                return idx + 1

print(solution(n, cores))


""" 시간초과 당함
class Core:
    def __init__(self, core_num, process_time):
        self.core_num = core_num
        self.process_time = process_time

    def can_process(self, ticking_time):
        if ticking_time == 0: return True
        if ticking_time % self.process_time == 0:
            return True
        else: return False


ticking_time = 0
answer = 0
core_list = [Core(idx+1, process_time) for idx, process_time in enumerate(cores)]

while n > 0:
    for core in core_list:
        if core.can_process(ticking_time):
            n -= 1
            answer = core.core_num
        if n == 0: break
    ticking_time += 1

print(answer)
"""