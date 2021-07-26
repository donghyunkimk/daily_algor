def dfs(idx,dir):

    # 방문 확인
    check[idx] = 1

    # 시계방향으로 움직이면
    if dir == 1:

        # 톱니 바퀴 이동
        wheel[idx].insert(0,wheel[idx].pop(-1))

        # 0~3번 톱니이고, 방문한 적 없으면
        if 0 <= idx + 1 < 4 and check[idx+1] == 0:

            # 현재 톱니의 3번(이동 전 2번)과 오른쪽 톱니의 6번 확인
            if wheel[idx][3] != wheel[idx+1][6]:
                dfs(idx+1, -1)

        if 0 <= idx - 1 < 4 and check[idx-1] == 0:

            # 현재 톱니의 7번(이동 전 6번)과 왼쪽 톱니의 2번 확인
            if wheel[idx][7] != wheel[idx-1][2]:
                dfs(idx-1, -1)

    else:
        wheel[idx].append(wheel[idx].pop(0))
        if 0 <= idx + 1 < 4 and check[idx + 1] == 0:

            if wheel[idx][1] != wheel[idx + 1][6]:
                dfs(idx + 1, 1)

        if 0 <= idx - 1 < 4 and check[idx-1] == 0:

            if wheel[idx][5] != wheel[idx - 1][2]:
                dfs(idx - 1, 1)

    return

T = int(input())

for tc in range(1,1+T):

    # 회전 수
    k = int(input())

    # 톱니
    wheel = [list(map(int,input().split())) for _ in range(4)]

    # 번호, 방향
    arr = [list(map(int,input().split())) for _ in range(k)]

    for q in arr:

        # 방문 확인용
        check = [0 for _ in range(4)]

        # 번호(1~4번인데 wheel의 index는 0~3이라 -1함), 방향
        dfs(q[0]-1,q[1])

    # 결과
    res = 0

    # 화살표가 가리키는 곳을 계산에 따라 계산
    for w in range(4):
        res += wheel[w][0] * (2**w)

    print('#{} {}'.format(tc,res))