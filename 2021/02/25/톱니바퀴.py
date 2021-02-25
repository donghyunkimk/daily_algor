# 움직일 바퀴, 방향
def bfs(idx,dir):

    temp = [[idx,dir]]

    while len(temp) != 0:
        i,d = temp.pop(0)

        for q in range(2):
            ni = i+x[q]

            # 0 ~ 3 범위 초과하지 않고
            if 0 <= ni < 4:

                # 돌린적이 없는 경우
                if visited[ni] == 0:

                    # 기준 바퀴의 왼쪽
                    if ni < i:

                        # 맞닿은 극이 다른 경우
                        if wheel[i][6] != wheel[ni][2]:
                            temp.append([ni,d*(-1)])

                    # 기준 바퀴의 오른쪽
                    else:
                        if wheel[i][2] != wheel[ni][6]:
                            temp.append([ni,d*(-1)])

        # 방향이 시계방향(1)인 경우
        # 오른쪽으로 한칸씩 민다
        if d == 1:
            wheel[i].insert(0,wheel[i].pop(-1))

        # 반시계방향(-1)인 경우
        # 왼쪽으로 한칸씩 민다
        else:
            wheel[i].insert(8,wheel[i].pop(0))

        # 돌린 것 체크
        visited[i] = 1


    return

# 왼쪽 오른쪽
x = [-1,1]

# 톱니바퀴
wheel = [list(map(int,input())) for _ in range(4)]

# 회전 횟수
k = int(input())

# 회전 방법
k_detail = [list(map(int,input().split())) for _ in range(k)]

for K in k_detail:

    # 돌린 바퀴 확인용, 매번 초기화
    visited = [0]*4

    # -1은 톱니바퀴의 index랑 같게 하기 위해
    bfs(K[0]-1,K[1])

# 결과 값
res = 0

for w in range(4):

    # 12시 방향이 S극인 경우
    if wheel[w][0] == 1:

        # 1, 2, 4, 8 순서대로 더하기
        res += 1 * (2**w)

print(res)