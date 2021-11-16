n = int(input())
board = [1]
idx = 1
while True:
    if board[-1] >= n:
        break

    else:
        board.append(board[idx-1]+6*idx)
        idx += 1
        
print(len(board))