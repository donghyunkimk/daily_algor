from collections import deque

m,n = map(int,input().split())

board = [list(map(str,input())) for _ in range(n)]

cnt = [[10000 for _ in range(m)] for _ in range(n)]

cnt[0][0] = 0

x = [1,0]
y = [0,1]

temp = deque()
temp.append([0,0])
while len(temp):
    i,j = temp.popleft()
    if i == n-1 and j == m-1:
        break

    for q in range(2):
        ii = x[q] + i
        jj = y[q] + j
        if ii < n and jj < m:
            temp_cnt = cnt[i][j]
            if board[ii][jj] == '1':
                temp_cnt += 1
                if cnt[ii][jj] > temp_cnt:
                    cnt[ii][jj] = temp_cnt
                temp.append([ii,jj])
            else:
                if cnt[ii][jj] > temp_cnt:
                    cnt[ii][jj] = temp_cnt
                temp.appendleft([ii,jj])

print(cnt[n-1][m-1])