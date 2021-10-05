T = int(input())

for tc in range(1,1+T):
    word,n = map(str,input().split())

    len_word = len(word)
    word = list(word)

    n = int(n)

    temp = 0
    # 구해야 할 자리수
    idx = 1
    while True:
        if temp + len_word ** idx < n:
            temp += len_word ** idx
            idx += 1

        else:
            break

    answer = ''
    for q in range(idx):
        t_num = len_word ** (idx - q - 1)



    print('#{} {}'.format(tc,answer))

