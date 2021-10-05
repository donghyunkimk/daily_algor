T = int(input())

answer = [0 for _ in range(50001)]

for tc in range(1,1+T):
    a,b,c,d = map(int,input().split())

    time = [0 for _ in range(101)]
    for q in range(a,b+1):
        time[q] += 1

    for w in range(c,d+1):
        time[w] += 1

    answer[tc] = time.count(2)

for e in range(1,50001):
    if answer[e] == 0:
        print('#{} {}'.format(e,0))
    else:
        print('#{} {}'.format(e,answer[e]-1))