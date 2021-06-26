import sys
sys.stdin = open('문홍안.txt')

# 돌
stone = [0]*100

# 재산
P = int(input())

# 비서 수
N = int(input())

# 비서의 위치, 방향
dir = [list(map(str,input().split())) for _ in range(N)]

# 이동
for q in dir:

    # 오른쪽으로 이동하는 경우
    if q[1] == 'R':

        # 현재위치에서 오른쪽으로 이동하면서 +1 해주기
        # 만일 시작 위치가 0이었으면 int(q[0])-1 해서
        # 현재 위치를 밟는 경우 제거
        for w in range(int(q[0]),100):
            stone[w] += 1

    else:

        # 현재위치에서 왼쪽으로 이동하면서 +1 해주기
        # 현재 위치 밟는 경우 제거하기 위해 -1 해줌
        for e in range(0,int(q[0])-1):
            stone[e] += 1

blue = 0
red = 0
green = 0

for r in range(100):

    # 나머지가 0인 경우 파란색 추가
    if stone[r]%3 == 0:
        blue += 1

    # 나머지가 1인 경우 빨간색 추가
    elif stone[r]%3 == 1:
        red += 1

    # 나머지가 2인 경우 초록색 추가
    else:
        green += 1

print(format(P*(blue/100),".2f"))
print(format(P*(red/100),".2f"))
print(format(P*(green/100),".2f"))