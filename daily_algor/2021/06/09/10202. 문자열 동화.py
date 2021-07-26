T = int(input())

for tc in range(1,1+T):

    # 문자열의 길이
    n = int(input())

    # A,B,C 문자
    a = input()
    b = input()
    c = input()

    # 문자 바꾼 횟수
    cnt = 0

    # 세 문자의 관계는 총 3 가지 경우의 수가 있다
    # 1. 두 문자가 서로 같고, 나머지 하나는 다른 경우
    # 2. 세 문자가 모두 같은 경우
    # 3. 세 문자가 모두 다른 경우
    for q in range(n):

        # 두 문자가 서로 같고, 나머지 하나는 다른 경우
        if a[q] == b[q] and a[q] != c[q]:
            cnt += 1

        elif b[q] == c[q] and a[q] != c[q]:
            cnt += 1

        elif c[q] == a[q] and a[q] != b[q]:
            cnt += 1

        # 세 문자가 모두 같은 경우
        elif a[q] == b[q] == c[q]:
            pass

        # 세 문자가 모두 다른 경우
        else:
            cnt += 2

    print('#{} {}'.format(tc,cnt))