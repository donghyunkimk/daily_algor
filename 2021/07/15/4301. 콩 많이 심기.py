T = int(input())

for tc in range(1,1+T):

    n,m = map(int,input().split())

    # 밭
    lst = [list(1 for _ in range(n)) for q in range(m)]

    # 심은 콩의 수
    res = 0

    for w in range(m):
        for e in range(n):

            # 콩을 못 심는 곳이 아니고
            if lst[w][e] == 1:

                # 범위 안에 있으면
                # 거리가 2인 지점을 콩을 심지 못하게 0 으로 갱신
                if w+2 < m:
                    lst[w+2][e] = 0
                if e+2 < n:
                    lst[w][e+2] = 0

                # 콩의 수 추가
                res += 1

    print('#{} {}'.format(tc,res))