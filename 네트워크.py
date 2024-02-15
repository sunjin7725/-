def connected(computers, idx, visited):
    visited[idx] = True
    for inner_idx, computer in enumerate(computers[idx]):
        if inner_idx != idx and computer == 1 and not visited[inner_idx]:
            connected(computers, inner_idx, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for idx in range(n):
        if not visited[idx]:
            answer += 1
            connected(computers, idx, visited)
    return answer


if __name__ == '__main__':
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(3, computers))
