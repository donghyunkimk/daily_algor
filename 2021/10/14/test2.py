t,a,s,b = map(int,input().split())

board = list(map(int,input().split()))

board.sort()

res = dict()

for q in range(1,a//2+1):
