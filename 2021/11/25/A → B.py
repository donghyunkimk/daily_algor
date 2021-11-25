import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())

temp = deque([a,1])
ans = 1
while len(temp):
    num = temp.popleft()
    cnt = temp.popleft()

    if num*2 < b:
        temp.append(num*2)
        temp.append(cnt+1)
    elif num*2 == b:
        ans = cnt + 1
        break

    if int(str(num) + '1') < b:
        temp.append(int(str(num) + '1'))
        temp.append(cnt+1)
    elif int(str(num) + '1') == b:
        ans = cnt + 1
        break

if ans == 1:
    print(-1)
else:
    print(ans)