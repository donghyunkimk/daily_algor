import sys
sys.stdin = open('5656. [모의 SW 역량테스트] 벽돌 깨기.txt')


def dfs():
    for j in range(w):
        for i in range(h):
            if bricks[i][j] != 0:
                bricks[i][j] = 0
                for q in range(1,bricks[i][j]):
                    for e in range(4):
                        if 0 <= i+(x[e]*q) < h and 0 <= j+(y[e]*q) < w:
                            bricks[i+(x[e]*q)][j+(y[e]*q)] = 0









x = [-1,1,0,0] # 상 하 좌 우
y = [0,0,-1,1]


T = int(input())

for tc in range(1,1+T):
    n,w,h = map(int,input().split()) # n 구슬의 수, w 길이, h 높이

    bricks = [list(map(int,input().split())) for _ in range(h)] # 벽돌들

    min_cnt = w*h

    dfs()