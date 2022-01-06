t = int(input())

for tc in range(1,1+t):
    n = int(input())
    board = list(map(int,input().split()))

    # dp
    ans = [0 for _ in range(n)]

    # 시작 위치
    idx = 0
    while n > idx:
        num = board[idx]
        ans[idx] += 1
        score = ans[idx]
        for q in range(idx+1,n):
            if num < board[q] and score > ans[q]:
                ans[q] += 1

        idx += 1

    print('#{} {}'.format(tc,max(ans)))