import sys
sys.stdin = open('5162. 두가지 빵의 딜레마.txt')

T = int(input())

for tc in range(1,1+T):
    a,b,c = map(int,input().split())

    if a >= b:
        res = c//b
        print('#{} {}'.format(tc,res))

    else:
        res = c//a
        print('#{} {}'.format(tc,res))

# 최대한 많은 갯수의 빵을 사면 됨
# 잔돈은 신경쓰지 않아도 됨
# a+b 섞어서 사는 것보다 a b 중 더 작은 금액의 빵을 몰빵하는 것이 이득
# ex)a = 1, b = 2인 경우
# a+b == 3이지만, a == 1이다, 고로 하나만 사자