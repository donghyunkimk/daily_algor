import sys
sys.stdin = open('4579. 세상의 모든 팰린드롬 2.txt')

T = int(input())

for tc in range(1,1+T):

    # 단어
    word = list(str(input()))

    # 단어 길이
    n = len(word)

    # 카운트
    cnt = 0

    # 단어의 시작점, 끝점에 *이 있으면 무조건 팰린드롬임
    if word[0] == '*' or word[-1] == '*':
        print('#{} {}'.format(tc,'Exist'))

    else:
        for q in range(n//2):

            # 단어의 시작점의 값 == 끝점의 값
            # 더 반복할 필요 없음
            if word[q] == '*' or word[-1-q] == '*':
                cnt = n//2
                break

            # 해당 위치의 값과 반대편의 위치의 값이 같으면
            elif word[q] == word[-1-q]:
                cnt += 1

            # 하나라도 조건에 불일치한 경우 끝
            else:
                break

        if cnt == n//2:
            print('#{} {}'.format(tc, 'Exist'))
        else:
            print('#{} {}'.format(tc, 'Not exist'))