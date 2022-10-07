N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4


def solution(n, road, k):
    visited_country = [False for _ in range(n + 1)]
    visited_country[0] = True
    visited_country[1] = True

    road_dict = {}
    for i in road:
        exist_road = road_dict.get((i[0], i[1]), None)
        if exist_road:
            if i[2] < exist_road:
                road_dict[(i[0], i[1])] = i[2]
        else:
            road_dict[(i[0], i[1])] = i[2]
    road = [[key[0], key[1], value] for key, value in road_dict.items()]

    def dfs(left_roads, start_point=1, now_costs=0):
        passed_roads = []
        if len(left_roads) == 0: return
        while left_roads:
            if now_costs > k: break
            now_road = left_roads.pop()
            if now_road[0] == start_point and now_costs + now_road[2] <= k:
                if visited_country[now_road[1]]: continue
                visited_country[now_road[1]] = True
                dfs(left_roads + passed_roads, now_road[1], now_costs + now_road[2])
                left_roads.append(now_road)
            elif now_road[1] == start_point and now_costs + now_road[2] <= k:
                if visited_country[now_road[0]]: continue
                visited_country[now_road[0]] = True
                dfs(left_roads + passed_roads, now_road[0], now_costs + now_road[2])
                left_roads.append(now_road)
            else:
                passed_roads.append(now_road)
    dfs(road)
    return visited_country.count(True) - 1
print(solution())