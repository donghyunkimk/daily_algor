import sys

n = int(sys.stdin.readline().rstrip())

board = list(map(int,sys.stdin.readline().rstrip().split()))

board.sort()

ans = 0
for q in range(n):
    ans += board[q] * (n-q)

print(ans)