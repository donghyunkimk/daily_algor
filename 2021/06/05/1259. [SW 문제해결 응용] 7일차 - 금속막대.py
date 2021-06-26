def dfs(idx):
    global temp
    global max_lst

    for e in range(n):

        # 방문한적 없고, 암나사 == 수나사이면
        if check_lst[e] == 0 and sort_lst[e][0] == idx:

            # 방문 체크
            check_lst[e] = 1

            # temp에 암 수 나사 추가
            temp.append(sort_lst[e][0])
            temp.append(sort_lst[e][1])

            # 함수 실행
            dfs(sort_lst[e][1])

    # max_lst보다 temp의 길이가 길면(현재의 최대 길이면)
    if len(max_lst) < len(temp):
        max_lst = temp

    return

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    temp_lst = list(map(str,input().split()))

    # append 안 하기 위해(속도 높이기 위해)
    lst = [0 for _ in range(n)]

    # lst에 저장
    for q in range(n):
        lst[q] = [temp_lst[2*q], temp_lst[2*q+1]]

    # 정렬
    sort_lst = sorted(lst, key=lambda x:x[0])

    # 최대 길이 저장
    max_lst = []

    for w in range(n):

        # 방문 확인용
        check_lst = [0 for _ in range(n)]
        temp = [sort_lst[w][0],sort_lst[w][1]]
        check_lst[w] = 1
        dfs(sort_lst[w][1])
        check_lst[w] = 0

    print('#{}'.format(tc),end=' ')
    for r in max_lst:
        print(r, end=' ')
    print()