places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
def check(place, x, y):
    max_len = len(place) - 1

    if x + 1 <= max_len and place[y][x+1] == 'P':
        return 0
    elif y + 1 <= max_len and place[y+1][x] == 'P':
        return 0
    elif x - 1 >= 0 and place[y][x-1] =='P':
        return 0
    elif y - 1 >= 0 and place[y-1][x] == 'P':
        return 0
    elif x + 2 <= max_len and place[y][x+1] != 'X' and place[y][x+2] == 'P':
        return 0
    elif y + 2 <= max_len and place[y+1][x] != 'X' and place[y+2][x] == 'P':
        return 0
    elif x - 2 >= 0 and place[y][x-1] != 'X' and place[y][x-2] == 'P':
        return 0
    elif y - 2 >= 0 and place[y-1][x] != 'X' and place[y-2][x] == 'P':
        return 0
    elif x + 1 <= max_len and y + 1 <= max_len \
        and not (place[y+1][x] == 'X' and place[y][x+1] == 'X') and place[y+1][x+1] == 'P':
        return 0
    elif x - 1 >= 0 and y - 1 >= 0 and not (place[y-1][x] == 'X' and place[y][x-1] == 'X') and place[y-1][x-1] == 'P':
        return 0
    elif x + 1 <= max_len and y - 1 >= 0 and not (place[y-1][x] == 'X' and place[y][x+1] == 'X') and place[y-1][x+1] == 'P':
        return 0
    elif x - 1 >= 0 and y + 1 <= max_len and not (place[y+1][x] == 'X' and place[y][x-1] == 'X') and place[y+1][x-1] == 'P':
        return 0
    return 1


answer = []
for place in places:
    result = 1
    for y in range(len(place)):
        for x in range(len(place[y])):
            if place[y][x] == 'P':
                result = check(place, x, y)
            if not result:
                break
        if not result:
            break
    answer.append(result)
