n = int(input())

board = []
for q in range(n):
    board.append(int(input()))

board.sort()

for w in board:
    print(w)