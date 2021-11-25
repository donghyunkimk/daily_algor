import sys

n = int(sys.stdin.readline())

board = list(map(int,sys.stdin.readline().split()))

x = int(sys.stdin.readline())

ans = dict()
for q in board:
    if q not in ans:
        ans[q] = 1

cnt = 0
for w in board:
    if x-w in ans:
        cnt += 1

print(cnt//2)