T = int(input())

for tc in range(1,1+T):
    n,p = map(int,input().split())

    res = 1

    cnt = n - n//p*p

    for q in range(p-cnt):
        res *= (n//p)

    for w in range(cnt):
        res *= (n//p+1)

    print('#{} {}'.format(tc,res))