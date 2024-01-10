import pandas as pd

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

df = pd.DataFrame(data=0, columns=friends, index=friends)

for gift in gifts:
    _from, _to = gift.split()
    df.loc[_from, _to] += 1

df['taken'] = df.sum()
df['gift_point'] = [row[friends].sum() - row['taken'] for idx, row in df.iterrows()]

answer_list = []
for give_friend in friends:
    cnt = 0
    for take_friend in friends:
        if give_friend != take_friend:
            if df.loc[give_friend, take_friend] > df.loc[take_friend, give_friend]:
                cnt += 1
            elif (df.loc[give_friend, take_friend] == df.loc[take_friend, give_friend] and
                  df.loc[give_friend, 'gift_point'] > df.loc[take_friend, 'gift_point']):
                cnt += 1
    answer_list.append(cnt)



