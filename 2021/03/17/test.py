# tc
T = int(input())

for tc in range(1,1+T):
    s,p,q,m = map(int,input().split())

    # Ai값이 존재했는지(방문) 여부를 확인
    visited = [0]*m

    # 중복된 값을 발견했을 때, 그 값의 index값을 찾기 위해 Ai 값을 저장
    check = [0]*m

    # A0
    temp = s

    # A0 방문 확인
    visited[temp] = 1

    # A0의 값 0번 index에 저장
    check[0] = temp

    # m+1 안하면 0,0,0,1 케이스 오류 발생
    for x in range(1,m+1):
        temp_sum = (p * temp + q) % m
        temp = temp_sum

        # 중복 없으면
        if visited[temp] == 0:

            # 체크
            visited[temp] = 1

            # 해당 index에 저장
            check[x] = temp

        else:
            break

    # break 걸린 x값 - 중복된 정수의 index 값
    res = x - check.index(temp)

    print('#{} {}'.format(tc,res))