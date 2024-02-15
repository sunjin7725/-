from collections import Counter
from itertools import combinations


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]


answer = []

for k in course:
    orders_combi = [j for i in orders for j in combinations(i, k)]
    orders_combi = list(map(lambda x: ''.join(sorted(x)), orders_combi))
    if orders_combi:
        orders_count = Counter(orders_combi)
        orders_count = sorted(orders_count.items(), key=lambda x: x[1], reverse=True)
        max_orders_count = max(orders_count, key=lambda x: x[1])[1]
        for menu, cnt in orders_count:
            if cnt == max_orders_count and cnt > 1:
                answer.append(menu)
            else: break
