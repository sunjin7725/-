def solution(tickets):
    visit = [1] * len(tickets)
    stack = [('ICN', ['ICN'], visit)]
    answer = []

    while stack:
        start, lst, visit = stack.pop(0)
        if sum(visit) == 0:
            answer.append(lst)

        else:
            for idx, ticket in enumerate(tickets):
                ticket_start, ticket_end = ticket
                if visit[idx] != 0 and start == ticket_start:
                    copy_visit = visit.copy()
                    copy_lst = lst.copy()
                    copy_visit[idx] = 0
                    copy_lst.append(ticket_end)
                    stack.append((ticket_end, copy_lst, copy_visit))
    answer.sort()
    return answer[0]