for tc in range(1, 11):

    n = int(input())

    # str
    nodes = [[0]] + [list(input().split()) for _ in range(n)]

    # 부모 노드, 현재 값, 사칙연산
    board = [[0,0,0] for _ in range(n+1)]

    for q in range(n + 1):
        if len(nodes[q]) == 4:
            idx, car, left, right = nodes[q]

            board[q][2] = car
            board[int(left)][0] = q
            board[int(right)][0] = q

        elif len(nodes[q]) == 2:
            idx, num = nodes[q]

            board[int(idx)][1] = int(num)

    for w in range(n//2):
        if board[board[n-2*w-1][0]][2] == '+':
            board[board[n - 2 * w-1][0]][1] = board[n - 2 * w - 1][1] + board[n - 2 * w][1]

        elif board[board[n-2*w-1][0]][2] == '-':
            board[board[n - 2 * w-1][0]][1] = board[n - 2 * w - 1][1] - board[n - 2 * w][1]

        elif board[board[n-2*w-1][0]][2] == '*':
            board[board[n - 2 * w-1][0]][1] = board[n - 2 * w - 1][1] * board[n - 2 * w][1]

        else:
            board[board[n - 2 * w-1][0]][1] = board[n - 2 * w - 1][1] / board[n - 2 * w][1]

    print('#{} {}'.format(tc,int(board[1][1])))