n = int(input())
board = dict()
board[0] = 0
board[1] = 1
board[2] = 1

for q in range(3,n+1):
    board[q] = board[q-1] + board[q-2]

print(board[n])