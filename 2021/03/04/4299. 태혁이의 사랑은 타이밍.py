# tc 수
T = int(input())

for tc in range(1,1+T):
    # 날짜, 시간, 분
    d,h,m = map(int,input().split())

    # -1 출력을 위한 check
    check = 0
    day = d - 11
    hour = day*24 + h - 11
    if hour < 0:
        check = 1

    if check == 0:
        minute = hour*60 + m - 11
        if minute < 0:
            check = 1

    if check == 0:
        print('#{} {}'.format(tc,minute))

    else:
        print('#{} {}'.format(tc,-1))