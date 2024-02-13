def find_island(maps, x, y, border=0):
    border += int(maps[y][x])
    maps[y][x] = 'X'
    max_x = len(maps[0]) - 1
    max_y = len(maps) - 1

    if x < max_x and maps[y][x + 1] != 'X':
        border = find_island(maps, x + 1, y, border)
    if x > 0 and maps[y][x - 1] != 'X':
        border = find_island(maps, x - 1, y, border)
    if y < max_y and maps[y + 1][x] != 'X':
        border = find_island(maps, x, y + 1, border)
    if y > 0 and maps[y - 1][x] != 'X':
        border = find_island(maps, x, y - 1, border)
    return border


def solution(maps):
    result = []
    maps = list(map(list, maps))
    for x in range(len(maps[0])):
        for y in range(len(maps)):
            test = maps[y][x]
            if maps[y][x] != 'X':
                result.append(find_island(maps, x, y))
    if result:
        return sorted(result)
    else:
        return [-1]


if __name__ == '__main__':
    import numpy as np
    maps = ["X591X1", "X591X1", "X1X5X1", "1231XX", "1XXX11", "X111XX"]
    for y in range(len(maps)):
        print(list(maps[y]))
    print(solution(maps))



