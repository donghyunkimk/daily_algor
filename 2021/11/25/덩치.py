n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = [1 for _ in range(n)]

for q in range(n):
    x,y = board[q]
    for w in range(q+1,n):
        xx,yy = board[w]

        if x > xx and y > yy:
            ans[w] += 1
        elif x < xx and y < yy:
            ans[q] += 1

print(*ans)

