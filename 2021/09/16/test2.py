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
            n -= temp
            break

    answer = ''
    for q in range(idx):
        t_num = len_word ** (idx - q - 1)
        # c_num = n // t_num
        for w in range(len_word):
            if n - t_num > 0:
                n -= t_num

            elif n - t_num == 0:
                n -= t_num
                answer += word[-1]
                break

            else:
                answer += word[w]
                break

    # while idx != 1:
    #     t_num = len_word ** (idx - 1)
    #
    #     if n > len_word:
    #         if n % t_num == 0:
    #             answer += word[-1]
    #
    #         else:
    #             answer += word[n // t_num]
    #         n -= n // t_num * t_num
    #
    #     elif n == len_word:
    #         answer += word[0]
    #
    #     idx -= 1
    #
    # answer += word[n-1]
    print('#{} {}'.format(tc,answer))