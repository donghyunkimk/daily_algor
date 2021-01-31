import sys
sys.stdin = open('2369. [AtCoder Beginner Contest 073] B. Theater.txt')

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    seats = [0] * 100001

    cnt = 0

    for q in range(n):
        L,R = map(int,input().split())

        for w in range(L,R+1):
            if seats[w] == 0:
                seats[w] = 1
                cnt += 1

    print('#{} {}'.format(tc,cnt))

