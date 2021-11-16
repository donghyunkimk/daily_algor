def bfs(idx):
    global ans
    global check

    temp = [[board[idx],idx,1]]

    while len(temp):
        cur_num, cur_idx, cnt = temp.pop(0)

        for w in range(cur_idx+1,n):
            if cnt < 2:
                temp.append([cur_num+board[w],w,cnt+1])
            else:
                if cur_num+board[w] > ans:
                    if cur_num+board[w] == m:
                        ans = cur_num+board[w]
                        temp = []
                        check = 1
                        break

                    elif cur_num+board[w] < m:
                        ans = cur_num+board[w]
    return

n,m = map(int,input().split())

board = list(map(int,input().split()))

ans = 0

check = 0

for q in range(n):
    if check == 0:
        bfs(q)

print(ans)