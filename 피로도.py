from collections import deque
from itertools import permutations


def search_dungeon(dungeons, fatigue):
    dungeon_case = []

    def permutation(_list, result=[]):
        checkbox = [0] * len(_list)
        if len(_list) == 0:
            dungeon_case.append(result.copy())
            return

        for idx in range(len(_list)):
            if checkbox[idx] == 1: continue
            result.append(_list[idx])
            checkbox[idx] = 1
            permutation(_list[:idx] + _list[idx + 1:], result)
            checkbox[idx] = 0
            result.pop()

    permutation(dungeons)
    # dungeon_case = permutations(dungeons)

    search_dungeon_case = []
    for case in dungeon_case:
        fatigue_in_case = fatigue
        dungeon_cnt = 0
        for dungeon in case:
            need, comsume = dungeon
            if fatigue_in_case < need:
                break
            fatigue_in_case -= comsume
            dungeon_cnt += 1
        search_dungeon_case.append(dungeon_cnt)
    return search_dungeon_case


def solution(k, dungeons):
    return max(search_dungeon(dungeons, k))
