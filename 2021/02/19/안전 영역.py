def bfs(idx):

    # 방문판
    visited = [[0]*N for _ in range(N)]

    # bfs index값 저장 공간
    temp = []

    # 지역 수
    room = 0

    for q in range(N):
        for w in range(N):

            # 강수량보다 높이가 높고, 방문한 적 없으면
            if board[q][w] > idx and visited[q][w] == 0:

                # 저장
                temp.append([q,w])

                # 방문
                visited[q][w] = 1

                while len(temp) != 0:

                    i,j = temp.pop(0)

                    for e in range(4):
                        ni = i+x[e]
                        nj = j+y[e]

                        # board의 범위 안 넘기고
                        if 0 <= ni < N and 0 <= nj < N:

                            # 방문한 적 없고
                            if visited[ni][nj] == 0:

                                # 강수량보다 높이가 높으면
                                if board[ni][nj] > idx:

                                    # 방문 체크
                                    visited[ni][nj] = 1
                                    temp.append([ni,nj])

                # while 끝나면 지역 하나의 지역으로 인식
                room += 1

    # 다 끝나면 cnt에 저장
    cnt.append(room)

    return

# 상 하 좌 우 이동
x = [-1,1,0,0]
y = [0,0,-1,1]

# 배열의 크기
N = int(input())

# 지역
board = [list(map(int,input().split())) for _ in range(N)]

# 지역의 개수 저장
cnt = []

# 최대 높이
max_height = max(map(max,board))

# 최저 높이
min_height = min(map(min,board))

# 최저 높이 -1 한 이유
# ex) 모든 높이가 2인 경우, 최저 높이로 시작하면
# 모든 구역이 잠겨서 0이 되어버림
# 그러나 강수량이 1인 경우에는 1인 지역이 성립함
for height in range(min_height-1,max_height+1):

    # 강수량
    bfs(height)

print(max(cnt))