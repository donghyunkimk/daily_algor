def comb(temp_lst,comb_idx):
    for e in range(comb_idx,n):
        for ee in cores_dir[e]:
            comb(temp_lst+[ee],comb_idx+1)


    pass


T = int(input())

for tc in range(1,1+T):
    n = int(input())

    board = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0

    cores = []
    cores_dir = []

    for q in range(n):
        for w in range(n):
            if board[q][w] == 1:
                if q == 0 or q == n-1 or w == 0 or w == n-1:
                    cnt += 1

                else:
                    cores.append([q,w])

    for qq in cores:
        idx = 0
        cores_dir.append([])
        up_cnt = 0
        for up in range(0,qq[0]):
            if board[up][qq[1]] == 1:
                up_cnt = 1
                break
        if up_cnt == 0:
            cores_dir[idx].append(1)

        down_cnt = 0
        for down in range(qq[0]+1,n):
            if board[down][qq[1]] == 1:
                down_cnt = 1
                break
        if down_cnt == 0:
            cores_dir[idx].append(2)

        left_cnt = 0
        for left in range(0,qq[1]):
            if board[qq[0]][left] == 1:
                left_cnt = 1
                break
        if left_cnt == 0:
            cores_dir[idx].append(3)

        right_cnt = 0
        for right in range(qq[1]+1,n):
            if board[qq[0]][right] == 1:
                right_cnt = 1
                break
        if right_cnt == 0:
            cores_dir[idx].append(4)

        idx += 1

    cores_comb = []

    comb([],0)