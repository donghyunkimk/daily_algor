import sys
sys.stdin = open('5789. 현주의 상자 바꾸기.txt')

T = int(input())

for tc in range(1,1+T):

    # n개의 상자, q번 동작
    n,q = map(int,input().split())

    # 숫자를 변경할 범위들의 값
    swap = [list(map(int,input().split())) for _ in range(q)]

    # n개의 상자
    board = [0]*n

    for qq in range(q):

        # board의 범위는 0부터 n-1까지
        # swap 값은 1부터 시작한다고 가정
        # -1해서 값을 조정
        for w in range(swap[qq][0]-1,swap[qq][1]):

            # qq는 0부터, 문제에서는 1부터 시작
            board[w] = qq+1

    print('#{}'.format(tc),*board)