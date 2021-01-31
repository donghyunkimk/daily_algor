import sys
sys.stdin = open('2357. [AtCoder Beginner Contest 073] A. September 9.txt')

T = int(input())

for tc in range(1,1+T):
    n = list(str(input()))

    if '9' in n:
        print('#{} {}'.format(tc,'Yes'))
    else:
        print('#{} {}'.format(tc,'No'))