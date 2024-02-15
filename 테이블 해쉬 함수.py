data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

data = sorted(data, reverse=True)
data = sorted(data, key=lambda x: x[col-1])

result = []
for i in range(row_begin, row_end+2):
    _sum = 0
    for value in data[i-1]:
        _sum += value % i
    result.append(_sum)

answer = result[0]
for i in range(1, len(result)):
    answer ^= result[i]
