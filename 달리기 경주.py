players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

""" 시간초과
for call in callings:
    idx = players.index(call)
    players.pop(idx)
    players = players[:idx-1] + [call] + players[idx-1:]
    print(players)
"""
