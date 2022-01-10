n,k = map(int,input().split())
board = []
for q in range(n):
    board.append(int(input()))

board.reverse()
ans = 0
for w in board:
    if k >= w:
        ans += k//w
        k -= k//w * w
print(ans)