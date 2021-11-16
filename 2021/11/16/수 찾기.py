n = int(input())
board = dict()
for q in list(map(int,input().split())):
    board[q] = 1

m = int(input())
for w in list(map(int,input().split())):
    if w in board:
        print(1)
    else:
        print(0)