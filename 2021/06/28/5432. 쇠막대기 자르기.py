T = int(input())

for tc in range(1,1+T):

    # 쇠막대기와 레이저 정보
    board = list(input())

    # 현재 위치
    idx = 0

    # 현재까지 잘린 쇠막대기의 수
    cnt = 0

    # '('의 개수
    left = 0

    while True:

        # '('인 경우
        if board[idx] == '(':

            # 바로 ')' 오면(레이저인 경우)
            if board[idx+1] == ')':
                idx += 2
                cnt += left

            # 쇠막대기의 시작위치인 경우
            else:
                idx += 1
                left += 1

        # ')'인 경우(쇠막대기의 끝인 경우)
        else:
            idx += 1

            # 어떤 막대기를 2번 자르면 3개임
            cnt += 1
            left -= 1

        # 끝까지 가면 끝내기
        if idx == len(board):
            break

    print('#{} {}'.format(tc,cnt))