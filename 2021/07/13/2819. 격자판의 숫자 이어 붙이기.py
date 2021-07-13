def dfs(i,j,cnt,cur_word):
    global res

    # 6번 움직였으면
    if cnt == 6:

        # lst 안에 cur_word 값의 key가 없으면
        if lst.get(cur_word) == None:
            lst[cur_word] = cur_word
            res += 1

        return

    # 상 하 좌 우 이동
    for e in range(4):
        ii = i + x[e]
        jj = j + y[e]

        if 0 <= ii < 4 and 0 <= jj < 4:
            dfs(ii,jj,cnt+1,cur_word+str(board[ii][jj]))

    return

T = int(input())

# 상 하 좌 우
x = [0,0,-1,1]
y = [-1,1,0,0]

for tc in range(1,1+T):

    board = [list(map(int,input().split())) for _ in range(4)]

    # 만들어지는 값 저장하기 위한 빈 딕셔너리
    lst = dict()

    # 결과 값
    res = 0

    for q in range(4):
        for w in range(4):

            # x,y,이동 횟수,현재 단어
            dfs(q,w,0,str(board[q][w]))

    print('#{} {}'.format(tc,res))