import sys
sys.stdin = open('1219_input.txt')

def bfs():

    # 길이 연결되어 있는지 확인용
    check = 0

    temp = [0]

    visited[0] = 1

    while len(temp) != 0:
        idx = temp.pop(0)

        for w in range(2):

            # board[idx][w]에 값이 입력되었으며, 해당 값을 방문한 적이 없으면
            if board[idx][w] != -1 and visited[board[idx][w]] == 0:
                temp.append(board[idx][w])
                visited[board[idx][w]] = 1

                # 그 값이 99이면 탈출
                if board[idx][w] == 99:
                    temp = []
                    check = 1
                    break

    return check


for t in range(10):
    tc,n = map(int,input().split())

    road = list(map(int,input().split()))

    board = [[-1,-1] for _ in range(100)]

    visited = [0]*100

    for q in range(n):
        if board[road[2*q]][0] == -1:
            board[road[2*q]][0] = road[2*q+1]

        else:
            board[road[2*q]][1] = road[2*q+1]

    res = bfs()

    print('#{} {}'.format(tc,res))