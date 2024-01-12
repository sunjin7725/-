import numpy as np


def is_all_same(arr):
    size = len(arr)
    if np.sum(arr) == size ** 2:
        return True, 1
    elif np.sum(arr) == 0:
        return True, 0
    return False, None


def rolling(arr, result=None):
    if result is None:
        result = [0] * 2
    size = int(len(arr)//2)
    arr = np.array(arr)
    for y in range(0, len(arr), size):
        for x in range(0, len(arr[0]), size):
            is_same, value = is_all_same(arr[y:y+size, x:x+size])
            if is_same:
                result[value] += 1
            elif (not is_same) and size > 1:
                result = rolling(arr[y:y+size, x:x+size], result)
    return result


def solution(arr):
    is_same, value = is_all_same(arr)
    if is_same:
        result = [0, 0]
        result[value] += 1
        return result
    else:
        return rolling(arr)


if __name__ == '__main__':
    arr = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    print(solution(arr))

