T = int(input())

for tc in range(1,1+T):
    n = int(input())
    arr = list(map(int,input().split()))

    cnt = 0

    for q in range(1,n-1):

        if arr[q-1] < arr[q] < arr[q+1] or arr[q+1] < arr[q] < arr[q-1]:
            cnt += 1

    print('#{} {}'.format(tc,cnt))