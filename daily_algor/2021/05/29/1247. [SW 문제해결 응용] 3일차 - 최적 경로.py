def search(idx, score):
    global res

    # 가지치기
    if res < score:
        return

    # 모든 곳 다 방문했으면
    if check.count(1) == n:

        # 마지막 방문지에서 집까지 거리 더해주기
        score += abs(customer[idx*2] - home[0]) + abs(customer[idx*2+1] - home[1])

        if res > score:
            res = score

        return

    for r in range(n):
        if check[r] == 0:
            check[r] = 1
            search(r, score + cu_cu[idx][r])
            check[r] = 0

    return

T = int(input())

for tc in range(1,1+T):

    # 고객 수
    n = int(input())

    # 회사 , 집 , 고객
    arr = list(map(int,input().split()))

    # 회사 좌표
    company = arr[:2]

    # 집 좌표
    home = arr[2:4]

    # 고객 좌표
    customer = arr[4:]

    # 거리 확인하기
    # 회사 -> 고객
    co_cu = [0 for _ in range(n)]

    for first in range(n):
        co_cu[first] = abs(company[0] - customer[first*2]) + abs(company[1] - customer[first*2+1])

    # 고객 -> 고객
    cu_cu = [[0]*n for _ in range(n)]

    for q in range(n):
        for w in range(n):
            cu_cu[q][w] = abs(customer[q*2] - customer[w*2]) + abs(customer[q*2+1] - customer[w*2+1])

    # 방문 체크
    check = [0 for _ in range(n)]

    # 최소 값
    res = 99999999999

    # 첫 번째 집 선택
    for e in range(n):

        # 방문
        check[e] = 1

        # 시작 위치, 현재까지의 거리
        search(e, co_cu[e])

        # 방문 해제
        check[e] = 0

    print('#{} {}'.format(tc,res))