from dataclasses import dataclass

dirs = 'LLRR'


def get_target(source, command):
    arrow = {
        'U': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
        'D': (0, -1)
    }
    target_x = source[0] + arrow[command][0]
    target_y = source[1] + arrow[command][1]

    if target_x > 5 or target_x < -5 or \
            target_y > 5 or target_y < -5:
        return None
    return (target_x, target_y)


def solution1(dirs):
    path_set = set()
    now_coord = (0, 0)

    for idx, command in enumerate(dirs):
        target_coord = get_target(now_coord, command)
        if target_coord:
            path_set.add((now_coord, target_coord))
            path_set.add((target_coord, now_coord))
            now_coord = target_coord
    return len(path_set)//2


def solution(dirs):
    visit = set()
    x = 0;
    y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y + 1)))
            y += 1

        elif d == 'D' and y > -5:
            visit.add(((x, y - 1), (x, y)))
            y -= 1

        elif d == 'R' and x < 5:
            visit.add(((x, y), (x + 1, y)))
            x += 1

        elif d == 'L' and x > -5:
            visit.add(((x - 1, y), (x, y)))
            x -= 1
    print(visit)
    return len(visit)

print(solution1(dirs))