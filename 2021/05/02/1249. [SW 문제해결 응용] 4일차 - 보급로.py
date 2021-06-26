def bfs():

    # temp에 시작 위치(0,0) 저장
    temp = [[0,0]]

    # temp가 빌 때까지 반복
    # == (n-1,n-1)의 값을 구할 때까지
    while len(temp):
        i,j = temp.pop(0)

        for q in range(4):
            ni = i + x[q]
            nj = j + y[q]

            # 범위 제한 조건 안 넘기면
            if 0 <= ni < n and 0 <= nj < n:

                # 이동하려는 위치까지 이동하는 데 소요된 복구 작업의 시간이
                # 현재 위치까지 소요된 복구 작업 시간 + 이동하려는 위치에서 소요되는 작업 시간보다 크면
                # 값 바꾸고, temp에 [ni,nj] 추가
                if check_board[ni][nj] > check_board[i][j] + board[ni][nj]:
                    check_board[ni][nj] = check_board[i][j] + board[ni][nj]
                    temp.append([ni,nj])

    return

x = [0,0,-1,1]
y = [-1,1,0,0]

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    board = [list(map(int,input())) for _ in range(n)]

    # 90000인 이유는 최대 100*100 배열이고
    # 해당 배열을 모두 방문해도 9 * 10000이기 때문
    check_board = [[90000]*n for _ in range(n)]

    # 시작 위치 0으로 만들기
    # 0 아니면 출발이 안 됨
    check_board[0][0] = 0

    bfs()

    print('#{} {}'.format(tc,check_board[n-1][n-1]))