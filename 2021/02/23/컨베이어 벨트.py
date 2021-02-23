# n 컨베이어 벨트 길이, k 탈출조건
n,k = map(int,input().split())

# 컨베이어 벨트 내구도
belt = list(map(int,input().split()))

# 로봇의 위치
robot_idx = [0]*n

# 출력 단계
res = 1

# k와 비교하기 위한 값
cnt = 0

while True:

    # 벨트 이동
    belt.insert(0,belt.pop(-1))

    # 컨베이어 벨트의 이동에 따라 로봇의 위치도 조정
    # 마지막 위치는 바닥으로
    # 마지막 위치에 도달한 로봇은 바닥으로 뛰어 내림
    robot_idx.insert(0,0)
    robot_idx.pop(-1)
    robot_idx[-1] = 0

    for q in range(2,n+1):

        # 로봇이 올라가있고
        if robot_idx[-q] != 0:

            # 이동할 위치가 비어있고
            # 이동할 위치의 내구도가 1 이상인 경우
            # 이동하고, 내구도 감소
            if robot_idx[1-q] == 0 and belt[n+1-q] > 0:
                robot_idx[1 - q] = 1
                robot_idx[-q] = 0
                belt[n + 1 - q] -= 1

                # 내구도가 0이면 cnt + 1 해주기
                if belt[n + 1 - q] == 0:
                    cnt += 1

    # 탈출조건
    if cnt >= k:
        break

    # index 0 의 자리가 비어있고, 내구도가 1 이상이면
    if robot_idx[0] == 0 and belt[0] > 0:
        robot_idx[0] = 1
        belt[0] -= 1

        if belt[0] == 0:
            cnt += 1

    # 탈축조건
    if cnt == k:
        break

    # 다 돌면 현재 단계 + 1
    res += 1

print(res)