def find(idx, color, temp_sum):
    global res

    # 탈출조건1
    # 현재까지의 합이 res보다 크면 더 확인할 필요 없음
    if temp_sum > res:
        return

    # 탈출조건2
    # idx의 값이 n-1일 때, 현재까지의 합과 res의 값을 비교
    # res보다 작으면 교체
    if idx == n-1:
        if temp_sum < res:
            res = temp_sum
        return

    # 흰색과 빨간색으로만 이루어진 국기를 방지하기위해
    # n-2를 기준으로 나눠서 확인
    # n-2 전까지는 관계없음
    if idx < n-2:
        for w in range(color,3):
            find(idx+1, w, temp_sum+cnt_board[idx][w])

    # n-2일 때에는
    # 파란색을 칠했는지 칠하지 않았는지를 기준으로 나눠서 확인
    # 칠하지 않았다면 파란색을 칠해준다
    else:
        if color >= 1:
            for w in range(color, 3):
                find(idx + 1, w, temp_sum + cnt_board[idx][w])

        else:
            find(idx+1, 1, temp_sum + cnt_board[idx][1])

    return


T = int(input())

for tc in range(1,1+T):

    # n줄 m개의 문자
    n,m = map(int,input().split())

    # 초기 국기의 색들
    board = [list(input()) for _ in range(n)]

    # 흰, 파, 빨 순서로 몇 개씩 필요한지 저장
    cnt_board = [[0 for _ in range(3)] for _ in range(n)]

    for q in range(n):
        # 흰
        cnt_board[q][0] = m-board[q].count('W')
        # 파
        cnt_board[q][1] = m-board[q].count('B')
        # 빨
        cnt_board[q][2] = m-board[q].count('R')

    # 결과 값
    res = 99999999

    # idx(현재위치), color(현재 색), 현재까지의 합(첫 줄과 마지막 줄의 합, 흰,빨로 고정)
    find(1,0,cnt_board[0][0] + cnt_board[-1][2])

    print('#{} {}'.format(tc,res))