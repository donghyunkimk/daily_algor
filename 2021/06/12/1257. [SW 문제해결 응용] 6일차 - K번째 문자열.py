T = int(input())

for tc in range(1,1+T):

    # 찾을 문자열
    k = int(input())

    # 문자열
    word = input()

    # 문자열의 길이
    num = len(word)

    # 문자열 저장할 장소
    board = []

    for q in range(num):
        for w in range(num):

            # 현재 index값(w) + 찾을 문자열의 길이(q) + 1의 길이 확인
            if w+q+1 <= num:
                board.append(word[w:w+q+1])

    # 중복 제거
    board = list(set(board))

    # 정렬
    board.sort()

    # k-1(리스트는 시작 index값이 0인데, 문제에서는 1임)
    if len(board) > k-1:
        print('#{} {}'.format(tc,board[k-1]))

    else:
        print('#{} {}'.format(tc,'none'))