T = int(input())

# 이동 방향
# 이동 X 상 우 하 좌
x = [0,0,1,0,-1]
y = [0,-1,0,1,0]

for tc in range(1,1+T):

    # 이동 시간 m, BC의 개수 a
    m,a = map(int,input().split())

    # 이동 정보
    move_a = list(map(int,input().split()))
    move_b = list(map(int,input().split()))

    # BC의 정보
    board = [0 for _ in range(a)]
    for q in range(a):

        # 위치, 범위 c, 성능 p
        # 위치에서 -1씩 해줘야 함
        board[q] = list(map(int,input().split()))

    # 현재 위치
    idx_a = [0,0]
    idx_b = [9,9]

    # 현재까지의 합
    res = 0

    # 이동 정보 불러오기 위한 idx
    # 초기 위치에서도 충전하기 위해 -1로 시작
    idx = -1
    while idx != m:

        # 현재 최대 값
        temp_res = 0

        a_i, a_j = idx_a
        b_i, b_j = idx_b

        # BC 불러와서 조건 확인
        for w in range(a):
            w_i, w_j, w_c, w_p = board[w]
            temp_a = 0

            # BC의 범위 안에 있는지 확인
            if abs(w_i - a_i - 1) + abs(w_j - a_j - 1) <= w_c:
                temp_a += w_p

            for e in range(a):
                e_i, e_j, e_c, e_p = board[e]
                temp_b = 0
                if abs(e_i - b_i - 1) + abs(e_j - b_j - 1) <= e_c:

                    # 같은 BC 조건으로 확인하고, a도 그 BC 안에 있으면
                    # BC를 나눠 갖는데, 이미 a에서 더했으므로 더해줄 필요 없음
                    if w == e and temp_a != 0:
                        pass
                    else:
                        temp_b += e_p

                # 현재 최대 값 갱신
                if temp_res < temp_a + temp_b:
                    temp_res = temp_a + temp_b

        idx += 1

        if idx != m:
            idx_a = [idx_a[0] + x[move_a[idx]], idx_a[1] + y[move_a[idx]]]
            idx_b = [idx_b[0] + x[move_b[idx]], idx_b[1] + y[move_b[idx]]]

        res += temp_res

    print('#{} {}'.format(tc,res))