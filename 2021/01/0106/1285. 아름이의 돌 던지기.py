import sys
sys.stdin = open('1285. 아름이의 돌 던지기.txt')

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    positions = list(map(int,input().split()))

    cnt = 1
    min_num = 100001

    for position in positions:
        if abs(position) < min_num:
            min_num = abs(position)
            cnt = 1
        elif abs(position) == min_num:
            cnt += 1

    print('#{} {} {}'.format(tc,min_num,cnt))
