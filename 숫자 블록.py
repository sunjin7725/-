begin = 1000000000 - 10
end = 1000000000

# result = [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]


def get_divide_num(num):
    result = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            result.append(i)
            if i != (num // i):
                result.append(num // i)

    return [i for i in sorted(result) if i <= 10000000 or i == num]


def solution(begin, end):
    result = [0] * (end - begin + 1)
    for i in range(begin, end + 1):
        divide_nums = get_divide_num(i)
        if len(divide_nums) == 1:
            result[i - begin] = 0
        elif len(divide_nums) == 2:
            result[i - begin] = 1
        elif len(divide_nums) > 2:
            result[i - begin] = divide_nums[-2]
    return result

print(solution(begin, end))


""" 시간초과
def solution(begin, end):
    result = [0] * (end + 1)
    
    for i in range(1, end + 1):
        for j in range(i * 2, end + 1, i):
            result[j] = i
    return result[begin:end+1]
"""
