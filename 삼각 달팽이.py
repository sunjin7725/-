n = 5

x, y = 0, -1
num = 1
answer = [[0 for _ in range(i+1)] for i in range(n)]

for i in range(n):
    for _ in range(i, n):
        if i % 3 == 0:
            y += 1
        elif i % 3 == 1:
            x += 1
        else:
            x -= 1
            y -= 1
        answer[y][x] = num
        num += 1
