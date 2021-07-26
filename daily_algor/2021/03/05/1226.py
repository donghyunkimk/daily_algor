import sys
sys.stdin = open('1226.txt')

def bfs(ii,jj):

    check = 0

    temp = [[ii,jj]]

    # 방문 표시
    visited[ii][jj] = 1

    # 계속 반복
    while True:
        i_idx, j_idx = temp.pop(0)

        for e in range(4):
            ni = i_idx+x[e]
            nj = j_idx+y[e]

            # index 범위 안에 있고
            if 0 <= ni < 100 and 0 <= nj < 100:

                # 이동할 곳이 길이며, 방문한 적이 없는 경우
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:
                    temp.append([ni,nj])
                    visited[ni][nj] = 1

                # 도착점이면 탈출
                elif maze[ni][nj] == 3:
                    check = 1
                    break

        # 도착점에 도착했거나 더 이상 이동하지 못하게 되었을 때
        if check == 1 or len(temp) == 0:
            break

    return check

x = [-1,1,0,0]
y = [0,0,-1,1]


for t in range(10):
    tc = int(input())

    # 미로
    maze = [list(map(int,input())) for _ in range(100)]

    # 방문 확인용
    visited = [[0]*100 for _ in range(100)]

    i = -1
    j = -1

    for q in range(100):
        for w in range(100):

            # 출발점 찾기
            if maze[q][w] == 2:
                i = q
                j = w
                break

        if i != -1:
            break

    res = bfs(i,j)

    print('#{} {}'.format(tc,res))