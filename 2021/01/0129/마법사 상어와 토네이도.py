import sys
sys.stdin = open('마법사 상어와 토네이도.txt')

# 1. 방향 정하기

# 격자의 크기
N = int(input())

# 방향 안내판
idx_board = [[0]*N for _ in range(N)]

# 방향 idx
# 오른쪽, 아래, 왼쪽, 위
x = [0,0,1,0,-1]
y = [0,1,0,-1,0]

# 방향을 안내판에 입력하기
idx_board[0][0] = 1
idx = 1
cnt = 1
x_idx = 0
y_idx = 0

while cnt < N*N:
    if 0 <= x_idx + x[idx] < N and 0 <= y_idx + y[idx] < N:
        if idx_board[x_idx + x[idx]][y_idx + y[idx]] == 0:
            idx_board[x_idx + x[idx]][y_idx + y[idx]] = idx
            cnt += 1
            x_idx += x[idx]
            y_idx += y[idx]

        else:
            idx += 1
            if idx == 5:
                idx = 1

    else:
        idx += 1
        if idx == 5:
            idx = 1

# ----------------------------------------- 문제 없음 -----------------------------------------------

# 2. 퍼지는거 계산
# 모래밭
sand_board = [list(map(int,input().split())) for _ in range(N)]

# idx_board == 방향 안내판, sand_board == 값 수정해야할 모래 밭
# 시작점은 sand_board[N//2][N//2]

sand_i = N//2
sand_j = N//2

res = 0

while sand_i != 0 and sand_j != 0:

    temp_minus = 0

    if sand_board[sand_i][sand_j] == 1:
        temp = sand_board[sand_i][sand_j-1]

        # 1
        if 0 <= sand_i-1 and sand_j+1 < N:
            sand_board[sand_i-1][sand_j+1] += int(temp * 0.01)

        else:
            res += int(temp * 0.01)

        if sand_i+1 < N and sand_j+1 < N:
            sand_board[sand_i+1][sand_j+1] += int(temp * 0.01)

        else:
            res += int(temp * 0.01)

        temp_minus += int(temp * 0.01) * 2

        # 2
        if 0 <= sand_i-2:
            sand_board[sand_i-2][sand_j] += int(temp * 0.02)

        else:
            res += int(temp * 0.02)

        if sand_i+2 < N:
            sand_board[sand_i+2][sand_j] += int(temp * 0.02)

        else:
            res += int(temp * 0.02)

        temp_minus += int(temp * 0.02) * 2

        # 7
        if 0 <= sand_i - 1:
            sand_board[sand_i-1][sand_j] += int(temp * 0.07)

        else:
            res += int(temp * 0.07)

        if 0 <= sand_i + 1:
            sand_board[sand_i+1][sand_j] += int(temp * 0.07)

        else:
            res += int(temp * 0.07)

        temp_minus += int(temp * 0.07) * 2

        # 10
        if 0 <= sand_i-1 and 0 <= sand_j-1:
            sand_board[sand_i-1][sand_j-1] += int(temp * 0.1)

        else:
            res += int(temp * 0.1)

        if sand_i+1 < N and 0 <= sand_j-1:
            sand_board[sand_i+1][sand_j-1] += int(temp * 0.1)

        else:
            res += int(temp * 0.1)

        temp_minus += int(temp * 0.1) * 2

        # 5
        if 0 <= sand_j - 2:
            sand_board[sand_i][sand_j - 2] += int(temp * 0.05)

        else:
            res += int(temp * 0.05)

        temp_minus += int(temp * 0.05)

        # @
        if 0 <= sand_j-1:
            sand_board[sand_i][sand_j - 1] += sand_board[sand_i][sand_j] - temp_minus

        else:
            res += sand_board[sand_i][sand_j] - temp_minus


    elif sand_board[sand_i][sand_j] == 2:
        pass

    elif sand_board[sand_i][sand_j] == 3:
        temp = sand_board[sand_i][sand_j + 1]

        # 1
        if 0 <= sand_i - 1 and sand_j + 1 < N:
            sand_board[sand_i - 1][sand_j + 1] += int(temp * 0.01)

        else:
            res += int(temp * 0.01)

        if sand_i + 1 < N and sand_j + 1 < N:
            sand_board[sand_i + 1][sand_j + 1] += int(temp * 0.01)

        else:
            res += int(temp * 0.01)

        temp_minus += int(temp * 0.01) * 2

        # 2
        if 0 <= sand_i - 2:
            sand_board[sand_i - 2][sand_j] += int(temp * 0.02)

        else:
            res += int(temp * 0.02)

        if sand_i + 2 < N:
            sand_board[sand_i + 2][sand_j] += int(temp * 0.02)

        else:
            res += int(temp * 0.02)

        temp_minus += int(temp * 0.02) * 2

        # 7
        if 0 <= sand_i - 1:
            sand_board[sand_i - 1][sand_j] += int(temp * 0.07)

        else:
            res += int(temp * 0.07)

        if 0 <= sand_i + 1:
            sand_board[sand_i + 1][sand_j] += int(temp * 0.07)

        else:
            res += int(temp * 0.07)

        temp_minus += int(temp * 0.07) * 2

        # 10
        if 0 <= sand_i - 1 and 0 <= sand_j - 1:
            sand_board[sand_i - 1][sand_j - 1] += int(temp * 0.1)

        else:
            res += int(temp * 0.1)

        if sand_i + 1 < N and 0 <= sand_j - 1:
            sand_board[sand_i + 1][sand_j - 1] += int(temp * 0.1)

        else:
            res += int(temp * 0.1)

        temp_minus += int(temp * 0.1) * 2

        # 5
        if 0 <= sand_j - 2:
            sand_board[sand_i][sand_j - 2] += int(temp * 0.05)

        else:
            res += int(temp * 0.05)

        temp_minus += int(temp * 0.05)

        # @
        if 0 <= sand_j - 1:
            sand_board[sand_i][sand_j - 1] += sand_board[sand_i][sand_j] - temp_minus

        else:
            res += sand_board[sand_i][sand_j] - temp_minus


    else:
        pass

