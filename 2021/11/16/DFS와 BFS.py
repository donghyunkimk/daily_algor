def dfs(i):
    for w in range(1,n+1):
        if board[i][w] == 1 and check[w] == 0:
            check[w] = 1
            ans_dfs.append(w)
            dfs(w)
    return
def bfs():
    temp = [v]

    while len(temp):
        num = temp.pop(0)
        for e in range(1,n+1):
            if board[num][e] == 1 and check[e] == 0:
                check[e] = 1
                ans_bfs.append(e)
                temp.append(e)

    return
n,m,v = map(int,input().split())

board = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
check[v] = 1

for q in range(m):
    a,b = map(int,input().split())

    board[a][b] = 1
    board[b][a] = 1

ans_dfs = [v]
ans_bfs = [v]

dfs(v)

check = [0 for _ in range(n+1)]
check[v] = 1

bfs()

print(*ans_dfs)
print(*ans_bfs)