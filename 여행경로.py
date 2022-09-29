tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


def get_travel_path(tickets, first_target="ICN"):
    result = []

    def dps(travel_path, using_check=[]):
        if len(using_check) == len(tickets):
            result.append(travel_path.copy())
        for idx in range(len(tickets)):
            if idx in using_check: continue
            if tickets[idx][0] == travel_path[-1]:
                travel_path.append(tickets[idx][1])
                using_check.append(idx)
                dps(travel_path, using_check)
                travel_path.pop()
                using_check.pop()

    dps([first_target])
    return result

_list = [['ICN', 'SFO', 'ATL', 'ICN', 'ATL', 'SFO'], ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'], ['ICN', 'ATL', 'SFO', 'ATL', 'ICN', 'SFO']]
print(sorted(_list, key=lambda x: ''.join(x)))