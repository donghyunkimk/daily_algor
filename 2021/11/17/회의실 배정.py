n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

board.sort(key=lambda x:(x[1],x[0]))

ans = 1
now = board[0][1]
for q in board[1:]:
    if q[0] >= now:
        now = q[1]
        ans += 1

print(ans)