import re

num = 437674
base = 3

def is_prime(num):
    if not num.isnumeric(): return False
    num = int(num)
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

def transfer_num(num, base):
    transfer = '0123456789ABCDEF'
    result = []
    while num > 0:
        num, q = divmod(num, base)
        result.append(q)
    return ''.join([transfer[i]for i in result[::-1]])
