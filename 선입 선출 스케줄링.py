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

def reform_to_result_format(t_list):
    result_form = []
    for idx, t in enumerate(t_list):
        if idx == len(t_list)-1:
            result_form.extend(t)
        else:
            result_form.append(t[0])
    return result_form


def is_available(bf_t, af_t):
    if bf_t[-2] == af_t[0]:
        return True
    else:
        return False


def solution(tickets):
    num_tickets = len(tickets)
    append_check = -1
    result_visit_list = []
    start_list = [t for t in tickets if t[0] == "ICN"]
    for t in start_list:
        need_visit = [t+[0]]
        used_tickets_node, used_tickets = [], []
        while need_visit:
            current_tickets = need_visit.pop()
            if current_tickets[:-1] != len(used_tickets)-1:
                used_tickets_node, used_tickets = used_tickets_node[:current_tickets[-1]], used_tickets[:current_tickets[-1]]
            used_tickets_node.append(current_tickets)
            used_tickets.append(current_tickets[:-1])
            if len(used_tickets) == num_tickets:
                result_visit_list.append(reform_to_result_format(used_tickets))
                if sorted(used_tickets) == sorted(tickets):
                    if need_visit:
                        current_tickets = need_visit.pop()
                        used_tickets_node, used_tickets = used_tickets_node[:current_tickets[-1]], used_tickets[:current_tickets[-1]]
                        used_tickets_node.append(current_tickets)
                        used_tickets.append(current_tickets[:-1])
                    else:
                        break
            for l_t in tickets:
                if is_available(current_tickets, l_t) and l_t not in used_tickets:
                    need_visit.append(l_t + [len(used_tickets)])
                    append_check += 1
            if append_check == -1:
                continue
            append_check = -1
    return min(result_visit_list)


cc = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])




