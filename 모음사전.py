def solution(find_word):
    word_list = []

    def dfs(length, word=''):
        vowel = "AEIOU"
        if length == 0:
            return
        for i in range(len(vowel)):
            word_list.append(word + vowel[i])
            dfs(length-1, word + vowel[i])
    dfs(5)
    return word_list.index(find_word) + 1

if __name__ == '__main__':
    print(solution('AAAE'))