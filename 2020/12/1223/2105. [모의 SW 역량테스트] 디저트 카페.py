import sys
sys.stdin = open('2105. [모의 SW 역량테스트] 디저트 카페.txt')


def search(ii,jj,dir,path): # y 좌표, x 좌표, 진행 방향, 중복 여부 확인을 위한 리스트
    global max_eat # 값을 수정해야 하기 때문에 global 사용


    if dir < 2: # 2보다 작으면 == 좌하 or 우하 방향으로 이동하면
        if 0 <= ii+x[dir] < n and 0 <= jj+y[dir] < n: # 범위 제한
            if road[ii+x[dir]][jj+y[dir]] not in path: # 다음에 이동할 곳이 중복 값이 아니면
                search(ii+x[dir], jj+y[dir], dir, path+[road[ii+x[dir]][jj+y[dir]]]) # 좌표 수정, 방향은 그대로, 체크용 리스트에 값 집어 넣기
            else: # 중복 값이 있으면
                search(ii, jj, dir + 1, path) # 현재 위치, 방향 수정, 체크용 리스트에 추가 X

        search(ii, jj, dir+1, path) # 다음 이동 방향이 주어진 범위 넘어갈 경우, 리턴을 위해 조건 안 집어 넣음

    elif dir == 2: # 우상으로 이동하면
        if 0 <= ii+x[dir] < n and 0 <= jj+y[dir] < n: # 범위
            if road[ii+x[dir]][jj+y[dir]] not in path: # 중복 값 확인
                if ii+x[dir]-start[0] == jj+y[dir]-start[1]:
                    # 좌상은 현재 위치 값에 -1, -1을 해주는 것
                    # 출발점에 도달하기 위해 우상에서 좌상으로 방향을 바꿔야 하는 기점
                    # 해당 위치를 넘어가도 사각형을 그리면서 시작점으로 돌아올 수는 있음
                    # 그러나 연산 숫자가 많아질 것으로 판단
                    # (시작점은 다르지만) 같은 곳을 방문하는 사각형이 중복이 생기기 때문
                    search(ii+x[dir], jj+y[dir], dir+1, path+[road[ii+x[dir]][jj+y[dir]]]) # 좌표 수정, 방향 수정, 체크용 리스트에 값 추가
                else:
                    search(ii + x[dir], jj + y[dir], dir, path+[road[ii+x[dir]][jj+y[dir]]]) # 좌표 수정, 방향 그대로, 체크용 리스트에 값 추가
            else:
                return
        else:
            return

    else:
        if ii+x[dir] != start[0]: # 아직 출발점에 도달하지 못했을 때
            if road[ii+x[dir]][jj+y[dir]] not in path: # 중복 확인
                search(ii+x[dir], jj+y[dir], dir, path+[road[ii+x[dir]][jj+y[dir]]]) # 좌표 수정, 방향 그대로, 체크용 리스트에 값 추가
            else:
                return
        else:
            if len(path) != 1:
                if len(path) > max_eat:
                    max_eat = len(path)

    return

x = [1,1,-1,-1] # 좌하, 우하, 우상, 좌상
y = [-1,1,1,-1]

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    road = [list(map(int,input().split())) for _ in range(n)] # 길

    max_eat = -1 # 조건에 만족 X == -1 출력

    for i in range(n-1):
        for j in range(1,n-1):
            start=[i,j] # 좌상 방향으로 진행할지 말지를 결정할 때 사용
            search(i,j,0,[road[i][j]]) # y 좌표, x 좌표, 진행 방향, 중복 여부 확인을 위한 리스트

    print('#{} {}'.format(tc, max_eat))