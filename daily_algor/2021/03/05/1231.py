def dfs(idx):
    global res

    # 길이가 4인 경우(자식이 둘인 경우)
    if len(node[idx]) == 4:

        # 왼쪽 -> 정점 -> 오른쪽 순으로 확인
        dfs(int(node[idx][2]))
        res += node[idx][1]
        dfs(int(node[idx][3]))

    # 길이가 3인 경우(자식이 하나인 경우)
    elif len(node[idx]) == 3:
        dfs(int(node[idx][2]))
        res += node[idx][1]

    # 자식이 없는 경우
    else:
        res += node[idx][1]

    return


for tc in range(1,11):
    n = int(input())

    # 정점번호는 1부터 시작이기 때문에 앞에 0추가해서 index값 통일
    node = [[0]]+[list(map(str,input().split())) for _ in range(n)]

    res = ''

    # 정점번호
    dfs(1)

    print('#{} {}'.format(tc,res))