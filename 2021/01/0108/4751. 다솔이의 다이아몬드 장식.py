import sys
sys.stdin = open('4751. 다솔이의 다이아몬드 장식.txt')

T = int(input())

for tc in range(1,1+T):

    # 단어
    word = str(input())

    # 단어의 길이
    word_len = len(word)

    # .으로 5줄 만들기
    # 4*word_len+1은 장식 후 문자열의 가로 길이
    board = [['.']*(4*word_len+1) for _ in range(5)]

    # 글자를 인덱싱하기 위한 값
    idx = 0

    for q in range(4*word_len+1):

        # .을 #으로 변경
        if q%4 == 0:
            board[2][q] = '#'

        # 위 아래 .을 #으로 변경
        elif q%4 == 1 or q%4 == 3:
            board[1][q] = '#'
            board[3][q] = '#'

        # 단어 넣고, 위로 2칸 아래로 2칸의 .을 #으로 변경
        else:
            board[0][q] = '#'
            board[4][q] = '#'
            board[2][q] = word[idx]
            idx += 1

    for w in board:
        for e in w:
            print(e,end='')
        print()