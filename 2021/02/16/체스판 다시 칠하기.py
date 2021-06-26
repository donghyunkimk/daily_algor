def dfs(i,j,color,cnt):
    global min_res

    # 8칸 확인
    for ii in range(i,i+8):
        for jj in range(j,j+8):

            # 0,7의 색과 1,0의 색은 같음
            if jj != j+7:
                if board[ii][jj] == x[color%2]:
                    color += 1

                # 색이 다른 경우 한 cnt+1
                else:
                    color += 1
                    cnt += 1

            else:
                if board[ii][jj] != x[color%2]:
                    cnt += 1

    if min_res > cnt:
        min_res = cnt

    return



# 체스판 크기
N,M = map(int,input().split())

# 체스판
board = [list(map(str,input())) for _ in range(N)]

# 최소 값
min_res = 64

# 흰 검 이동
x = ['W','B']

# 8x8 체스판 특정하기
for q in range(N-7):
    for w in range(M-7):
        # 체스판의 시작점(0,0)의 색도 바꿀 수 있음
        # q,w,색,몇 번 바꿨는지지
        dfs(q,w,0,0)
        dfs(q,w,1,0)

print(min_res)