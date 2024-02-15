from collections import Counter
class ShoppingList:
    def __init__(self, want, number):
        self.shopping = dict(list(zip(want, number)))

    def can_buy(self, discount_cnt):
        for key in self.shopping.keys():
            if discount_cnt.get(key, -1) < self.shopping.get(key):
                return False
        return True


if __name__ == '__main__':
    want = ["banana", "apple", "rice", "pork", "pot"]
    number = [3, 2, 2, 2, 1]
    discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

    shopping_list = ShoppingList(want, number)
    result = []
    for i in range(len(discount)):
        discount_cnt = Counter(discount[i: min(len(discount), i + 10)])
        if shopping_list.can_buy(discount_cnt):
            result.append(i+1)

