import sys
sys.stdin = open('3431. 준환이의 운동관리.txt')

T = int(input())

for tc in range(1,1+T):

    # L분 이상 U분 이하의 운동 시간, X 현재 운동한 시간
    L,U,X = map(int,input().split())

    # 부족한 경우
    if X < L:
        print('#{} {}'.format(tc,L-X))

    # 초과한 경우
    elif X > U:
        print('#{} {}'.format(tc,-1))

    # 충분한 경우
    else:
        print('#{} {}'.format(tc,0))