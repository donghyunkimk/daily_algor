def dfs(idx,cur_sum):
    global res

    if cur_sum == k:
        res += 1
        return

    if cur_sum > k:
        return

    if idx == n:
        if cur_sum == k:
            res += 1

        return

    dfs(idx+1,cur_sum + arr[idx])
    dfs(idx+1,cur_sum)

    return

T = int(input())

for tc in range(1,1+T):

    n,k = map(int,input().split())

    arr = list(map(int,input().split()))

    res = 0

    for q in range(n):
        dfs(q+1,arr[q])

    print('#{} {}'.format(tc,res))