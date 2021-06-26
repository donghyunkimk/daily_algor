import sys
sys.stdin = open('3456. 직사각형 길이 찾기.txt')

T = int(input())

for tc in range(1,1+T):

    # 3개의 숫자
    number = list(map(int,input().split()))

    # 정렬
    number.sort()

    # 조건
    if number[0] != number[1]:
        print('#{} {}'.format(tc,number[0]))
    else:
        print('#{} {}'.format(tc,number[2]))