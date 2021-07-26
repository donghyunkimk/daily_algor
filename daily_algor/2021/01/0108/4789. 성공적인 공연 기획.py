import sys
sys.stdin = open('4789. 성공적인 공연 기획.txt')

T = int(input())

for tc in range(1,1+T):

    # 박수 칠 사람들
    board = list(str(input()))

    # 현재까지 박수 친 사람 숫자
    clap = 0

    # 모든 사람이 박수치게 만드는 데 필요한 사람 숫자
    needs = 0


    for q in range(len(board)):
        if board[q] != 0:

            # 현재까지 박수친 사람의 숫자가 q 이상일 때
            # q명 이상일 때 박수치기 때문에
            if clap >= q:
                clap += int(board[q])
            else:

                # needs에 부족한 숫자 채우고
                needs += q - clap

                # 박수친 사람 숫자 갱신
                clap = q + int(board[q])

    print('#{} {}'.format(tc,needs))