if __name__ == '__main__':
    numbers = [2, 7]
    answer = []

    num = 7
    def find(num):
        bit_num = '0' + bin(num)[2:]
        idx =  bit_num.rfind('0')
        bit_num = list(bit_num)
        bit_num[idx] = '1'

        if num % 2 == 1:
            bit_num[idx + 1] = '0'
        return int(''.join(bit_num), 2)
