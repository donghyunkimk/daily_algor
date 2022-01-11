import sys

n = int(sys.stdin.readline().rstrip())

board = list(map(int,sys.stdin.readline().rstrip().split()))

ans = [0 for _ in range(n)]

idx = 0
while idx < n:
    num = board[idx]
    ans[idx] += 1
    cnt = ans[idx]
    for q in range(idx+1,n):
        if board[q] > num and cnt > ans[q]:
            ans[q] = cnt
    idx += 1

print(max(ans))