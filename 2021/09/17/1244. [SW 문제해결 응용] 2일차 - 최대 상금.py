T = int(input())

for tc in range(1,1+T):
    a,cnt = map(int,input().split())

    a_str = str(a)
    a_len = len(a_str)
    a_lst = [0 for _ in range(a_len)]
    a_dict = dict()

    for q in range(a_len):
        a_lst[q] = int(a_str[q:q+1])
        if a_lst[q] not in a_dict:
            a_dict[a_lst[q]] = 1

    a_lst.reverse()
    for w in range(a_len):
        if max(a_lst[:a_len-w]) != a_lst[a_len-w-1]:
            max_idx = a_lst[:a_len - w].index(max(a_lst[:a_len - w]))
            a_lst[a_len-w-1], a_lst[max_idx] = a_lst[max_idx], a_lst[a_len-w-1]
            cnt -= 1
            if cnt == 0:
                break

    while cnt != 0:
        if len(a_dict) == a_len:
            cnt -= 1

        else:
            a_lst[-1], a_lst[-2] = a_lst[-2], a_lst[-1]
            cnt -= 1

    a_lst.reverse()
    answer = ''
    for e in a_lst:
        answer += str(e)

    print('#{} {}'.format(tc,int(answer)))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645


