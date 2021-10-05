T = int(input())

answer = [0 for _ in range(50001)]

for tc in range(1,1+T):
    a,b,c,d = map(int,input().split())

    if d > a and b > c:
        answer[tc] = min(b,d) - max(a,c)

for e in range(1,50001):
    if answer[e] == 0:
        print('#{} {}'.format(e,0))
    else:
        print('#{} {}'.format(e,answer[e]))