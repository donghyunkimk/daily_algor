def check(temp_sum, idx):
    global res

    # n == idx는 끝까지 확인했다는 뜻
    # height의 index는 n-1이 끝이기 때문
    if n != idx:

        # 현재까지의 합이 선반의 높이보다 작은 경우
        if temp_sum < b:
            check(temp_sum,idx+1)
            check(temp_sum+height[idx],idx+1)

        # 그 외의 경우
        else:

            # 현재까지의 최소 값보다 현재까지의 합이 작은 경우
            if temp_sum < res:
                res = temp_sum
                return

    # 끝까지 확인한 경우
    else:

        # 현재까지의 최소 값보다 현재까지의 합이 작은 경우
        if b <= temp_sum < res:
            res = temp_sum
            return

    return


T = int(input())

for tc in range(1,1+T):

    # 점원의 수, 선반의 높이
    n,b = map(int,input().split())

    # 점원들의 키
    height = list(map(int,input().split()))

    # 결과 저장
    res = 2000000

    # 지금까지의 합, 현재 idx 값
    check(0,0)

    print('#{} {}'.format(tc,res-b))