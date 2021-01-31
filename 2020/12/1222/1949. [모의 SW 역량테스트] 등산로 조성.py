import sys
sys.stdin = open('1949. [모의 SW 역량테스트] 등산로 조성.txt')


def search(start_x, start_y, cur_height, cnt, check): # 시작 위치, 현재 높이, 현재 몇 번 움직였는지, 깎았는지 여부(0 안 깎음, 1 깎음)
    global max_path

    for dir in range(4): # 상 하 좌 우 탐색
        if 0 <= start_x+x[dir] < n and 0 <= start_y+y[dir] < n: # 범위 제한
            nx = start_x+x[dir]
            ny = start_y+y[dir]
            if cur_height > mountain[nx][ny]: # 현재 높이가 이동할 방향의 높이보다 높을 때
                if visited[nx*n+ny] == 0: # 방문 안 했으면
                    visited[nx*n+ny] = 1 # 방문 체크
                    search(nx, ny, mountain[nx][ny], cnt + 1, check)
                    visited[nx * n + ny] = 0 # 방문 초기화

            else:
                if mountain[nx][ny] - cur_height < k:
                    # 이동할 방향의 높이 - 현재 높이가 k보다 작으면
                    # 만약 k와 같거나 크면 다 깎아도 이동할 수 없음
                    # k와 비교하는 이유는 봉우리를 최소한으로 깎기 위해(최소한으로 깎아야 가장 많은 곳 방문 가능)
                    if check != 1: # 깎은적이 없으면
                        if visited[nx * n + ny] == 0: # 방문 안 했으면
                            visited[nx * n + ny] = 1 # 방문 체크
                            search(nx, ny, cur_height-1, cnt + 1, 1)
                            visited[nx * n + ny] = 0


    if max_path < cnt:
        max_path = cnt

    return

x = [-1,1,0,0] # 상 하 좌 우
y = [0,0,-1,1]


T = int(input())

for tc in range(1,1+T):
    n,k = map(int,input().split())

    mountain = [list(map(int,input().split())) for _ in range(n)] # 봉우리

    max_num = 0 # 가장 높은 봉우리
    start = [] # 시작 지점

    for i in range(n):
        for j in range(n):
            if mountain[i][j] > max_num:
                max_num = mountain[i][j]
                start = []
                start.append([i,j])

            elif mountain[i][j] == max_num:
                start.append([i,j])

    max_path = 0 # 가장 긴 등산로

    for s in start:
        visited = [0]*(n**2) # 방문여부 초기화
        visited[s[0]*n+s[1]] = 1 # 시작 지점 방문 체크
        search(s[0],s[1],mountain[s[0]][s[1]],1,0) # 시작 위치, 현재 높이, 현재 몇 번 움직였는지, 깎았는지 여부(0 안 깎음, 1 깎음)
    print('#{} {}'.format(tc, max_path))