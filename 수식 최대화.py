expression = "100-200*300-500+20"

operation = ['*', '-', '+']

import re

from itertools import permutations

order_list = list(permutations(operation, 3))

operation_order = list(re.sub('[0-9]', '', expression))
num_order = re.split('[^0-9]', expression)

result = []
for order in order_list:
    num_order_copy = num_order.copy()
    operation_order_copy = operation_order.copy()
    for operation in order:
        while operation in operation_order_copy:
            idx = operation_order_copy.index(operation)
            num_order_copy[idx] = str(eval(num_order_copy[idx] + operation + num_order_copy[idx+1]))
            operation_order_copy.pop(idx)
            num_order_copy.pop(idx+1)
    result.append(int(num_order_copy[0]))
result = list(map(abs, result))
print(max(result))
