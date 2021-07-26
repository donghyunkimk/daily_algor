# 화단의 크기
N = int(input())

# 화단의 평당 가격
board = [list(map(int,input().split()))]

# 화단 5평의 가격
board_x5 = [[0]*N for _ in range(N)]

# 상 하 좌 우
x = [-1,1,0,0]
y = [0,0,-1,1]

# 5평의 가격의 합 정리
for i in range(1,N-1):
    for j in range(1,N-1):
        for k in range(4):
            board_x5[i][j] += board[i+x[k]][j+y[k]]

        board_x5 += board[i][j]

