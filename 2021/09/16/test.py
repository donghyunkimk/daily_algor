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
    while idx != 1:
        if n == len_word:
            if idx != 1:
                answer += word[0]

            else:
                n = 0

        elif n > len_word:
            pass

        else:

            t_num = len_word ** (idx - 1)
            answer += word[n // t_num]
            n -= n // t_num * t_num

        idx -= 1

    answer += word[n-1]
    print('#{} {}'.format(tc,answer))