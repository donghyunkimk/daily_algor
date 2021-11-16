# 물품의 수, 무게
n,k = map(int,input().split())

# 물건의 무게
board = [list(map(int,input().split())) for _ in range(n)]
board = [[0,0]] + board

# dp 저장
ans = [[0]*(k+1) for _ in range(n+1)]

for q in range(1,n+1):

    # 무게, 가치
    w,v = board[q]

    for e in range(1,k+1):

        # 현재의 무게보다 작은 무게의 경우
        if w > e:
            ans[q][e] = ans[q-1][e]

        # 그 외의 경우
        else:
            ans[q][e] = max(ans[q-1][e-w]+v,ans[q-1][e])

print(ans[-1][-1])