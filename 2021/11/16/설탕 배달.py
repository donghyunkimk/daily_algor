n = int(input())

board = [-1 for _ in range(n+1)]
board[3] = 1
lst = [3]
if n >= 5:
    board[5] = 1
    lst.append(5)

for q in range(6,n+1):
    temp = 2000
    for w in lst:
        if board[q-w] != -1:
            if board[w] + board[q-w] < temp:
                temp = board[w] + board[q-w]

    if temp != 2000:
        board[q] = temp

print(board[-1])