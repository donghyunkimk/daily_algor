def bfs():
    global cnt
    # 멘홀 위치, 현재까지 걸린 시간
    temp = [[r,c,1,board[r][c]]]

    # 주어진 시간 전에 모든 위치 방문 가능하기 때문에 조건을 len(temp)로 줌
    while len(temp):

        # 위치(i,j), 현재까지 시간, 현재위치의 터널 번호
        i,j,time,num = temp.pop(0)

        # 탈출조건
        # 시간 됐으면 탈출
        if time == l:
            break

        for q in range(4):
            ii = i+tunnel[2*num][q]
            jj = j+tunnel[2*num+1][q]

            # 0,0을 더해서 현재 위치에서 이동하지 않는 경우 배제
            if ii == i and jj == j:
                continue

            # 범위 조건
            if 0 <= ii < n and 0 <= jj < m:

                # 방문할 위치의 값이 0이 아니고
                # 방문한 적 없으면
                if board[ii][jj] != 0 and check[ii][jj] == 0:
                    temp_num = board[ii][jj]

                    # 이동할 곳의 터널이 현재의 터널과 연결 가능한지 확인
                    if tunnel[2*temp_num][(q+2)%4] != 0 or tunnel[2*temp_num+1][(q+2)%4] != 0:
                        temp.append([ii,jj,time+1,temp_num])
                        check[ii][jj] = 1
                        cnt += 1

    return

T = int(input())

# 터널 정보
# 상 좌 하 우
tunnel = [
    [0],[0],
    [-1,0,1,0],[0,-1,0,1],
    [-1,0,1,0],[0,0,0,0],
    [0,0,0,0],[0,-1,0,1],
    [-1,0,0,0],[0,0,0,1],
    [0,0,1,0],[0,0,0,1],
    [0,0,1,0],[0,-1,0,0],
    [-1,0,0,0],[0,-1,0,0]
]

for tc in range(1,1+T):

    # 세로 n 가로 m 맨홀 위치 r,c 시간 l
    n,m,r,c,l = map(int,input().split())

    # 지도
    board = [list(map(int,input().split())) for _ in range(n)]

    # 방문 확인
    check = [[0 for _ in range(m)] for t in range(n)]

    # 맨홀은 무조건 방문
    check[r][c] = 1

    # 맨홀 1
    cnt = 1

    bfs()
    print('#{} {}'.format(tc,cnt))