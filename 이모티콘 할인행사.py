from itertools import product

discount = [0.1, 0.2, 0.3, 0.4]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

discount_case = product(discount, repeat=len(emoticons))

result = []
for i in discount_case:
    emoticon_buy = 0
    plus = 0
    for wannabe_discount, value in users:
        user_buy = 0
        for idx, percentage in enumerate(i):
            if percentage >= wannabe_discount / 100:
                user_buy += emoticons[idx] * (1-percentage)
        if user_buy >= value:
            plus += 1
        else:
            emoticon_buy += user_buy

    result.append([plus, emoticon_buy])
result = sorted(result, reverse=True)
