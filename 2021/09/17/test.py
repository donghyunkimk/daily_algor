def dfs(idx,cur_lst,cur_cnt):
    global max_num

    if idx == a_len - 1 or cnt == 0:


    for q in range(idx+1,a_len):
        if cur_lst[idx] < cur_lst[q]:
            cur_lst[idx], cur_lst[q] = cur_lst[q], cur_lst[idx]
            dfs(idx+1, cur_lst, cur_cnt-1)
            cur_lst[idx], cur_lst[q] = cur_lst[q], cur_lst[idx]

    if idx != a_len - 1:
        dfs(idx+1,cur_lst,cur_cnt)



    return

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

    max_num = 0

    # idx, 바꿀 리스트, 남은 횟수
    dfs(0,a_lst,cnt)

    # while cnt != 0:
    #     if len(a_dict) == a_len:
    #         cnt -= 1
    #
    #     else:
    #         a_lst[-1], a_lst[-2] = a_lst[-2], a_lst[-1]
    #         cnt -= 1
    #
    # a_lst.reverse()
    # answer = ''
    # for e in a_lst:
    #     answer += str(e)
    #
    # print('#{} {}'.format(tc,int(answer)))

    print(max_num)
