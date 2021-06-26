import sys
sys.stdin = open('1961. 숫자 배열 회전.txt')

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    board = [list(map(int,input().split())) for _ in range(n)]

    res = [0]*(n*3)

    # 90도
    for q in range(n):
        temp = ''
        for w in range(n):
            temp += str(board[-1-w][q])
        res[q*3] = temp

    # 180도
    for qq in range(n):
        temp1 = ''
        for ww in range(n):
            temp1 += str(board[-1-qq][-1-ww])
        res[qq*3+1] = temp1

    # 270도
    for qqq in range(n):
        temp2 = ''
        for www in range(n):
            temp2 += str(board[www][-1-qqq])
        res[qqq*3+2] = temp2

    print('#{}'.format(tc))
    for x in range(n*3):
        if x%3 == 2:
            print(res[x], end = '')
            print()
        else:
            print(res[x], end = ' ')