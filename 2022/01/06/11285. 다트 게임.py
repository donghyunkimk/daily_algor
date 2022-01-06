from collections import deque

ans = deque()

t = int(input())

for tc in range(1,1+t):
    n = int(input())

    score = 0
    for q in range(n):
        x,y = map(int,input().split())

        num = (x*x + y*y)**(1/2)
        if num <= 20:
            score += 10
        elif num <= 40:
            score += 9
        elif num <= 60:
            score += 8
        elif num <= 80:
            score += 7
        elif num <= 100:
            score += 6
        elif num <= 120:
            score += 5
        elif num <= 140:
            score += 4
        elif num <= 160:
            score += 3
        elif num <= 180:
            score += 2
        elif num <= 200:
            score += 1

    ans.append(score)

for w in range(t):
    print('#{} {}'.format(w+1,ans[w]))