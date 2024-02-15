def collatz(n):
    result = []
    sum_result = []
    cnt = 0
    while n > 1:
        result.append((cnt, n))
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        min_y = min(result[cnt][1], n)
        max_y = max(result[cnt][1], n)
        sum_result.append(min_y + ((max_y - min_y)/2))
        cnt += 1
    result.append((cnt, n))
    return result, sum_result


if __name__ == '__main__':
    k = 5
    ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

    answer = []
    result, sum_result = collatz(k)
    n = len(result) - 1
    for a, b in ranges:
        if a == 0 and b == 0:
            answer.append(sum(sum_result))
        else:
            b += n
            if a > b:
                answer.append(-1)
            else:
                answer.append(sum(sum_result[a:b]))

