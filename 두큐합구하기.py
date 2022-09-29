from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = len(queue1) * 4
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    wanted_num = (sum1 + sum2) / 2
    if int(wanted_num) != wanted_num: return -1

    try_count = 0
    while try_count < limit:
        print(queue1, queue2)
        print(sum1, sum2)
        if sum1 == sum2:
            return try_count
        if sum1 > sum2:
            num = queue1.popleft()
            sum1 -= num
            sum2 += num
            queue2.append(num)
            try_count += 1
        else:
            num = queue2.popleft()
            sum1 += num
            sum2 -= num
            queue1.append(num)
            try_count += 1
    return -1

arr1 = [1,1,1]
arr2 = [5,1,1]

solution(arr1, arr2)