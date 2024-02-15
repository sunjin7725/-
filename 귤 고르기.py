from collections import Counter

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

tang_cnt = sorted(Counter(tangerine).items(), key=lambda x: x[1], reverse=True)

cnt = 0
while k > 0:
    k -= tang_cnt.pop(0)[1]
    cnt += 1

