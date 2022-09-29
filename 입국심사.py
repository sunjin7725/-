n = 6
times = [7, 10]

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people_cnt = sum(list(map(lambda x: mid//x, times)))
        if people_cnt >= n:
            answer = mid
            right = mid - 1
        elif people_cnt < n:
            left = mid + 1
    return answer

print(solution(n ,times))