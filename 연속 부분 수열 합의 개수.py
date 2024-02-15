elements = [7, 9, 1, 1, 4]


def summation(elements, k=1):
    result = []
    num = len(elements)
    elements = elements * 2
    for i in range(num):
        result.append(sum(elements[i:i + k]))
    return set(result)


def solution(elements):
    answer = set()
    for i in range(1, len(elements) + 1):
        answer.update(summation(elements, i))
    return len(sorted(list(answer)))


if __name__ == '__main__':
    test = solution(elements)
