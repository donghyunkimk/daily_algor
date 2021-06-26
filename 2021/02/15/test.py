# i,j,씨앗을 몇 개 뿌렸는지, 현재 결과 값, 중복 피하기 위한 temp
def dfs(i,j,cnt,res,temp):
    global min_res

    # 탈출조건
    # 씨앗 3개 뿌리면 확인하고 리턴
    if cnt == 3:
        if min_res > res:
            min_res = res
        return

    for qq in range(i,N-1):

        # y축의 시작 위치(i)에서 이동하지 않았으면
        # ex) 1,3 선택한 후, 1,4 확인하기 위해(1,1 / 1,2 처럼 이 전에 확인한 경우 피하기 위해)
        if qq == i:

            # x축은 다음 칸 부터
            for ww in range(j+1,N-1):

                # 겹치는 것 확인용 check
                check = 0

                # 임시 저장 리스트에서 하나 뽑아서
                for ee in temp:

                    # 겹치는 것 없는 경우
                    if check == 0:

                        # 12방향에서 하나라도 같은 위치가 있으면 탈출
                        for r in range(12):
                            if ee[0]+x[r] == qq and ee[1]+y[r] == ww:
                                check = 1
                                break

                    # 겹치는 것 있는 경우 탈출
                    else:
                        break

                # 다 돌았는데도, 겹치는 것 없는 경우
                if check == 0:

                    # 결과 값 더해주기
                    t_res = 0
                    for rr in range(4):
                        t_res += board[qq+x[rr]][ww+y[rr]]

                    t_res += board[qq][ww]
                    dfs(qq,ww,cnt+1,res+t_res,temp+[[qq,ww]])


        # y축의 시작위치(i)에서 이동한 경우
        else:

            # x축은 다시 처음부터 확인
            for ww in range(1,N-1):
                check = 0
                for ee in temp:
                    if check == 0:
                        for r in range(12):
                            if ee[0] + x[r] == qq and ee[1] + y[r] == ww:
                                check = 1
                                break

                    else:
                        break

                if check == 0:
                    t_res = 0
                    for rr in range(4):
                        t_res += board[qq + x[rr]][ww + y[rr]]

                    t_res += board[qq][ww]
                    dfs(qq, ww, cnt + 1, res + t_res, temp + [[qq, ww]])

    return


# 화단의 크기
N = int(input())

# 화단의 평당 가격
board = [list(map(int,input().split())) for _ in range(N)]

# 상 하 좌 우 좌상 좌하 우하 우상 상x2 하x2 좌x2 우x2
x = [-1,1,0,0,-1,1,1,-1,-2,2,0,0]
y = [0,0,-1,1,-1,-1,1,1,0,0,-2,2]

# 최소 값, 3000 = 화단의 최대 가격 200 * 선택할 수 있는 15 평
min_res = 3000

for q in range(1,N-1):
    for w in range(1,N-1):

        # 상 하 좌 우 현재위치 5가지 값 더해주기
        temp_res = 0
        for e in range(4):
            temp_res += board[q+x[e]][w+y[e]]

        temp_res += board[q][w]
        dfs(q,w,1,temp_res,[[q,w]])

print(min_res)