T = int(input())

for tc in range(1,1+T):

    # 점프대의 수
    n = int(input())

    # 점프대의 높이
    h = list(map(int,input().split()))

    # 정렬
    h.sort(reverse=True)

    # 왼쪽 오른쪽 끝 값의 초기값
    l = h[0]
    r = h[0]

    idx = 1

    # 높이의 최대 차이
    h_max = 0

    while True:
        if h_max < abs(l - h[idx*2-1]):
            h_max = abs(l - h[idx*2-1])

        if h_max < abs(r - h[idx*2]):
            h_max = abs(r - h[idx*2])

        # 왼쪽 오른쪽 끝 값 갱신
        l = h[idx*2-1]
        r = h[idx*2]

        idx += 1

        # n이 홀수 일때
        if n % 2 == 1:
            if idx*2-1 == n:

                # 마지막 값들끼리 비교
                if h_max < abs(l - r):
                    h_max = abs(l - r)
                break

        # n이 짝수 일때
        else:
            if idx*2 == n:

                # n이 6일때, 1,2 / 3,4를 확인하면 5가 남으므로
                # (6은 idx범위 벗어나므로)
                # 마지막 남은 값(5)을 따로 확인
                if h_max < abs(l - h[idx*2-1]):
                    h_max = abs(l - h[idx * 2 - 1])
                l = h[idx*2-1]
                if h_max < abs(l - r):
                    h_max = abs(l - r)
                break

    print('#{} {}'.format(tc,h_max))