import sys
sys.stdin = open('양.txt')

def search(i,j):
    global sheep
    global wolf

    temp = []
    temp.append([i,j])

    while len(temp) != 0:

        # temp의 값을 하나 뽑아서
        ii,jj = temp.pop(0)

        # 4방향 확인
        for e in range(4):
            N_i = ii + x[e]
            N_j = jj + y[e]

            # 범위 확인
            if 0 <= N_i < R and 0 <= N_j < C:

                # 방문 여부 확인
                if visited[N_i][N_j] == 0:

                    # 방문 체크
                    visited[N_i][N_j] = 1

                    # 늑대면 +1하고, temp에 추가
                    if board[N_i][N_j] == 'v':
                        wolf += 1
                        temp.append([N_i,N_j])

                    # 양
                    elif board[N_i][N_j] == 'o':
                        sheep += 1
                        temp.append([N_i,N_j])

                    # 땅
                    elif board[N_i][N_j] == '.':
                        temp.append([N_i,N_j])

    # 양과 늑대의 숫자를 리턴
    return [sheep, wolf]

# 이동 상 하 좌 우
x = [-1,1,0,0]
y = [0,0,-1,1]

# 행, 렬
R,C = map(int,input().split())

# 마당
board = [list(str(input())) for _ in range(R)]

# 방문 확인용
visited = [[0]*C for _ in range(R)]

# 양 결과
res_o = 0

# 늑대 결과
res_v = 0

for q in range(R):
    for w in range(C):

        # 양, 늑대, 결과값 초기화
        sheep = 0
        wolf = 0
        res = [0,0]

        # 방문 확인
        if visited[q][w] == 0:
            visited[q][w] = 1

            if board[q][w] == 'v':
                wolf += 1
                res = search(q, w)

            elif board[q][w] == 'o':
                sheep += 1
                res = search(q, w)

            elif board[q][w] == '.':
                res = search(q, w)

            else:
                pass

        if res[0] == res[1] == 0:
            pass

        else:
            if res[0] > res[1]:
                res_o += res[0]

            else:
                res_v += res[1]

print(res_o, res_v)