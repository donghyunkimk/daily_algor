def bfs(i,j):
    while len(temp) != 0:
        ni,nj = temp.pop(0)

        for qq in range(1,n+1):
            if board[ni][qq] == 1:
                board[ni][qq] = 0
                board[qq][ni] = 0
                visited[qq] = 1
                visited[ni] = 1
                temp.append([ni,qq])

            if board[nj][qq] == 1:
                board[nj][qq] = 0
                board[qq][nj] = 0
                visited[qq] = 1
                visited[nj] = 1
                temp.append([nj,qq])

    return

# tc 개수
T = int(input())

for tc in range(1,1+T):
    # 주민 수, 관계 수
    n,m = map(int,input().split())

    # 관계
    items = [list(map(int,input().split())) for _ in range(m)]

    # 관계들 저장해서 for문 돌지 않기 위함
    board = [[0]*(n+1) for _ in range(n+1)]

    # 관계가 나오지 않은 곳을 찾기 위해
    visited = [1]+[0]*n

    # 무리의 수
    cnt = 0

    # 관계가 확인된 곳 저장
    for q in items:
        board[q[0]][q[1]] = 1
        board[q[1]][q[0]] = 1

    for w in items:
        # 관계가 확인된 곳이면
        if board[w[0]][w[1]] == 1:

            # 무리의 수 + 1 및 board 초기화, visited 변경
            cnt += 1
            temp = [[w[0],w[1]]]
            board[w[0]][w[1]] = 0
            board[w[1]][w[0]] = 0
            visited[w[0]] = 1
            visited[w[1]] = 1
            bfs(w[0],w[1])

    # 무리의 숫자 + 관계가 나오지 않은 곳들의 수(사람 하나가 하나의 무리)
    res = cnt + visited.count(0)

    print('#{} {}'.format(tc,res))