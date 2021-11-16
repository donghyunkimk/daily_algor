board = [0 for _ in range(1001)]
board[2] = 1

idx = 5
new_num = 3

while True:
    check = 0
    cur_num = new_num
    board[cur_num] = 1
    for q in range(idx,1001,2):
        if q%cur_num != 0 and board[q] == 0:
            if check == 0:
                new_num = q
                idx = q+1
                check = 1
        elif q%cur_num == 0:
            board[q] = -1