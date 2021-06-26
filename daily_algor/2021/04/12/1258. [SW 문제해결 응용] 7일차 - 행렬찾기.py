def search(i,j):

    # 화학 물질들의 구역 길이
    i_cnt = 1
    j_cnt = 1

    while True:
        ni = i + x[0]

        if ni < n and board[ni][j] != 0:
            i_cnt += 1
            i = ni

        else:
            break

    while True:
        nj = j + y[1]

        if nj < n and board[i][nj] != 0:
            j_cnt += 1
            j = nj

        else:
            break

    # [x 길이, y 길이, 곱]
    res.append([i_cnt,j_cnt,i_cnt*j_cnt])

    # x,y 길이 return
    return [i_cnt, j_cnt]

def visit(ii,jj):

    # 방문처리
    for e in range(ii, ii+i_c):
        for r in range(jj, jj+j_c):
            visited[e][r] = 1

    return

# 아래, 오른쪽 이동
x = [1,0]
y = [0,1]

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    # 화학 물질 현황
    board = [list(map(int,input().split())) for _ in range(n)]

    # 방문 여부
    visited = [[0 for _ in range(n)] for _ in range(n)]

    # [x 길이, y 길이, 곱] 순서로 저장
    res = []

    for q in range(n):
        for w in range(n):

            # 방문한적 없고, 0이 아니면 시작점으로 인식
            if board[q][w] != 0 and visited[q][w] == 0:

                # 길이 저장
                [i_c,j_c] = search(q,w)

                # 방문 처리
                visit(q,w)

    # 사각형의 넓이, 행의 길이에 따라 정렬
    res.sort(key=lambda x : (x[2], x[0]))

    print('#{} {}'.format(tc,len(res)), end=' ')
    for p_res in res:
        print(p_res[0],p_res[1],end=' ')
    print()