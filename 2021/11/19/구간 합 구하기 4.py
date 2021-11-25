from sys import stdin

n,m = map(int,stdin.readline().split())

board = [0 for _ in range(n+1)]

num = list(map(int,stdin.readline().split()))

for q in range(n):
    board[q+1] = num[q] + board[q]

for w in range(m):
    i,j = map(int,stdin.readline().split())

    print(board[j] - board[i-1])