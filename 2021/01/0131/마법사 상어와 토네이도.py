import sys
sys.stdin = open('마법사 상어와 토네이도.txt')

# 모래 날리기
# i,j,날릴 모래의 크기,날릴 방향
def blow(I, J, sand, blow_dir):
    global res

    # 얼마나 날렸는지 저장
    temp = 0

    for w in range(5):
        for e in range(5):
            if rate[blow_dir][w][e] != 0:
                if rate[blow_dir][w][e] != 'a':
                    if int(sand * rate[blow_dir][w][e]) > 0:
                        if 0 <= I + rate_x[w] < N and 0 <= J + rate_y[e] < N:
                            sandbox[I + rate_x[w]][J + rate_y[e]] += int(sand * rate[blow_dir][w][e])

                        else:
                            res += int(sand * rate[blow_dir][w][e])

                        temp += int(sand * rate[blow_dir][w][e])

                # 'a'의 위치 기억해두기
                else:
                    temp_i = I + rate_x[w]
                    temp_j = J + rate_y[e]

    # a의 위치가 모래밭 안 넘어가면
    if 0 <= temp_i < N and 0 <= temp_j < N:
        sandbox[temp_i][temp_j] += sand - temp

    # 넘어가면 결과값에 저장
    else:
        res += sand - temp

    return

# 격자의 크기
N = int(input())

# 모래밭
sandbox = [list(map(int,input().split())) for _ in range(N)]

# 시작 위치
i = N//2
j = N//2

# 방향, 왼, 아래, 오, 위
x = [0,1,0,-1]
y = [-1,0,1,0]

# 초반 방향
dir = 0

# 몇 칸 이동해야 하는지, dir_cnt[0]칸을 몇 번 이동했는지
# dir_cnt[0]칸을 2번 이동하면 dir_cnt[0]에 +1 해줘야 함
dir_cnt = [1, 0]

# 모래가 뿌려지는 비율 /// 왼쪽, 아래, 오른쪽, 위
rate = [[[0,0,0.02,0,0], [0,0.1,0.07,0.01,0], [0.05,'a',0,0,0], [0,0.1,0.07,0.01,0], [0,0,0.02,0,0]],
        [[0,0,0,0,0], [0,0.01,0,0.01,0], [0.02,0.07,0,0.07,0.02], [0,0.1,'a',0.1,0], [0,0,0.05,0,0]],
        [[0,0,0.02,0,0], [0,0.01,0.07,0.1,0], [0,0,0,'a',0.05], [0,0.01,0.07,0.1,0], [0,0,0.02,0,0]],
        [[0,0,0.05,0,0], [0,0.1,'a',0.1,0], [0.02,0.07,0,0.07,0.02], [0,0.01,0,0.01,0], [0,0,0,0,0]]]

# 함수에서 사용하기 위한 것??????
rate_x = [-2,-1,0,1,2]
rate_y = [-2,-1,0,1,2]

# 모래밭 밖으로 나가는 모래의 합
res = 0

# 탈출 조건
check = 1

while check < N * N:

    for q in range(dir_cnt[0]):
        i += x[dir]
        j += y[dir]

        blow(i,j,sandbox[i][j],dir)

        check += 1

    # 현재 방향 값이 3이면 0으로 초기화
    if dir == 3:
        dir = 0
    else:
        dir += 1

    # 이동해야할 칸의 숫자는 두 번 이동한 후 +1칸이 됨
    # 시작 지점에서 왼쪽으로 1칸, 그 다음 아래쪽으로 1칸 이동
    # 그 다음 오른쪽으로 2칸 이동 후 위쪽으로 2칸 이동
    # 다시 왼쪽으로 3칸 ... 반복 됨
    if dir_cnt[1] == 0:
        dir_cnt[1] = 1

    else:
        # 단, 마지막은(i값이 0인 행) 이 전 이동한 칸수 반복
        if i == 0 and j == N-1:
            pass

        else:
            dir_cnt[1] = 0
            dir_cnt[0] += 1

print(res)