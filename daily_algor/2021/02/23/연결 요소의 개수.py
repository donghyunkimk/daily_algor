def bfs(idx):
    global res

    temp = [[board[idx][0],board[idx][1]]]

    while len(temp) != 0:

        i,j = temp.pop(0)

        for w in range(idx+1,m):
            if visited[w] == 0:
                if board[w][0] == i or board[w][1] == i or board[w][0] == j or board[w][1] == j:
                    visited[w] = 1
                    temp.append([board[w][0],board[w][1]])

    res += 1

    return


n,m = map(int,input().split())

# 간선의 값
board = [list(map(int,input().split())) for _ in range(m)]

board.sort(key=lambda x:(x[0],x[1]))

print(board)

visited = [0]*m

res = 0

for q in range(m):
    if visited[q] == 0:
        visited[q] = 1
        bfs(q)

print(res)