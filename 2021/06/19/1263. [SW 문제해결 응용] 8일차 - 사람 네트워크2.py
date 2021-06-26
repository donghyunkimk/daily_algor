def bfs(idx):
    global res

    # bfs 값 저장용
    temp = []

    # 현재까지 거리의 합
    temp_res = 0

    # 방문 여부 확인
    check = [0 for _ in range(n)]

    for t in lines[idx]:
        temp.append([t,1])
        check[t] = 1
        temp_res += 1
    check[idx] = 1

    while check.count(0):

        # 현재 방문 위치, 현재 위치까지 이동한 거리
        i,cnt = temp.pop(0)

        for y in lines[i]:
            if check[y] == 0:
                check[y] = 1
                temp_res += cnt+1
                temp.append([y,cnt+1])

        # 탈출조건
        # 현재까지의 합이 res보다 큰 경우 더 확인할 필요 X
        if temp_res > res:
            break


    # res값 갱신
    if temp_res < res:
        res = temp_res

    return



T = int(input())

for tc in range(1,1+T):

    # 초기 input 값
    board = list(map(int,input().split()))

    # 사람의 수
    n = board[0]

    # n*n형태로 만들기
    arr = []
    for q in range(n):
        arr.append(board[q*n+1:(q+1)*n+1])

    # 직접 연결된 노드 확인
    lines = []
    for w in range(n):
        temp_lines = []
        for e in range(n):
            if arr[w][e] == 1:
                temp_lines.append(e)

        lines.append(temp_lines)

    # 결과 값
    res = 999999999

    # bfs
    for r in range(n):
        bfs(r)

    print('#{} {}'.format(tc,res))