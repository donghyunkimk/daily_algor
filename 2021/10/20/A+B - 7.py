n = int(input())

temp = [[0,0]]

res = 0

while len(temp):
    kg, cnt = temp.pop(0)

    if kg == n:
        res = cnt
        break

    if kg + 5 <= n:
        temp.append([kg+5,cnt+1])
    if kg + 3 <= n:
        temp.append([kg+3,cnt+1])

if res != 0:
    print(res)
else:
    print(-1)