# n = int(input())
#
# board = set()
#
# for q in range(n):
#     board.add(str(input()))
#
# board = list(board)
# board.sort(key=lambda x:(len(x),x))
# 
# print("\n".join(board))
#
# n = int(input())
# board = dict()
#
# for q in range(n):
#     word = str(input())
#     if word not in board:
#         board[word] = 1
#
# board = sorted(board.keys(),key=lambda x:(len(x),x))
#
# print("\n".join(board))

n = int(input())

board = dict()

for q in range(n):
    word = str(input())
    if word not in board:
        board[word] = 1

board = sorted(board.keys(),key=lambda x:(len(x),x))

for w in board:
    print(w)