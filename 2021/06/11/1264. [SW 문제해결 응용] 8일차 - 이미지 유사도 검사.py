T = int(input())

for tc in range(1,1+T):
    # 코드열의 길이
    n = int(input())

    # x,y
    x = list(input())
    y = list(input())

    # LCS를 구현하기 위한 2차원 배열
    board = [[0 for one in range(n+1)] for two in range(n+1)]

    res = 0
    for q in range(n):
        for w in range(n):

            # 값이 같을 때, 현재 위치(x,y)에서 -1만큼 해준 곳(x-1,y-1)의 값 +1
            if x[q] == y[w]:
                board[q+1][w+1] = board[q][w] + 1
                if board[q+1][w+1] > res:
                    res = board[q+1][w+1]

            # 값이 다를 때, 현재 위치 기준 왼쪽, 위의 값 중 큰 값을 현재 위치의 값으로
            else:
                board[q+1][w+1] = max(board[q+1][w],board[q][w+1])

    print('#{}'.format(tc),end=" ")
    print(format(res/n*100,".2f"))