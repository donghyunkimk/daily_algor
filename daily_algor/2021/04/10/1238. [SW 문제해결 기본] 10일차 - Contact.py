def bfs():
    global res_idx
    global res

    temp = [[s,0]]

    while len(temp) != 0:
        idx, cnt = temp.pop(0)

        # cnt 값이 최근에 연락받은 사람의 숫자보다 크면(더 늦게 연락 받으면)
        if cnt > res_idx:

            # res_idx값 변경
            res_idx = cnt

            # res 값 초기화 후 idx 추가
            res = []
            res.append(idx)

        # cnt와 res_idx이 같으면
        elif cnt == res_idx:

            # idx 추가
            res.append(idx)

        for w in range(1,101):

            # 연결된 사람이며(연락해야 하는 사람), 상대방이 연락받은 적 없으면(방문 X)
            if board[idx][w] == 1 and visited[w] == 0:
                temp.append([w,cnt + 1])
                visited[w] = 1


    return

for tc in range(1,11):

    # 데이터의 길이 n 시작점 s
    n,s = map(int,input().split())

    # 연락망
    contact = list(map(int,input().split()))

    # 연락 관계 저장
    board = [[0]*101 for _ in range(101)]

    # 방문 확인
    visited = [0 for _ in range(101)]

    # board에 관계 저장
    for q in range(n//2):
        board[contact[2*q]][contact[2*q+1]] = 1

    # 가장 나중에 연락받는 사람들 저장
    res = []

    # 가장 나중에 연락받는 사람의 연락받는 순서
    res_idx = -1

    bfs()

    print('#{} {}'.format(tc,max(res)))