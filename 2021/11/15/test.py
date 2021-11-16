n,m,k = map(int,input().split())

# 상 하 좌 우
x = [0,0,-1,1]
y = [-1,1,0,0]

board = [list(map(int,input().split())) for _ in range(n)]
dice = [[0,2,0],[4,1,3],[0,5,0],[0,6,0]]


cnt = 0
ans = 0

while cnt != k:

