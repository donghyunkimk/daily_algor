import sys
sys.stdin = open('10580. 전봇대.txt')

    T = int(input())

    for tc in range(1,1+T):
        n = int(input())

        # 전선을 저장하기 위한 빈 list
        wire_check = []

        # 교차점
        cnt = 0

        for q in range(n):
            wire = list(map(int,input().split()))

            # 왼쪽 전봇대에서 전선의 위치
            wire_l = wire[0]

            # 오른쪽 전봇대에서 전선의 위치
            wire_r = wire[1]


            if wire_check != 0:
                for w in wire_check:

                    # 교차점이 생기는 경우
                    if (w[0] < wire_l and w[1] > wire_r) or (w[0] > wire_l and w[1] < wire_r):

                        # 교차점 추가
                        cnt += 1

                # 새로운 전선 추가
                wire_check.append(wire)

            else:
                wire_check.append(wire)

        print('#{} {}'.format(tc,cnt))

    #
    # wire = [list(map(int,input().split())) for _ in range(n)]
    #
    # print(wire)