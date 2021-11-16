import timeit
start_time = timeit.default_timer()  # 시작 시간 체크

board = [1]
idx = 1
while True:
    board.append(board[idx-1]+6*idx)
    idx += 1

    if board[-1] >= 1000000000:
        break

print(board)

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))