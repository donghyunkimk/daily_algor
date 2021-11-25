board = [[0 for _ in range(14)] for _ in range(15)]
board[14][0] = 1
for q in range(14):
    board[0][q] = q+1
    board[q][0] = 1

for w in range(1,15):
    for e in range(1,14):
        board[w][e] = board[w-1][e] + board[w][e-1]

t = int(input())

for r in range(t):
    k = int(input())
    n = int(input())

    print(board[k][n-1])