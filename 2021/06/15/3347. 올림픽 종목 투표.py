T = int(input())

for tc in range(1,1+T):

    # 종목, 위원
    n,m = map(int,input().split())

    # 종목의 비용 리스트
    n_lst = list(map(int,input().split()))

    # 위원의 비용 리스트
    m_lst = list(map(int,input().split()))

    # 선택된 횟수 체크
    check = [0 for _ in range(n)]

    # 하나씩 확인하면서 가장 재밌는 종목 선정
    # 하나의 종목 선정하면 바로 종료
    for w in range(m):
        for e in range(n):
            if n_lst[e] <= m_lst[w]:
                check[e] += 1
                break

    res = check.index(max(check)) + 1

    print('#{} {}'.format(tc,res))