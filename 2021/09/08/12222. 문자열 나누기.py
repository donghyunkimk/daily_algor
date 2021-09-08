T = int(input())

# 좌 우 우하 위치의 타일 확인위한 인덱스
x = [0,1,1]
y = [1,0,1]

for tc in range(1,1+T):

    n,m = map(int,input().split())

    tiles = [list(input()) for _ in range(n)]

    # 방문여부
    check = [[0]*m for _ in range(n)]

    answer = 0
    for q in range(n):
        if answer == 1:
            break

        for w in range(m):
            if answer == 1:
                break

            if tiles[q][w] == '#' and check[q][w] == 0:
                check[q][w] = 1

                # 3 방향 확인
                for e in range(3):
                    i = x[e] + q
                    j = y[e] + w

                    if i < n and j < m:
                        if tiles[i][j] == '#':
                            check[i][j] = 1

                        else:
                            answer = 1
                            break

                    else:
                        answer = 1
                        break

    if answer == 1:
        print('#{} {}'.format(tc,'NO'))

    else:
        print('#{} {}'.format(tc,'YES'))