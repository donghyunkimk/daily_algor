T = int(input())

for tc in range(1,1+T):

    # 기준 값
    arr = list(str(input()))

    # 초기 값
    base = [0 for _ in range(len(arr))]

    cnt = 0

    for q in range(len(arr)):
        if int(arr[q]) != base[q]:
            cnt += 1
            for w in range(q,len(arr)):
                base[w] = int(arr[q])

    print('#{} {}'.format(tc,cnt))
