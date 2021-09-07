T = int(input())

for tc in range(1,1+T):
    a,b = map(int,input().split())

    print('#{} {}'.format(tc,(a+b)%24))