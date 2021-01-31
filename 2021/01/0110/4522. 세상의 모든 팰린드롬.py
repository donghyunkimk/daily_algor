import sys
sys.stdin = open('4522. 세상의 모든 팰린드롬.txt')

T = int(input())

for tc in range(1,1+T):

    # 확인할 단어
    word = str(input())

    # 단어 길이 // 2
    word_len = len(word)//2

    # 끝까지 다 돌았는지 확인용 == 팰린드롬인지 확인
    cnt = 0

    for q in range(word_len):

        # 같은 경우, 하나의 알파벳이 ?인 경우
        if word[q] == word[-q-1] or word[q] == '?' or word[-q-1] == '?':
            cnt += 1
        else:

            # 조건에 부합하지 않으면 바로 종료
            break

    if cnt == word_len:
        print('#{} {}'.format(tc,'Exist'))
    else:
        print('#{} {}'.format(tc,'Not exist'))

# 짝수 홀수 조심