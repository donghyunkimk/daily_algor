def dfs(cur_sum, idx):
    global max_res
    global min_res

    # 갱신
    if idx == n:
        if cur_sum > max_res:
            max_res = cur_sum

        if min_res > cur_sum:
            min_res = cur_sum
        return

    for q in range(4):
        if cal[q] != 0:
            if q == 0:
                cal[q] -= 1
                dfs(cur_sum+num[idx], idx+1)

                # 연산자 + 안 해주면 -가 누적
                # 한 바퀴 돌면 0 0 0 0으로 변함
                cal[q] += 1

            elif q == 1:
                cal[q] -= 1
                dfs(cur_sum - num[idx], idx + 1)
                cal[q] += 1

            elif q == 2:
                cal[q] -= 1
                dfs(cur_sum * num[idx], idx + 1)
                cal[q] += 1

            else:
                cal[q] -= 1

                # 소수점 버리기 위해 //으로 처리하면
                # 반올림 처리 되어버림
                dfs(int(cur_sum / num[idx]), idx + 1)
                cal[q] += 1

    return

T = int(input())

for tc in range(1,1+T):

    # 숫자의 개수
    n = int(input())

    # 연산자 + - * / 순서
    cal = list(map(int,input().split()))

    # 수식에 사용되는 숫자
    num = list(map(int,input().split()))

    # 최대값, 최소값
    max_res = -100000000
    min_res = 100000000

    # 현재까지의 합, 확인해야할 숫자의 위치(index)
    dfs(num[0],1)

    print('#{} {}'.format(tc,max_res-min_res))