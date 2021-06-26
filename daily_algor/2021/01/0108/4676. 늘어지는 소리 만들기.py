import sys
sys.stdin = open('4676. 늘어지는 소리 만들기.txt')

T = int(input())

for tc in range(1,1+T):

    # 초기 글자
    word = list(str(input()))

    # 문자열의 길이
    l = len(word)

    # 삽입할 하이픈의 갯수
    h = int(input())

    # 하이픈을 넣을 위치
    word_insert = list(map(int,input().split()))

    # 정렬
    word_insert.sort(reverse=True)

    # - 집어 넣기
    for q in word_insert:
        word.insert(q,'-')

    # 출력
    print('#{}'.format(tc),end=' ')
    for num in range(len(word)):
        if num != len(word)-1:
            print(word[num],end='')
        else:
            print(word[num])


# 정렬한 이유는 작은 숫자부터 -을 넣으면 뒤에 글자의 위치가 변경됨
# ex) 2 2 3의 위치에 '-'을 넣을 때
# wo-w = > wo--w => wo---w가 됨
# 그러나 3 2 2 순서면
# wow- => wo-w- => wo--w-
# 물론 내가 생각한 방법 & 코드에 한정된 아이디어임