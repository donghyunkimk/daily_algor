T = int(input())

for tc in range(1,1+T):

    # n초
    n = int(input())

    # 커맨드
    # 커맨드, 속도
    command = [list(map(int,input().split())) for _ in range(n)]

    # 초기 스피드
    speed = 0

    # 이동 거리
    distance = 0

    for q in command:

        # 커맨드가 1인 경우
        # speed 가속(+)
        if q[0] == 1:
            speed += q[1]

        # 커맨드가 2인 경우
        # speed 감속(-)
        elif q[0] == 2:
            speed -= q[1]
            if speed < 0:
                speed = 0

        # 이동 거리에 speed 더하기
        # 매초 이동하기 때문에 speed * 1 해줄 필요 없음
        distance += speed

    print('#{} {}'.format(tc,distance))