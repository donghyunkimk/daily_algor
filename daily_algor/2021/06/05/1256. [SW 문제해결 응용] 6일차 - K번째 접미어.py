T = int(input())

for tc in range(1,1+T):

    # k번째
    k = int(input())

    # 문자열
    word = input()

    # 문자열 저장을 위해 미리 만들어둔 빈 리스트
    # .append 사용하면 시간이 오래걸림
    temp_lst = [0 for _ in range(len(word))]

    for q in range(len(word)):

        # 새로운 문자열 저장
        # 대문자로 인해 순서 어긋나는 것 배제를 위한 .lower
        temp_lst[q] = word[q:].lower()

    # 정렬
    temp_lst.sort()

    # none 출력 조건
    if k-1 > len(word):
        print('#{} {}'.format(tc,'none'))

    # 그 외
    else:
        print('#{} {}'.format(tc,temp_lst[k-1]))