a, b = map(int, input().split())

board = list(map(int, input().split()))

for q in range(a // 2):
    print(board[2 * q], board[2 * q + 1])