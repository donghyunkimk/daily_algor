import sys
n = int(sys.stdin.readline().rstrip())
board = list(map(int,sys.stdin.readline().rstrip().split()))
check = list(set(board[:]))
check.sort(reverse=True)
n = len(check)
ans = dict()

for q in range(n):
    ans[check[q]] = n - 1 - q

for w in range(len(board)):
    board[w] = ans[board[w]]

print(*board)