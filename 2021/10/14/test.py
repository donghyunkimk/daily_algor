n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

board.sort(key=lambda x:x[0])

max_num = 0
res = 0

idx = 0
while idx < n:
    temp = 0

    for q in range(idx,n):

        # 팔지 말지 정하기
        # 배송비가 판매 금액보다 비싸면 안 팜
        if board[idx][0] - board[q][1] > 0:
            temp += board[idx][0] - board[q][1]

    if temp > max_num:
        max_num = temp
        res = board[idx][0]

    idx += 1

print(res)