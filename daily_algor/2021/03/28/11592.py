T = int(input())

for tc in range(1,1+T):

    # 종로 거리의 길이, 말의 수
    d,n = map(int,input().split())

    # [말 위치, 속도]
    horse = [list(map(int,input().split())) for _ in range(n)]

    # 종로 거리가 끝나는 곳에서 가까운 순으로 정렬
    horse.sort(key=lambda x : x[0], reverse=True)

    # 말의 이동시간
    cnt = 0

    for q in horse:

        # (종로 거리의 길이 - 말의 위치)/말의 속도 == a
        # a가 현재 저장된 이동 시간보다 크면 cnt 값 바꾸기
        # 말을 추월하거나 자율주행차의 속도를 늦추지 않기 위해서는 말과 만나면 안 된다
        # cnt에 이동시간이 가장 긴 말의 이동시간을 저장해둬야 함
        if (d-q[0])/q[1] > cnt:
            cnt = (d-q[0])/q[1]

    # 가능한 최대 속도 = 거리의 길이 / 말의 이동시간
    res = d/cnt

    # {:0<9} 이란, 출력을 위한 9칸을 만들고 해당 칸에 res를 출력
    # 만일 res가 9칸이 안 된다면 나머지(오른쪽으로)는 0으로 채우기
    print('#{} {:0<9}'.format(tc,res))