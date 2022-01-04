T = int(input())

for tc in range(1,1+T):

    # N, P_D, P_G
    n,d,g = map(int,input().split())

    # 만들어질 수 있는 3가지 경우
    # P_G가 0%가 될 수 없는 경우
    if d != 0 and g == 0:
        print('#{} {}'.format(tc,'Broken'))

    # P_G가 100%가 될 수 없는 경우
    elif d != 100 and g == 100:
        print('#{} {}'.format(tc,'Broken'))

    # 그 외 경우
    else:
        check = 0
        for q in range(1,n+1):

            # q*d/100이 정수가 되는 순간 종료
            if (q*d/100) == (q*d//100):
                check = 1
                break
        if check == 1:
            print('#{} {}'.format(tc,'Possible'))
        else:
            print('#{} {}'.format(tc,'Broken'))