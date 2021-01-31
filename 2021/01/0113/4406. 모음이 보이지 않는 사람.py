import sys
sys.stdin = open('4406. 모음이 보이지 않는 사람.txt')

T = int(input())

for tc in range(1,1+T):

    # 단어
    word = str(input())

    # 모음 제거 후 단어
    my_word = ''

    for q in word:

        # 모음 아니면 my_word에 추가
        if q != 'a' and q != 'e' and q != 'i' and q != 'o' and q != 'u':
            my_word += q

    print('#{} {}'.format(tc,my_word))