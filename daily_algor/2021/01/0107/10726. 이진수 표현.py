import sys
sys.stdin = open('10726. 이진수 표현.txt')

T = int(input())

for tc in range(1,1+T):
    n,m = map(int,input().split())

    cnt = 0
    if len(bin(m))-2 >= n:
        for q in range(n):
            if bin(m)[-1-q] == '0':
                cnt = 1
                print('#{} {}'.format(tc,'OFF'))
                break

        if cnt == 0:
            print('#{} {}'.format(tc,'ON'))

    else:
        print('#{} {}'.format(tc,'OFF'))