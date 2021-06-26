def bfs(number):

    # 루트도 트리의 크기에 포함되기 때문에 1로 시작
    cnt = 1

    # 저장 공간
    temp = []
    for r in range(1,3):
        if storage[number][r] != 0:
            temp.append(storage[number][r])
            cnt += 1

    # bfs 돌면서 트리의 크기 확인
    while len(temp) != 0:
        item = temp.pop(0)

        for r in range(1, 3):
            if storage[item][r] != 0:
                temp.append(storage[item][r])
                cnt += 1

    return cnt

T = int(input())

for tc in range(1,1+T):

    # 정점의 수 v, 간선의 수 e, 공통조상 a,b
    v,e,a,b = map(int,input().split())

    # e개의 간선
    lst = list(map(int,input().split()))

    # 정점 간의 관계를 확인하기 위한 list
    # [부모의 값, 1번 자식, 2번 자식]
    storage = [[0,0,0] for _ in range(v+1)]

    for q in range(e):

        # 1번 자식이 없는 경우
        if storage[lst[q*2]][1] == 0:
            storage[lst[q * 2]][1] = lst[q*2+1]

        else:
            storage[lst[q * 2]][2] = lst[q*2+1]

        # 부모의 값 입력
        storage[lst[q*2+1]][0] = lst[q*2]

    # 부모 추적을 위한 빈 리스트
    a_lst = []
    b_lst = []

    # a,b 값이 모두 0에 도달할 때까지 반복해서 부모의 값을 추적
    while True:
        if a != 0:
            a = storage[a][0]
            a_lst.append(a)

        if b != 0:
            b = storage[b][0]
            b_lst.append(b)

        if a == 0 and b == 0:
            break

    # 공통조상 중 가장 가까운 것의 번호
    res_num = 0

    # 공통 조상을 찾는 절차
    for w in a_lst:
        if res_num != 0:
            break

        for e in b_lst:
            if w == e:
                res_num = w
                break

    # 그것을 루트로 하는 서브 트리의 크기
    res_cnt = bfs(res_num)

    print('#{} {} {}'.format(tc,res_num,res_cnt))