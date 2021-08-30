# 미리 만들어두기
alpha = dict()
lst = ['A', 'E', 'I', 'O', 'U']
idx = 0

def dfs(my_word):
    global idx

    alpha[my_word] = idx
    idx += 1

    if len(my_word) == 5:
        return

    for q in range(5):
        dfs(my_word + lst[q])

    return

dfs('')

def solution(word):
    answer = alpha.get(word)
    return answer