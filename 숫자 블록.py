begin = 1
end = 10
# result = [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]


def div_num(num):
    _list = []
    for i in range(1, int(num ** 1/2) + 1):
        if num % i == 0:
            _list.append(i)
    return _list

print(len(div_num(1000000000)))