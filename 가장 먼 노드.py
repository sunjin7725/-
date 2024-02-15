n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

vertex = sorted(vertex)
vertex = [sorted(i) for i in vertex]

class Node:
    def __init__(self, _id):
        self.node_id = _id
        self.next = []

    def add_next(self, next_node):
        self.next.append(next_node)
        self.next = list(set(self.next))


from collections import deque

node = {i+1: Node(i+1) for i in range(n)}
visited = [0 for _ in range(n+1)]
for v1, v2 in vertex:
    node[v1].add_next(node[v2])
    node[v2].add_next(node[v1])

q = deque([node[1]])
visited[1] = 1
while q:
    now = q.popleft()
    for node in now.next:
        if not visited[node.node_id]:
            visited[node.node_id] = visited[now.node_id] + 1
            q.append(node)

max_cnt = max(visited)
print(visited.count(max_cnt))
