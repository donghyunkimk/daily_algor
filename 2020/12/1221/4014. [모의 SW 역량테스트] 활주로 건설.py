import sys
sys.stdin = open('4014. [모의 SW 역량테스트] 활주로 건설.txt')

def width(wid_idx, wid_height, wid_cnt, wid_dir):
    # y좌표 고정 값, 현재 높이, 동일한 높이로 몇 번 연속되었는지, 방향?
    # wid_dir 시작은 0, 높아지면 1, 낮아지면 -1
    global res

    for q in range(n):
        if q < n-1: # 범위 제한, 다음 칸의 값을 확인하기 위해 n-2까지만

            if board[wid_idx][q+1] == wid_height: # 다음 칸의 높이가 현재 높이와 같으면
                wid_cnt += 1

                if wid_cnt == x: # 연속된 땅의 길이가 경사로의 길이와 같고
                    if wid_dir == -1: # 낮아진? 상태일 때
                        wid_cnt = 0 # 초기화
                        wid_dir = 0 # 방향성 초기화
                        # 3 3 2 2 2 3 과 같은 경우에는 222의 위치에 2개의 경사로가 필요함
                        # wid_cnt를 0으로 초기화하는 이유 == -1로 초기화할 경우, 필요 없는 곳에 땅을 사용하여
                        # 필요한 곳에 경사로를 놓지 못하는 경우 발생할 수 있음

            elif board[wid_idx][q+1] == wid_height +1: # 다음 땅의 높이가 1 높을 때(경사로 사용 가능)
                if wid_cnt >= x: # 현재까지의 땅의 길이와 경사로의 길이 확인
                    wid_height += 1 # 현재 높이 높이고
                    wid_cnt = 1 # 길이 초기화하고
                    wid_dir = 1 # 방향성 변경
                else:
                    break

            elif board[wid_idx][q+1] == wid_height -1: # 다음 땅의 높이가 1 낮아진 경우
                if wid_dir == -1:
                    # 현재 방향성이 -1인 경우 == 3 3 2 1 같은 경우
                    # 경사로를 놓을 땅을 확보하지 못해 방향성을 0으로 초기화하지 못한 경우
                    break
                else: # 그 외에는 1 높아질 때와 동일한 작업
                    wid_height -= 1
                    wid_cnt = 1
                    wid_dir = -1

            else: # 그 외의 경우 == 높이가 2 이상 높아지거나 낮아지는 경우
                break

        else:
            if wid_dir != -1: # 마지막 위치에 -1이 들어오는 경우 == 아직 방향성을 초기화하지 못한 상태 == 활주로 완성 X
                res += 1

    return

def column(col_idx, col_height, col_cnt, col_dir):
    global res

    for q in range(n):
        if q < n-1:
            if board[q + 1][col_idx] == col_height:
                col_cnt += 1

                if col_cnt == x:
                    if col_dir == -1:
                        col_cnt = 0
                        col_dir = 0

            elif board[q + 1][col_idx] == col_height + 1:
                if col_cnt >= x:
                    col_height += 1
                    col_cnt = 1
                    col_dir = 1
                else:
                    break

            elif board[q + 1][col_idx] == col_height - 1:
                if col_dir == -1:
                    break
                else:

                    col_height -= 1
                    col_cnt = 1
                    col_dir = -1

            else:
                break
        else:
            if col_dir == 1 or col_dir == 0:
                res += 1

    return

T = int(input())

for tc in range(1,1+T):
    n,x = map(int,input().split()) # n*n / x = 활주로 길이

    board = [list(map(int,input().split())) for _ in range(n)] # 절벽지대

    res = 0 # 결과

    for qq in range(n):
        width(qq,board[qq][0],1,0) # y좌표 고정
        column(qq,board[0][qq],1,0) # x좌표 고정

    print('#{} {}'.format(tc, res))