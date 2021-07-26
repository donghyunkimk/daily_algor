import sys
sys.stdin = open('숫자판 점프.txt')

# 이동 함수
def move(i,j,cnt,word):
    if cnt == 6:
        if word not in res:
            res.append(word)

        return

    for e in range(4):
        N_i = i+x[e]
        N_j = j+y[e]

        # 범위 확인
        if 0 <= N_i < 5 and 0 <= N_j < 5:
            move(N_i,N_j,cnt+1,word+str(board[N_i][N_j]))

    return

# 이동 상 하 좌 우
x = [-1,1,0,0]
y = [0,0,-1,1]

# 숫자판
board = [list(map(int,input().split())) for _ in range(5)]

# 저장 공간
res = []

for q in range(5):
    for w in range(5):
        move(q,w,1,str(board[q][w]))

print(len(res))