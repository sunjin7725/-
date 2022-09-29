n = 5
money = [1, 2, 5]


def solution(n, money):
    need = [1] + [0] * n
    for coin in money:
        for i in range(coin, n + 1):
            if i >= coin:
                need[i] += need[i - coin]

    return need[n] % 1000000007

print(solution(n, money))


# 시간 초과
def change_money(n, money):
    result = []

    def dfs(sum=0, payed_money=[0] * len(money)):
        if sum == n:
            result.append(tuple(payed_money.copy()))
        for idx, coin in enumerate(money):
            if sum > n: continue
            else:
                payed_money[idx] += 1
                sum += coin
                dfs(sum, payed_money)
                payed_money[idx] -= 1
                sum -= coin
    dfs()
    return len(set(change_money(n, money)))