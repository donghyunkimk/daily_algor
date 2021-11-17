# 제일 위 카드 버린다
# 제일 위 카드를 제일 아래로 옮긴다

from collections import deque

n = int(input())

board = deque([_ for _ in range(1,n+1)])

while len(board) != 1:
    board.popleft()
    board.append(board.popleft())

print(board[0])