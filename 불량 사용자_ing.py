import re

from itertools import permutations


def check(user_list, banned_id):
    result = [False for _ in range(len(user_list))]
    for banned in banned_id:
        compiler = re.compile(f'^{banned.replace("*", ".")}$')
        for idx, user in enumerate(user_list):
            if not result[idx] and re.match(compiler, user):
                result[idx] = True
                break
    return all(result)


if __name__ == '__main__':
    user_id = ["abcde", "accde", "adcde", "aecde"]
    banned_id = ["a*c*e", "a*c*e", "***de"]

    cnt = 0
    permu = list(set(['|'.join(sorted(i)) for i in permutations(user_id, len(banned_id))]))
    permu = list(map(lambda x: x.split('|'), permu))

    for candi in permu:
        if check(candi, banned_id):
            print(candi)
            cnt += 1
    #
