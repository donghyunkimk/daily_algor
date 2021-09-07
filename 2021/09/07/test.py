T = int(input())

for tc in range(1,1+T):
    a,b = map(str,input().split())

    word = list(a)
    word.sort()
    goal = int(b)

    n = len(word)

    t = 1
    while True:
        temp = n ** t

        if goal >= temp:
            goal -= temp

        else:
            break

        t += 1

    if goal == 0:
        t_word = word[-1]*(t-1)
    else:

    # 3자리를 만들어야 한다
        t_word = ''
        while goal >= n:
            g_idx = goal // (n**(t-1))
            if goal == n:
                t_word += word[0]
            else:
                t_word += word[g_idx]
            goal -= g_idx * (n**(t-1))
            t -= 1
        t_word += word[goal-1]

    print('#{} {}'.format(tc,t_word))