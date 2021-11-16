n = int(input())

board = [0 for _ in range(n + 1)]

if n == 2:
    board[2] = 1

elif n > 2:
    board[2] = 1
    board[3] = 1
    for q in range(4, n + 1):

        # 2 or 3으로 나눠지는 경우
        if q % 2 == 0 or q % 3 == 0:
            temp = n

            # 2로 나눠지는 경우
            if q % 2 == 0:
                if temp > board[2] + board[q // 2]:
                    temp = board[2] + board[q // 2]

            # 3으로 나눠지는 경우
            if q % 3 == 0:
                if temp > board[3] + board[q // 3]:
                    temp = board[3] + board[q // 3]

            # 빼기 1 하는 경우
            if temp > board[q - 1] + 1:
                temp = board[q - 1] + 1

            board[q] = temp

        # 2,3으로 나눠지지 않는 경우
        else:
            board[q] = board[q - 1] + 1

print(board[n])