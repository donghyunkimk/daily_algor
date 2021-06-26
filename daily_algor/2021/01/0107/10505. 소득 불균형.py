import sys
sys.stdin = open('10505. 소득 불균형.txt')

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    income = list(map(int,input().split()))

    income_avg = sum(income)/n

    cnt = 0
    for q in income:
        if q <= income_avg:
            cnt += 1

    print('#{} {}'.format(tc,cnt))