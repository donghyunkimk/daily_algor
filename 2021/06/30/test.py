T = int(input())

for tc in range(1, 1 + T):

    # 가지고 있는 카드
    card = list(input())

    # s,d,h,c
    s = [0 for _ in range(13)]
    d = [0 for _ in range(13)]
    h = [0 for _ in range(13)]
    c = [0 for _ in range(13)]

    # 중간에 탈출했는지 확인용
    check = 0

    # 출력 값
    ss = 13
    dd = 13
    hh = 13
    cc = 13

    for q in range(len(card) // 3):

        # 카드의 종류, 10의 자리, 1의 자리
        t = card[q * 3]
        x = card[q * 3 + 1]
        y = card[q * 3 + 2]

        # 카드의 번호
        num = int(x) * 10 + int(y) - 1

        if t == 'S':

            # 가지고 있지 않으면
            if s[num] == 0:
                s[num] = 1
                ss -= 1

            else:
                check = 1
                break

        elif t == 'D':
            if d[num] == 0:
                d[num] = 1
                dd -= 1

            else:
                check = 1
                break

        elif t == 'H':
            if h[num] == 0:
                h[num] = 1
                hh -= 1

            else:
                check = 1
                break

        else:
            if c[num] == 0:
                c[num] = 1
                cc -= 1

            else:
                check = 1
                break

    if check == 0:
        print('#{} {} {} {} {}'.format(tc,ss,dd,hh,cc))

    else:
        print('#{} {}'.format(tc, 'ERROR'))