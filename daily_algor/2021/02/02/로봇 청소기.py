import sys
sys.stdin = open('로봇 청소기.txt')

def search(i,j,s_dir):
    global res

    temp = []
    temp.append([i,j])

    while len(temp) != 0:

        ii,jj = temp.pop(0)

        for q in range(4):

            N_i = ii + x[(s_dir + 3 - q) % 4]
            N_j = jj + y[(s_dir + 3 - q) % 4]

            if board[N_i][N_j] == 0 and cleaned[N_i][N_j] == 0:
                temp.append([N_i,N_j])
                cleaned[N_i][N_j] = 1
                res += 1
                s_dir = (s_dir + 3 - q) % 4
                break

        if len(temp) == 0:
            N_i = ii+x[(s_dir+2)%4]
            N_j = jj+y[(s_dir+2)%4]

            if board[N_i][N_j] == 0:
                temp.append([N_i, N_j])

    return

# 방향 이동, 북 동 남 서
x = [-1,0,1,0]
y = [0,1,0,-1]

# n,m
N,M = map(int,input().split())

# 로봇 청소기 위치(r,c),방향
r,c,dir = map(int,input().split())

# 청소 구역
board = [list(map(int,input().split())) for _ in range(N)]

# 청소 확인
cleaned = [[0]*M for _ in range(N)]

res = 0

if board[r][c] == 0:
    cleaned[r][c] = 1
    res += 1

search(r,c,dir)

print(res)