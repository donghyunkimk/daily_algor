from collections import deque

t = int(input())

# tc가 50000개, append 시간 줄이기 위해 deque 사용
ans = deque()

for tc in range(1,1+t):
    a,b,c,d = map(int,input().split())

    if c > b or a > d:
        # print('#{} {}'.format(tc,0))
        ans.append(0)
    else:
        # print('#{} {}'.format(tc,min(b,d)-max(a,c)))
        ans.append(min(b,d)-max(a,c))

for q in range(50000):
    print('#{} {}'.format(q+1,ans[q]))