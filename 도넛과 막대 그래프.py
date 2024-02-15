"""
정점은 나가는 edge만 있고 들어오는 edge가 없음.

막대그래프는 나가는 엣지가 0개이며 들어오는 1개임.

8자모양 그래프는 나가는 엣지가 2개 들어오는 엣지가 2개.

도넛모양 그래프는 정점에서 나가는 엣지의 갯수에서 위 두개 그래프의 갯수를 뻄.
"""
import numpy as np

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]


nodes = list(set(np.array(edges).reshape(-1)))
centroid = 0
bar_graph_cnt = 0
eight_graph_cnt = 0
donut_graph_cnt = 0

node_in_count = {i: 0 for i in nodes}
node_out_count = {i: 0 for i in nodes}
for start, end in edges:
    node_in_count[end] += 1
    node_out_count[start] += 1

for node in nodes:
    if node_in_count[node] == 0 and node_out_count[node] > 1:
        centroid = node
    elif node_in_count[node] >= 2 and node_out_count[node] == 2:
        eight_graph_cnt += 1
    elif node_in_count[node] >= 1 and node_out_count[node] == 0:
        bar_graph_cnt += 1

donut_graph_cnt = node_out_count[centroid] - bar_graph_cnt - eight_graph_cnt
print([centroid, donut_graph_cnt, bar_graph_cnt, eight_graph_cnt])
