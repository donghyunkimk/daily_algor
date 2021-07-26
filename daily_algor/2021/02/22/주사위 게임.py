def move(num,location):
    global loc
    global cnt

    # 현재 위치 + 주사위 숫자가 n-1보다 작으면
    if location+num < n-1:

        # 현재 위치 + 주사위 숫자 + 보드 판에 적혀있는 숫자
        loc = location + num + board[location+num]

    # n-1 이상이면
    else:

        # 현재 위치 + 주사위 숫자
        loc = location + num

    cnt += 1

    return


n,m = map(int,input().split())

# 게임판
board = [int(input()) for _ in range(n)]

# 움직여야 할 숫자
dice = [int(input()) for _ in range(m)]

# 현재 위치
loc = 0

# 주사위 몇 번 사용했는지
cnt = 0

for q in dice:

    # 게임판의 크기는 n이므로 마지막 index값은 n-1임
    # 마지막에 도달하거나, 그 이상 숫자가 나오지 않은 경우
    if loc < n-1:
        move(q,loc)

    else:
        break

print(cnt)