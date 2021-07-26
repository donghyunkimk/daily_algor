import sys
sys.stdin = open('5549. 홀수일까 짝수일까.txt')

T = int(input())

for tc in range(1,1+T):

    # str로 받아서 인덱싱 후, 다시 int값으로 변환할 예정
    n = list(str(input()))

    if int(n[-1])%2 == 0:
        print('#{} {}'.format(tc,'Even'))
    else:
        print('#{} {}'.format(tc,'Odd'))