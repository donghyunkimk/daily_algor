prime = [2]

board = [_ for _ in range(3,10**6+1,2)]

visited = [0 for _ in range(3,10**6+1,2)]

idx = 0

while True:
    p = board[idx]

    prime.append(p)

    visited[idx] = 1

    temp = 0

    for q in range(idx+1,len(board)):
        if visited[q] == 0:
            if board[q]%p == 0:
                visited[q] = 1

            else:
                if temp == 0:
                    temp = q

    idx = temp

    if len(visited) - visited.count(1) == 0:
        break

print(prime)