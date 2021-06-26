import sys
sys.stdin = open('도로건설.txt')

def ver(ii,jj):
    global res

    for e in range(1,4):
        temp = []
        temp.append([ii,jj])
        idx = 0

        while len(temp) != 0:

            N_i = temp[idx][0]+nx[e]
            N_j = temp[idx][1]+ny[e]

            if 0 <= N_i < H and 0 <= N_j < W:

                if town[N_i][N_j] == 0:
                    temp.append([N_i,N_j])
                    idx += 1

                else:
                    temp = []


            else:
                if len(temp) > 1:
                    temp_res = 0

                    for h in house:
                        short_res = 10000

                        for t in temp:
                            if short_res > abs(h[0] - t[0]) + abs(h[1] - t[1]):
                                short_res = abs(h[0] - t[0]) + abs(h[1] - t[1])

                        if temp_res < short_res:
                            temp_res = short_res

                    res.append(temp_res)

                temp = []

    return

def right_down(ii,jj):
    global res

    for e in range(2):
        temp = []
        temp.append([ii, jj])
        idx = 0

        while len(temp) != 0:

            N_i = temp[idx][0] + nx[e*2]
            N_j = temp[idx][1] + ny[e*2]

            if 0 <= N_i < H and 0 <= N_j < W:

                if town[N_i][N_j] == 0:
                    temp.append([N_i, N_j])
                    idx += 1

                else:
                    temp = []


            else:
                if len(temp) > 1:
                    temp_res = 0

                    for h in house:
                        short_res = 10000

                        for t in temp:
                            if short_res > abs(h[0] - t[0]) + abs(h[1] - t[1]):
                                short_res = abs(h[0] - t[0]) + abs(h[1] - t[1])

                        if temp_res < short_res:
                            temp_res = short_res

                    res.append(temp_res)

                temp = []

    return

def left_down(ii,jj):
    global res

    temp = []
    temp.append([ii, jj])
    idx = 0

    while len(temp) != 0:

        N_i = temp[idx][0] + nx[3]
        N_j = temp[idx][1] + ny[3]

        if 0 <= N_i < H and 0 <= N_j < W:

            if town[N_i][N_j] == 0:
                temp.append([N_i, N_j])
                idx += 1

            else:
                temp = []


        else:
            if len(temp) > 1:
                temp_res = 0

                for h in house:
                    short_res = 10000

                    for t in temp:
                        if short_res > abs(h[0] - t[0]) + abs(h[1] - t[1]):
                            short_res = abs(h[0] - t[0]) + abs(h[1] - t[1])

                    if temp_res < short_res:
                        temp_res = short_res

                res.append(temp_res)

            temp = []

    return


T = int(input())

# 가로 세로 우하 좌하
nx = [0,1,1,1]
ny = [1,0,1,-1]

for tc in range(1,1+T):

    W,H = map(int,input().split())

    town = [list(map(int,input().split())) for _ in range(H)]

    res = []

    house = []

    for q in range(H):
        for w in range(W):
            if town[q][w] == 1:
                house.append([q,w])

    # 0,0은 따로 구하기
    start = [[0,n] for n in range(1,W)]
    sec = [[n,0] for n in range(1,H)]
    third = [[n,W-1] for n in range(1,H)]
    start += sec + third

    for x in start:

        if town[x[0]][x[1]] == 0:

            if x[0] == 0:

                ver(x[0],x[1])

            elif x[1] == 0:

                right_down(x[0],x[1])

            else:

                left_down(x[0],x[1])

    ver(0,0)
    right_down(0,0)

    if len(res) != 0:
        print('#{} {}'.format(tc,min(res)))
    else:
        print('#{} {}'.format(tc,-1))