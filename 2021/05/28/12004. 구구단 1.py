T = int(input())

# 1 ~ 9인 a,b를 곱해서 만들 수 있는 숫자인지 확인용
board = [0 for _ in range(101)]

# 구구단
for q in range(1,10):
    for w in range(1,10):
        board[q*w] = 1

for tc in range(1,1+T):

    N = int(input())

    # a,b를 곱해서 만들 수 있는 수이면
    if board[N] == 1:
        print('#{} {}'.format(tc,'Yes'))

    else:
        print('#{} {}'.format(tc,'No'))