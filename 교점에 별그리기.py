line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]


cross_point_list = []
while line:
    A, B, E = line.pop()
    for another_line in line:
        C, D, F = another_line
        if A*D-B*C != 0:
            x = (B*F-E*D)/(A*D-B*C)
            y = (E*C-A*F)/(A*D-B*C)
            if x.is_integer() and y.is_integer():
                cross_point_list.append((int(x), int(y)))

x_max = max(i[0] for i in cross_point_list)
x_min = min(i[0] for i in cross_point_list)
y_max = max(i[1] for i in cross_point_list)
y_min = min(i[1] for i in cross_point_list)
cross_point_list = sorted(cross_point_list, key=lambda x: x[1])

answer = []
for y in range(y_max, y_min - 1, -1):
    star_point = ""
    for x in range(x_min, x_max + 1):
        print(x, y)
        if (x, y) in cross_point_list: star_point += '*'
        else: star_point += '.'
    answer.append(star_point)