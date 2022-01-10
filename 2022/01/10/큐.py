import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
board = deque()
ans = deque()

for q in range(n):
    word = list(map(str,sys.stdin.readline().rstrip().split()))

    if word[0] == 'push':
        board.append(int(word[1]))
    elif word[0] == 'pop':
        if len(board) == 0:
            ans.append(-1)
        else:
            ans.append(board.popleft())
    elif word[0] == 'size':
        ans.append(len(board))
    elif word[0] == 'empty':
        if len(board) == 0:
            ans.append(1)
        else:
            ans.append(0)
    elif word[0] == 'front':
        if len(board) == 0:
            ans.append(-1)
        else:
            ans.append(int(board[0]))
    else:
        if len(board) == 0:
            ans.append(-1)
        else:
            ans.append(int(board[-1]))

for w in ans:
    print(w)