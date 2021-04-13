T = int(input())

for tc in range(1,1+T):

    # 정점의 개수, 간선의 개수
    v,e = map(int,input().split())

    # 간선의 정보
    board = [list(map(int,input().split())) for _ in range(e)]
    board.sort(key=lambda x : x[2])

    # 사이클 막기 위한 방문용
    visited = [0 for _ in range(v+1)]

    res = 0

    for q in board:
        if visited[q[0]] == 1 and visited[q[1]] == 1:
            pass

        else:
            res += q[2]
            visited[q[0]] = 1
            visited[q[1]] = 1


    print('#{} {}'.format(tc,res))