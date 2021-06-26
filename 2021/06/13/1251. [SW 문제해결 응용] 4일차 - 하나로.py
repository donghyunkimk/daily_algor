# 부모노드 찾기
def parent(idx):

    # check[idx] 값이 idx(초기 값)와 다른 경우
    if check[idx] != idx:

        # check[idx]의 부모노드 찾기
        # 찾아서 check[idx] 갱신
        check[idx] = parent(check[idx])

    return check[idx]

# 부모노드 갱신(하나의 집합인지 확인)
def union(i_idx, j_idx):
    ii = parent(i_idx)
    jj = parent(j_idx)

    if ii > jj:
        check[ii] = jj

    else:
        check[jj] = ii

T = int(input())

for tc in range(1,1+T):

    # n 개의 섬
    n = int(input())

    # 섬의 위치(x,y)
    x_idx = list(map(int,input().split()))
    y_idx = list(map(int,input().split()))

    # 섬의 위치
    island = [0 for _ in range(n)]

    for q in range(n):
        island[q] = [x_idx[q], y_idx[q]]

    # 세율
    e = float(input())

    # 선간의 거리(간선의 길이)
    lines = []

    for w in range(n):
        for r in range(w+1,n):
            if island[w][0] == island[r][0]:
                lines.append([abs(island[w][1] - island[r][1]), w, r])

            elif island[w][1] == island[r][1]:
                lines.append([abs(island[w][0] - island[r][0]), w, r])

            else:
                lines.append([(abs(island[w][0] - island[r][0]) ** 2 + abs(island[w][1] - island[r][1]) ** 2) ** (1 / 2), w, r])

    lines.sort(key=lambda x:x[0])

    # 하나의 집합인지 확인용
    # 부모노드가 적힐 예정
    check = [_ for _ in range(n)]

    # 결과값
    res = 0

    # 간선의 수 확인용
    cnt = 0

    for t in lines:
        num,i,j = t

        # i와 j의 부모노드가 다를 경우
        # == 하나의 집합이 아닐 경우
        if parent(i) != parent(j):

            # 부모노드 갱신
            union(i,j)
            res += (num**2*e)
            cnt += 1

        # 탈출조건
        # 간선의 수는 노드(n)-1
        if cnt == n-1:
            break

    print('#{} {}'.format(tc,round(res)))