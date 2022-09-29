import numpy as np


if __name__ == '__main__':
    n = 3
    left = 2
    right = 5

    arr = []
    for i in range(n):
        for j in range(n):
            arr.append(max(i + 1, j + 1))
    print(arr[left:right+1])
