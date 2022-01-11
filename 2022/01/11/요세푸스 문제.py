from collections import deque
import sys

board = deque()
ans = deque()
n,k = map(int,sys.stdin.readline().rstrip().split())

for q in range(1,n+1):
    board.append(q)

idx = 0
while len(board) != 0:
    # ans.append(board.popleft((idx+k)%len(board)))
    temp = (idx+k-1)%len(board)
    ans.append(board[temp])
    del board[temp]
    idx = temp

word = '<'
for w in ans:
    word += str(w) + ', '

print(word[:-2]+'>')