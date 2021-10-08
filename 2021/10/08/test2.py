def find():

    temp = [[]]

    for w in range(n):
        temp.append([[w],[]])
        temp.append([[w],[w]])

    return

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

res = 50000

for q in range(n//2+1):
    find()

print(res)