n = 6
wires = [[1, 2], [3, 4], [5, 6], [1, 3], [3, 5]]

wires = sorted(wires, key=lambda x: x[0])
result = []
all_node = set([n+1 for i in range(n)])
for i in range(n-1):
    elec = [set(), set()]
    new_wires = wires.copy()
    new_wires.pop(i)
    for idx, (start, end) in enumerate(new_wires):
        if idx == 0:
            elec[0].update((start, end))
            continue

        if start in elec[0]:
            elec[0].add(end)
        elif end in elec[0]:
            elec[0].add(start)
        else:
            elec[1].update((start, end))
    if not elec[1]:
        elec[1] = all_node - elec[0]
    result.append(abs(len(elec[0]) - len(elec[1])))
